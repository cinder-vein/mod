"""Checks that every item, block, entity type, effect, particle, attribute, enchantment and damage type our commands
name exists in Minecraft 1.20.1 or is registered by this jar.

Minecraft checks these when it loads a function, and one unknown name drops the whole function file (it logs
"Failed to load function ..." and the function is simply missing). Mecha (tools/lint_commands.py) only checks the
syntax, so this fills that gap.

    python3 tools/check_refs.py [path/to/mcmeta-1.20.1-registries]

The vanilla names come from misode's mcmeta registries (the "registries" branch for 1.20.1); without them only the
modded names are checked. What this jar registers: Palladium addon items, blocks and particle types under addon/,
and what A New Corps' KubeJS startup scripts register (its batteries and effects). Names from other mods we depend on
are listed in OTHER_MODS.

Problems already in base/ (A New Corps' own functions) are reported as inherited and don't fail.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NS = "final_lanterns"

# registered by mods Final Lanterns requires (checked against their 1.20.1 sources)
OTHER_MODS = {
    "item": set(), "block": set(), "particle_type": set(), "mob_effect": set(), "attribute": set(),
    "enchantment": set(), "damage_type": set(),
    "entity_type": {"palladium:effect", "palladium:custom_projectile", "palladium:suit_stand",
                    "palladium:custom_fireball"},
}

# command (after "execute ... run") -> [(registry, regex that captures the name)]
ID = r"(#?!?[a-z0-9_.-]+:[a-z0-9_/.-]+|#?[a-z0-9_/.-]+)"
POS = r"(?:[~^]?-?[0-9.]*\s+){3}"
PATTERNS = [
    (r"^give\s+\S+\s+" + ID, "item"),
    (r"^clear\s+\S+\s+" + ID, "item"),
    (r"^item\s+replace\s+.*?\swith\s+" + ID, "item"),
    (r"^summon\s+" + ID, "entity_type"),
    (r"^setblock\s+" + POS + ID, "block"),
    (r"^fill\s+" + POS + POS + ID, "block"),
    (r"^fill\s+" + POS + POS + r"\S+\s+replace\s+" + ID, "block"),
    (r"^effect\s+(?:give|clear)\s+\S+\s+" + ID, "mob_effect"),
    (r"^particle\s+" + ID, "particle_type"),
    (r"^attribute\s+\S+\s+" + ID, "attribute"),
    (r"^enchant\s+\S+\s+" + ID, "enchantment"),
    (r"^damage\s+\S+\s+\S+\s+" + ID, "damage_type"),
]
# inside execute chains
EXECUTE = [(r"\b(?:if|unless)\s+block\s+" + POS + ID, "block")]
SELECTOR_TYPE = re.compile(r"[\[,]type=!?([a-z0-9_.-]+:[a-z0-9_/.-]+|[a-z0-9_/.-]+)")


def full(name):
    return name if ":" in name else f"minecraft:{name}"


def vanilla(registries):
    out = {}
    for reg in ("item", "block", "entity_type", "mob_effect", "particle_type", "attribute", "enchantment"):
        path = registries / reg / "data.json"
        out[reg] = {full(n) for n in json.loads(path.read_text())} if path.exists() else None
    dmg = registries.parent / "mcmeta-1.20.1-data" / "data" / "minecraft" / "damage_type"
    out["damage_type"] = {f"minecraft:{p.stem}" for p in dmg.glob("*.json")} if dmg.exists() else None
    return out


def ours(src):
    """What this jar registers."""
    reg = {k: set(v) for k, v in OTHER_MODS.items()}
    for addon in (src / "addon").glob("*"):
        ns = addon.name
        reg["item"] |= {f"{ns}:{p.relative_to(addon / 'items').with_suffix('').as_posix()}"
                        for p in (addon / "items").rglob("*.json")}
        blocks = {f"{ns}:{p.relative_to(addon / 'blocks').with_suffix('').as_posix()}"
                  for p in (addon / "blocks").rglob("*.json")}
        reg["block"] |= blocks
        reg["item"] |= blocks
        reg["particle_type"] |= {f"{ns}:{p.stem}" for p in (addon / "particle_types").rglob("*.json")}
        for js in (addon / "kubejs_scripts").glob("*.js"):
            text = js.read_text(encoding="utf-8", errors="replace")
            for m in re.finditer(r"StartupEvents\.registry\(\s*['\"]([a-z_:]+)['\"]", text):
                kind = {"item": "item", "block": "block", "mob_effect": "mob_effect"}.get(m.group(1))
                if not kind:
                    continue
                end = text.find("StartupEvents.registry", m.end())
                for c in re.findall(r"\.create\(\s*['\"]([a-z0-9_:/]+)['\"]", text[m.end():end if end > 0 else None]):
                    name = c if ":" in c else f"kubejs:{c}"
                    reg[kind].add(name)
                    if kind == "block":
                        reg["item"].add(name)
    return reg


def commands(src):
    funcs = src / "data"
    for path in sorted(funcs.rglob("*.mcfunction")):
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.strip() and not line.lstrip().startswith("#"):
                yield f"{path.relative_to(src)}", n, line.strip()
    for path in sorted((funcs / NS / "palladium" / "powers").rglob("*.json")):
        try:
            power = json.loads(path.read_text(encoding="utf-8"))
        except ValueError:
            continue
        for name, ab in (power.get("abilities") or {}).items():
            for key in ("first_tick_commands", "commands", "last_tick_commands"):
                for cmd in ab.get(key) or []:
                    if isinstance(cmd, str):
                        yield f"{path.relative_to(src)} {name}", 0, cmd.strip()


def strip_text(cmd):
    """Drops quoted strings and JSON text, which hold names that aren't commands."""
    return re.sub(r'"(?:[^"\\]|\\.)*"', '""', cmd)


def check(src, known):
    problems = []
    for where, n, cmd in commands(src):
        if cmd.startswith(("tellraw", "title", "bossbar")) and " run " not in cmd:
            continue
        bare = strip_text(cmd)
        found = []
        for m in SELECTOR_TYPE.finditer(bare):
            found.append(("entity_type", m.group(1)))
        for pat, reg in EXECUTE:
            for m in re.finditer(pat, bare):
                found.append((reg, m.group(1)))
        tail = bare.split(" run ")[-1].lstrip("/")
        if bare.startswith("execute") and " run " not in bare:
            tail = ""
        for pat, reg in PATTERNS:
            m = re.match(pat, tail)
            if m:
                found.append((reg, m.group(1)))
        for reg, name in found:
            name = name.lstrip("!")
            if name.startswith("#"):
                continue  # tags are looked up when the command runs
            name = re.split(r"[{\[]", name)[0]
            name = full(name)
            pool = known.get(reg)
            if pool is None:
                continue
            if name not in pool:
                problems.append(f"{where}:{n}: unknown {reg} {name}\n      {cmd[:180]}")
    return problems


def main():
    registries = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if registries is None:
        for guess in (ROOT / "tools" / "mcmeta-registries",):
            if guess.exists():
                registries = guess
    van = vanilla(registries) if registries else {}
    if not van:
        print("(no vanilla registries given: only checking modded names)")

    def known_for(src):
        mod = ours(src)
        out = {}
        for reg in set(mod) | set(van):
            v = van.get(reg)
            out[reg] = None if (v is None and reg in van) else (v or set()) | mod.get(reg, set())
            if not van:
                out[reg] = mod.get(reg, set()) | {"minecraft:*"}
        return out

    def run(src):
        known = known_for(src)
        if not van:  # without vanilla data, skip minecraft names
            probs = [p for p in check(src, known) if " minecraft:" not in p.split("\n")[0]]
        else:
            probs = check(src, known)
        return probs

    base = ROOT / "base"
    inherited = {re.sub(r":\d+:", ":", p) for p in (run(base) if base.exists() else [])}
    found = run(ROOT / "src")
    new = [p for p in found if re.sub(r":\d+:", ":", p) not in inherited]
    print(f"{len(found) - len(new)} unknown names inherited from A New Corps (not counted)")
    if new:
        print(f"{len(new)} unknown name(s):")
        for p in new:
            print("  -", p)
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
