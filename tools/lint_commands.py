"""Syntax-checks every generated command against Minecraft's 1.20 command tree.

Needs the `mecha` package (pip install mecha); it is a development check, not part of the build.

    python3 tools/lint_commands.py

Checks: every .mcfunction file, every command inside Palladium powers (command abilities and
command_result conditions), every function a command calls, and that every scoreboard objective
the commands use is created in load.mcfunction.
"""
import json
import re
import sys
from pathlib import Path

from mecha import DiagnosticError, Mecha

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
NS = "greenlantern"


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
    for path in sorted((SRC / "data" / NS / "palladium" / "powers").glob("*.json")):
        power = json.loads(path.read_text())
        for name, ab in power["abilities"].items():
            for key in ("first_tick_commands", "commands", "last_tick_commands"):
                for cmd in ab.get(key, []):
                    yield f"{path.stem}/{name}", cmd
            for cond in walk(ab.get("conditions", {})):
                if cond.get("type") == "palladium:command_result":
                    yield f"{path.stem}/{name} (condition)", cond["command"]


def main():
    mc = Mecha(version="1.20")
    errors = []
    commands = list(collect())
    for where, cmd in commands:
        if cmd.startswith(("curios ", "energybar ")) or " run curios " in cmd or " run energybar " in cmd:
            continue  # Curios' and Palladium's own commands aren't in vanilla's command tree
        try:
            mc.parse(cmd + "\n", multiline=True)
        except DiagnosticError as e:
            errors.append(f"{where}: {cmd[:160]}\n      {e.diagnostics.exceptions[0].message}")

    functions = {str(p.relative_to(SRC / "data" / NS / "functions"))[:-len(".mcfunction")]
                 for p in (SRC / "data" / NS / "functions").rglob("*.mcfunction")}
    load = (SRC / "data" / NS / "functions" / "load.mcfunction").read_text()
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
                errors.append(f"{where}: objective {obj} is never created in load.mcfunction")

    print(f"Checked {len(commands)} commands")
    if errors:
        print(f"{len(errors)} problem(s):")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
