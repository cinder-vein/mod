"""Syntax-checks every generated command against Minecraft's 1.20 command tree.

Needs the `mecha` package (pip install mecha); it is a development check, not part of the build.

    python3 tools/lint_commands.py

Checks: every .mcfunction file, every command inside Palladium powers (command abilities and
command_result conditions), every function a command calls, and that every scoreboard objective
the commands use is created in a load function.

src/ is A New Corps (base/) plus what tools/gen_final.py adds: problems already in base/ are reported as inherited
(other mods' commands, for one), and only new ones fail.
"""
import json
import re
import sys
from pathlib import Path

from mecha import DiagnosticError, Mecha

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
BASE = ROOT / "base"
NS = "final_lanterns"


def walk(node):
    if isinstance(node, dict):
        yield node
        for v in node.values():
            yield from walk(v)
    elif isinstance(node, list):
        for v in node:
            yield from walk(v)


def collect():
    """Yields (where, command) for every command in the pack."""
    for path in sorted((SRC / "data").rglob("*.mcfunction")):
        for n, line in enumerate(path.read_text().splitlines(), 1):
            if line.strip() and not line.startswith("#"):
                yield f"{path.relative_to(SRC)}:{n}", line
    for path in sorted((SRC / "data" / NS / "palladium" / "powers").rglob("*.json")):
        power = json.loads(path.read_text())
        for name, ab in power["abilities"].items():
            for key in ("first_tick_commands", "commands", "last_tick_commands"):
                for cmd in ab.get(key, []):
                    yield f"{path.stem}/{name}", cmd
            for cond in walk(ab.get("conditions", {})):
                if cond.get("type") == "palladium:command_result":
                    yield f"{path.stem}/{name} (condition)", cond["command"]


def lint(src):
    """Returns (commands checked, problems) for the pack in `src`."""
    global SRC
    SRC = src
    mc = Mecha(version="1.20")
    errors = []
    commands = list(collect())
    for where, cmd in commands:
        sp = re.search(r"(?:^| run )superpower (.*)$", cmd)
        if sp and not re.fullmatch(r"(?:add|remove) [a-z0-9_.-]+:[a-z0-9_/.-]+ @[aeprs](?:\[[^\]]*\])?", sp.group(1)):
            errors.append(f"{where}: {cmd[:160]}\n      expected 'superpower add|remove <power> <selector>'")
        if cmd.startswith(("curios ", "energybar ", "superpower ")) or any(
                f" run {c} " in cmd for c in ("curios", "energybar", "superpower")):
            continue  # Curios' and Palladium's own commands aren't in vanilla's command tree
        try:
            mc.parse(cmd + "\n", multiline=True)
        except DiagnosticError as e:
            errors.append(f"{where}: {cmd[:160]}\n      {e.diagnostics.exceptions[0].message}")

    functions = {str(p.relative_to(SRC / "data" / NS / "functions"))[:-len(".mcfunction")]
                 for p in (SRC / "data" / NS / "functions").rglob("*.mcfunction")}
    tag = SRC / "data" / "minecraft" / "tags" / "functions" / "load.json"
    loaders = [v["id"] if isinstance(v, dict) else v for v in json.loads(tag.read_text())["values"]] if tag.exists() else []
    load = "".join(p.read_text() for p in (SRC / "data" / NS / "functions").glob("**/load.mcfunction"))
    load += "".join((SRC / "data" / ns / "functions" / f"{path}.mcfunction").read_text()
                    for ns, _, path in (v.partition(":") for v in loaders)
                    if (SRC / "data" / ns / "functions" / f"{path}.mcfunction").exists())
    objectives = set(re.findall(r"scoreboard objectives add (\S+)", load))
    obj_patterns = [
        r"scoreboard players (?:set|add|remove|reset|enable|get) \S+ (\S+)",
        r"scoreboard players operation \S+ (\S+) \S+ \S+ (\S+)",
        r"(?:if|unless) score \S+ (\S+)(?: (?:=|<|<=|>|>=) \S+ (\S+))?",
        r"store result score \S+ (\S+)",
        r'"objective":\s*"([^"]+)"',
    ]
    for where, cmd in commands:
        if cmd.startswith("tellraw"):
            continue  # help text mentions functions and objectives by name
        for t in re.findall(rf"function #{NS}:([a-z0-9_/]+)", cmd):
            if not (SRC / "data" / NS / "tags" / "functions" / f"{t}.json").exists():
                errors.append(f"{where}: calls missing function tag #{NS}:{t}")
        for f in re.findall(rf"function {NS}:([a-z0-9_/]+)", cmd):
            if f not in functions:
                errors.append(f"{where}: calls missing function {NS}:{f}")
        used = set()
        for pat in obj_patterns:
            for m in re.findall(pat, cmd):
                used.update([m] if isinstance(m, str) else [x for x in m if x])
        for sel in re.findall(r"scores=\{([^}]*)\}", cmd):
            used.update(k.split("=")[0] for k in sel.split(","))
        for obj in used:
            if obj.startswith("gl_") and obj not in objectives:
                errors.append(f"{where}: objective {obj} is never created in a load function")
    return len(commands), errors


def main():
    _, inherited = lint(BASE) if BASE.exists() else (0, [])
    count, found = lint(ROOT / "src")
    # host powers are copies of ring powers: their copied commands' problems are the ring's
    sys.path.insert(0, str(ROOT / "tools"))
    import entities
    from common import CORPS
    hosts = {f"host_{e.key}": CORPS[e.corps]["power"] for e in entities.ENTITIES}

    def norm(e):
        e = re.sub(r":\d+:", ":", e)
        for host, ring in hosts.items():
            e = e.replace(f"{NS}:{host}", f"{NS}:{ring}").replace(f"{host}/", f"{ring}/")
        return e

    known = {norm(e) for e in inherited}  # line numbers may shift in patched files
    new = [e for e in found if norm(e) not in known]
    print(f"Checked {count} commands ({len(inherited)} problems inherited from A New Corps, not counted)")
    if new:
        print(f"{len(new)} problem(s):")
        for e in new:
            print("  -", e)
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
