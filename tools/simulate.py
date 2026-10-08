"""A small simulator for the Final Lanterns datapack: runs the real generated functions in src/ tick by tick.

    python3 tools/simulate.py           # runs every scenario, prints what happened, exits 1 if one fails

It interprets the commands our functions use (scoreboards, tags, selectors, execute, function, summon, tp, kill,
tellraw/title) the way Minecraft 1.20.1 does, and treats the rest (particles, sounds, effects, items, Palladium's and
Curios' commands) as succeeding without effect, recording the ones a scenario wants to see. It doesn't load A New
Corps' own tick functions. It's a development check for the datapack's logic (does a ring offer happen when an emotion
reaches the threshold, does an entity come to a worthy player), not a replacement for testing in the game.
"""
import json
import math
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
NS = "final_lanterns"
EYES = 1.62
CURIOS_PATH = 'ForgeCaps."curios:inventory".Curios[{Identifier:"lantern_rings"}].StacksHandler.Stacks'
RING_CORPS = {f"{NS}:{item}": c for c, item in (
    ("green", "greenlanternring"), ("yellow", "yellowlanternring"), ("red", "redlanternring"),
    ("orange", "orangelanternring"), ("blue", "bluelanternring"), ("violet", "pinklanternring"),
    ("indigo", "indigolanternring"), ("white", "whitelanternring"), ("black", "blacklanternring"))}


class Entity:
    _n = 0

    def __init__(self, etype, pos, name=None, tags=(), gamemode="survival", dim="minecraft:overworld"):
        Entity._n += 1
        self.uuid = f"00000000-0000-0000-0000-{Entity._n:012d}"
        self.type, self.name, self.tags = etype, name, set(tags)
        self.pos, self.rot, self.dim, self.gamemode = list(pos), [0.0, 0.0], dim, gamemode
        self.alive, self.powers, self.vehicle, self.passengers, self.sneaking = True, set(), None, [], False
        self.health = 20.0
        self.rings = []  # lantern ring items worn in the Curios slot (ids), for players
        self.ring_slots = 2

    @property
    def is_player(self):
        return self.type == "minecraft:player"

    @property
    def holder(self):
        return self.name if self.is_player else self.uuid

    def __repr__(self):
        return self.name or f"{self.type}{sorted(self.tags)}"


def split(text):
    """Splits a command at top-level spaces (keeping [...], {...} and quoted strings together)."""
    out, cur, depth, quote, esc = [], "", 0, None, False
    for ch in text:
        if quote:
            cur += ch
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == quote:
                quote = None
            continue
        if ch in "\"'" and (cur == "" or depth > 0 or cur[-1] in "=:,[{"):
            quote = ch
            cur += ch
        elif ch in "[{":
            depth += 1
            cur += ch
        elif ch in "]}":
            depth -= 1
            cur += ch
        elif ch == " " and depth == 0:
            if cur:
                out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur:
        out.append(cur)
    return out


def in_range(value, rng):
    if ".." in rng:
        lo, hi = rng.split("..")
        return (lo == "" or value >= float(lo)) and (hi == "" or value <= float(hi))
    return value == float(rng)


def texts(component):
    """The visible text of a JSON text component (scores shown as <obj>)."""
    if isinstance(component, str):
        return component
    if isinstance(component, list):
        return "".join(texts(c) for c in component)
    if isinstance(component, dict):
        t = component.get("text", "")
        if "score" in component:
            t = f"<{component['score']['objective']}>"
        if "selector" in component:
            t = component["selector"]
        return t + "".join(texts(c) for c in component.get("extra", []))
    return ""


class Ctx:
    def __init__(self, sim, executor=None, pos=(0, 0, 0), rot=(0, 0), dim="minecraft:overworld", anchor="feet"):
        self.sim, self.executor, self.pos, self.rot, self.dim, self.anchor = sim, executor, list(pos), list(rot), dim, anchor

    def copy(self, **kw):
        c = Ctx(self.sim, self.executor, self.pos, self.rot, self.dim, self.anchor)
        for k, v in kw.items():
            setattr(c, k, v)
        return c


class Sim:
    def __init__(self, src=SRC, seed=1):
        self.src = src
        self.rng = random.Random(seed)
        self.functions = {}
        for path in (src / "data").glob("*/functions/**/*.mcfunction"):
            ns = path.relative_to(src / "data").parts[0]
            fid = f"{ns}:" + path.relative_to(src / "data" / ns / "functions").as_posix()[:-len(".mcfunction")]
            self.functions[fid] = [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines()
                                   if ln.strip() and not ln.strip().startswith("#")]
        self.objectives, self.scores = set(), {}
        self.entities, self.log, self.tick_no, self.unhandled = [], [], 0, {}
        self.calls = {}  # function id -> times called
        self.depth = 0

    # --- world -----------------------------------------------------------------------------------
    def add_player(self, name, pos=(0, 70, 0), gamemode="survival"):
        e = Entity("minecraft:player", pos, name=name, gamemode=gamemode)
        self.entities.append(e)
        return e

    def player(self, name):
        return next(e for e in self.entities if e.name == name)

    def score(self, holder, obj):
        return self.scores.get(obj, {}).get(holder)

    def set_score(self, holder, obj, value):
        if obj not in self.objectives:
            raise CommandError(f"unknown objective {obj}")
        self.scores.setdefault(obj, {})[holder] = int(value)

    def tag_values(self, tag_id, kind="functions"):
        ns, _, path = tag_id.partition(":")
        out = []
        for f in self.src.glob(f"data/{ns}/tags/{kind}/{path}.json"):
            for v in json.loads(f.read_text())["values"]:
                v = v["id"] if isinstance(v, dict) else v
                out += self.tag_values(v[1:], kind) if v.startswith("#") else [v]
        return out

    # --- running ---------------------------------------------------------------------------------
    def run_function(self, fid, ctx):
        self.calls[fid] = self.calls.get(fid, 0) + 1
        if fid not in self.functions:
            self.unhandled[f"missing function {fid}"] = self.unhandled.get(f"missing function {fid}", 0) + 1
            return 0
        self.depth += 1
        if self.depth > 200:
            raise RuntimeError(f"function recursion too deep at {fid}")
        for line in self.functions[fid]:
            self.execute(line, ctx)
        self.depth -= 1
        return 1

    def execute(self, line, ctx):
        try:
            return self.cmd(split(line), ctx)
        except CommandError:
            return 0

    def palladium(self):
        """What Palladium does each tick that the datapack reads: a worn ring's power runs its marker (fl_marker),
        and the Emotional Spectrum power (given by `superpower add`) runs its own."""
        for e in self.entities:
            if not e.is_player:
                continue
            for item in e.rings:
                c = RING_CORPS.get(item)
                if c and f"gl_t_{c}" in self.objectives:
                    e.tags.add(f"gl_{c}")
                    self.set_score(e.holder, f"gl_t_{c}", 3)
            if f"{NS}:emotional_spectrum" in e.powers and "gl_spirit" in self.objectives:
                self.set_score(e.holder, "gl_spirit", 3)

    def tick(self, n=1, only_ours=True):
        for _ in range(n):
            self.tick_no += 1
            self.palladium()
            for fid in self.tag_values("minecraft:tick"):
                if only_ours and not fid.startswith(f"{NS}:fl/"):
                    continue
                self.run_function(fid, Ctx(self, pos=(0, 0, 0)))
            self.entities = [e for e in self.entities if e.alive]

    def load(self):
        for fid in self.tag_values("minecraft:load"):
            if fid.startswith(f"{NS}:fl/"):
                self.run_function(fid, Ctx(self))

    # --- selectors -------------------------------------------------------------------------------
    def select(self, token, ctx):
        if not token.startswith("@"):
            if re.fullmatch(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", token):
                return [e for e in self.entities if e.uuid == token and e.alive]
            return [e for e in self.entities if e.name == token and e.alive]
        kind = token[:2]
        arglist = []
        if len(token) > 2:
            body = token[3:-1]
            for part in split_args(body):
                k, _, v = part.partition("=")
                arglist.append((k, v))
        if kind == "@s":
            cands = [ctx.executor] if ctx.executor is not None and ctx.executor.alive else []
        elif kind in ("@a", "@p", "@r"):
            cands = [e for e in self.entities if e.is_player and e.alive]
        else:
            cands = [e for e in self.entities if e.alive]
        limit, sort = None, None
        for k, v in arglist:
            if k == "limit":
                limit = int(v)
                continue
            if k == "sort":
                sort = v
                continue
            cands = [e for e in cands if self.match(e, k, v, ctx)]
        if kind == "@p":
            sort, limit = sort or "nearest", limit or 1
        if kind == "@r":
            sort, limit = "random", limit or 1
        if sort == "nearest":
            cands.sort(key=lambda e: dist(e.pos, ctx.pos))
        elif sort == "random":
            self.rng.shuffle(cands)
        return cands[:limit] if limit else cands

    def match(self, e, k, v, ctx):
        neg = v.startswith("!")
        val = v[1:] if neg else v
        if k == "tag":
            r = (val in e.tags) if val else (not e.tags)
        elif k == "type":
            if val.startswith("#"):
                r = e.type in self.tag_values(val[1:], "entity_types")
            else:
                r = e.type == (val if ":" in val else "minecraft:" + val)
        elif k == "scores":
            r = True
            for part in split_args(val[1:-1]):
                obj, _, rng = part.partition("=")
                s = self.score(e.holder, obj)
                if s is None or not in_range(s, rng):
                    r = False
            return r
        elif k == "distance":
            r = e.dim == ctx.dim and in_range(dist(e.pos, ctx.pos), val)
            return r
        elif k == "gamemode":
            r = e.is_player and e.gamemode == val
        elif k == "predicate":
            r = self.predicate(val, e, ctx)
        elif k in ("nbt", "x", "y", "z", "dx", "dy", "dz", "advancements", "name", "team", "level"):
            self.unhandled[f"selector {k}"] = self.unhandled.get(f"selector {k}", 0) + 1
            r = False
        else:
            raise CommandError(f"unknown selector option {k}")
        return r != neg

    def predicate(self, pid, e, ctx):
        ns, _, path = pid.partition(":")
        f = self.src / f"data/{ns}/predicates/{path}.json"
        if not f.exists():
            self.unhandled[f"missing predicate {pid}"] = 1
            return False
        return self.condition(json.loads(f.read_text()), e)

    def condition(self, c, e):
        if isinstance(c, list):
            return all(self.condition(x, e) for x in c)
        t = c["condition"].removeprefix("minecraft:")
        if t == "random_chance":
            return self.rng.random() < c["chance"]
        if t == "inverted":
            return not self.condition(c["term"], e)
        if t in ("alternative", "any_of"):
            return any(self.condition(x, e) for x in c["terms"])
        if t == "entity_properties":
            p = c.get("predicate", {})
            if "flags" in p:
                return p["flags"].get("is_sneaking") == e.sneaking
            return False  # equipment and the like: nobody holds anything here
        if t == "location_check":
            p = c["predicate"]
            if "dimension" in p and p["dimension"] != e.dim:
                return False
            y = p.get("position", {}).get("y", {})
            return ("min" not in y or e.pos[1] >= y["min"]) and ("max" not in y or e.pos[1] <= y["max"])
        self.unhandled[f"loot condition {t}"] = 1
        return False

    # --- coordinates -----------------------------------------------------------------------------
    def coords(self, toks, ctx):
        if toks[0].startswith("^"):
            left, up, fwd = (float(t[1:] or 0) for t in toks)
            yaw, pitch = map(math.radians, ctx.rot)
            origin = list(ctx.pos)
            if ctx.anchor == "eyes" and ctx.executor is not None:
                origin[1] += EYES if ctx.executor.is_player else 0.5
            fx, fy, fz = -math.sin(yaw) * math.cos(pitch), -math.sin(pitch), math.cos(yaw) * math.cos(pitch)
            ux, uy, uz = -math.sin(yaw) * -math.sin(pitch), math.cos(pitch), math.cos(yaw) * -math.sin(pitch)
            lx, lz = math.cos(yaw), math.sin(yaw)
            return [origin[0] + fx * fwd + ux * up + lx * left, origin[1] + fy * fwd + uy * up,
                    origin[2] + fz * fwd + uz * up + lz * left]
        out = []
        for i, t in enumerate(toks):
            out.append(ctx.pos[i] + float(t[1:] or 0) if t.startswith("~") else float(t))
        return out

    # --- commands --------------------------------------------------------------------------------
    def cmd(self, t, ctx):
        head = t[0]
        if head == "execute":
            return self.execute_chain(t[1:], ctx)
        if head == "function":
            fid = t[1]
            if fid.startswith("#"):
                for f in self.tag_values(fid[1:]):
                    self.run_function(f, ctx)
                return 1
            return self.run_function(fid, ctx)
        if head == "scoreboard":
            return self.scoreboard(t[1:], ctx)
        if head == "tag":
            targets = self.select(t[1], ctx)
            for e in targets:
                (e.tags.add if t[2] == "add" else e.tags.discard)(t[3])
            return len(targets)
        if head in ("tellraw", "title"):
            for e in self.select(t[1], ctx):
                if head == "title" and t[2] == "times":
                    continue
                raw = " ".join(t[3:] if head == "title" else t[2:])
                try:
                    msg = texts(json.loads(raw))
                except json.JSONDecodeError:
                    msg = raw
                self.log.append((self.tick_no, e.name or repr(e), head if head == "tellraw" else t[2], msg))
            return 1
        if head == "summon":
            pos = self.coords(t[2:5], ctx) if len(t) >= 5 else list(ctx.pos)
            nbt = " ".join(t[5:])
            e = Entity(t[1], pos, tags=re.findall(r'"([^"]+)"', (re.search(r"Tags:\[([^\]]*)\]", nbt) or [None, ""])[1]),
                       dim=ctx.dim)
            self.entities.append(e)
            pm = re.search(r"Passengers:\[\{id:\"([^\"]+)\",Tags:\[([^\]]*)\]", nbt)
            if pm:
                p = Entity(pm[1], pos, tags=re.findall(r'"([^"]+)"', pm[2]), dim=ctx.dim)
                p.vehicle = e
                e.passengers.append(p)
                self.entities.append(p)
            self.log.append((self.tick_no, "world", "summon", f"{t[1]} {sorted(e.tags)} at "
                                                              f"{[round(v, 1) for v in pos]}"))
            return 1
        if head == "tp":
            targets = self.select(t[1], ctx)
            if len(t) == 3:
                dest = self.select(t[2], ctx)
                if not dest:
                    return 0
                pos, rot = list(dest[0].pos), list(dest[0].rot)
            else:
                pos = self.coords(t[2:5], ctx)
                rot = list(targets[0].rot) if targets else [0, 0]
                if len(t) >= 7:
                    rot = [ctx.rot[0] + float(t[5][1:] or 0) if t[5].startswith("~") else float(t[5]),
                           ctx.rot[1] + float(t[6][1:] or 0) if t[6].startswith("~") else float(t[6])]
            for e in targets:
                e.pos, e.rot = list(pos), list(rot)
                for p in e.passengers:  # passengers ride along
                    p.pos = list(pos)
            return len(targets)
        if head == "kill":
            targets = self.select(t[1], ctx)
            for e in targets:
                e.alive = False
            return len(targets)
        if head == "superpower":
            for e in self.select(t[3], ctx):
                (e.powers.add if t[1] == "add" else e.powers.discard)(t[2])
            return 1
        if head == "loot":
            self.log.append((self.tick_no, getattr(ctx.executor, "name", None), "loot", " ".join(t[1:])))
            return 1
        if head == "give":
            for e in self.select(t[1], ctx):
                self.log.append((self.tick_no, e.name, "give", t[2]))
            return 1
        if head == "data" and t[1] == "get":
            targets = self.select(t[3], ctx) if t[2] == "entity" else []
            if targets and len(t) > 4 and t[4] == "Health":
                return int(targets[0].health)
            if targets and len(t) > 4 and t[4].startswith(CURIOS_PATH) and t[4].endswith(".Size"):
                if not targets[0].ring_slots:
                    raise CommandError("no Lantern Ring slot")
                return targets[0].ring_slots
            return 0
        if head == "data" and t[1] == "merge" and t[2] == "entity":
            m = re.search(r"Health:([0-9.]+)f?", t[4]) if len(t) > 4 else None
            for e in self.select(t[3], ctx) if m else []:
                e.health = float(m[1])
            return 1
        if head == "clear":
            return 0
        if head in ("particle", "playsound", "effect", "item", "data", "attribute", "bossbar", "damage", "advancement",
                    "energybar", "curios", "team", "spreadplayers", "fill", "setblock"):
            return 1
        self.unhandled[f"command {head}"] = self.unhandled.get(f"command {head}", 0) + 1
        return 1

    def scoreboard(self, t, ctx):
        if t[0] == "objectives":
            if t[1] == "add":
                self.objectives.add(t[2])
            return 1
        verb = t[1]
        if verb == "operation":
            a_holders = self.holders(t[2], ctx)
            b_holders = self.holders(t[5], ctx)
            if not b_holders:
                raise CommandError("no source")
            b = self.score(b_holders[0], t[6])
            if b is None:
                raise CommandError("source has no score")
            for h in a_holders:
                a = self.score(h, t[3])
                op = t[4]
                if op == "=":
                    a = b
                elif a is None:
                    raise CommandError("no score")
                elif op == "+=":
                    a += b
                elif op == "-=":
                    a -= b
                elif op == "*=":
                    a *= b
                elif op == "/=":
                    a = a // b if b else a
                elif op == "%=":
                    a = a % b if b else a
                elif op == "<":
                    a = min(a, b)
                elif op == ">":
                    a = max(a, b)
                self.set_score(h, t[3], a)
            return len(a_holders)
        holders = self.holders(t[2], ctx)
        if verb in ("set", "add", "remove"):
            for h in holders:
                cur = self.score(h, t[3]) or 0
                n = int(t[4])
                self.set_score(h, t[3], n if verb == "set" else cur + n if verb == "add" else cur - n)
            return len(holders)
        if verb == "get":
            s = self.score(holders[0], t[3]) if holders else None
            if s is None:
                raise CommandError("no score")
            return s
        if verb == "reset":
            for h in holders:
                if len(t) > 3:
                    self.scores.get(t[3], {}).pop(h, None)
            return 1
        if verb == "enable":
            return 1
        self.unhandled[f"scoreboard {verb}"] = 1
        return 1

    def holders(self, token, ctx):
        if token.startswith("#"):
            return [token]
        return [e.holder for e in self.select(token, ctx)]

    def execute_chain(self, t, ctx):
        i = 0
        ctxs = [ctx]
        store = None
        while i < len(t):
            sub = t[i]
            if sub == "run":
                total = 0
                for c in ctxs:
                    r = self.cmd(t[i + 1:], c)
                    if store:
                        self.store(store, r, c)
                    total += r or 0
                return total
            if sub in ("as", "at"):
                new = []
                for c in ctxs:
                    for e in self.select(t[i + 1], c):
                        new.append(c.copy(executor=e) if sub == "as" else c.copy(pos=list(e.pos), rot=list(e.rot),
                                                                                    dim=e.dim))
                ctxs, i = new, i + 2
            elif sub == "positioned":
                if t[i + 1] == "as":
                    ctxs = [c.copy(pos=list(e.pos)) for c in ctxs for e in self.select(t[i + 2], c)]
                    i += 3
                else:
                    ctxs = [c.copy(pos=self.coords(t[i + 1:i + 4], c), anchor="feet") for c in ctxs]
                    i += 4
            elif sub == "rotated":
                if t[i + 1] == "as":
                    ctxs = [c.copy(rot=list(e.rot)) for c in ctxs for e in self.select(t[i + 2], c)]
                    i += 3
                else:
                    ctxs = [c.copy(rot=[c.rot[0] + float(t[i + 1][1:] or 0) if t[i + 1].startswith("~") else float(t[i + 1]),
                                        c.rot[1] + float(t[i + 2][1:] or 0) if t[i + 2].startswith("~") else float(t[i + 2])])
                            for c in ctxs]
                    i += 3
            elif sub == "anchored":
                ctxs = [c.copy(anchor=t[i + 1]) for c in ctxs]
                i += 2
            elif sub == "facing":
                new = []
                for c in ctxs:
                    if t[i + 1] == "entity":
                        targets = self.select(t[i + 2], c)
                        if not targets:
                            continue
                        tp = list(targets[0].pos)
                        if t[i + 3] == "eyes":
                            tp[1] += EYES if targets[0].is_player else 0
                    else:
                        tp = self.coords(t[i + 1:i + 4], c)
                    new.append(c.copy(rot=look(c.pos, tp)))
                ctxs = new
                i += 4
            elif sub == "align":
                ctxs = [c.copy(pos=[math.floor(v) for v in c.pos]) for c in ctxs]
                i += 2
            elif sub == "in":
                ctxs = [c.copy(dim=t[i + 1]) for c in ctxs]
                i += 2
            elif sub == "on":
                new = []
                for c in ctxs:
                    e = c.executor
                    rel = (e.passengers if t[i + 1] == "passengers" else [e.vehicle] if e and e.vehicle else []) if e else []
                    new += [c.copy(executor=x) for x in rel if x and x.alive]
                ctxs, i = new, i + 2
            elif sub in ("if", "unless"):
                want = sub == "if"
                kind = t[i + 1]
                if kind == "score":
                    if t[i + 4] == "matches":  # if score <holder> <objective> matches <range>
                        ctxs = [c for c in ctxs if self.test_score(t[i + 2], t[i + 3], t[i + 5], c) == want]
                        i += 6
                    else:                      # if score <holder> <objective> <op> <holder> <objective>
                        ctxs = [c for c in ctxs if self.test_cmp(t[i + 2:i + 7], c) == want]
                        i += 7
                elif kind == "entity":
                    ctxs = [c for c in ctxs if bool(self.select(t[i + 2], c)) == want]
                    i += 3
                elif kind == "predicate":
                    ctxs = [c for c in ctxs if (c.executor is not None and self.predicate(t[i + 2], c.executor, c)) == want]
                    i += 3
                elif kind == "block":
                    ctxs = [c for c in ctxs if want]  # every block is air here
                    i += 5
                elif kind == "data":
                    if t[i + 2] == "entity" and t[i + 4].startswith(CURIOS_PATH):
                        m = re.search(r'Items\[\{id:"([^"]+)"\}\]$', t[i + 4])
                        ctxs = [c for c in ctxs if any(bool(m) and m[1] in e.rings
                                                       for e in self.select(t[i + 3], c)) == want]
                    else:
                        ctxs = [c for c in ctxs if not want]
                    i += 5 if t[i + 2] in ("entity", "storage", "block") else 4
                else:
                    raise CommandError(f"unknown execute if {kind}")
            elif sub == "store":
                store = (t[i + 1], t[i + 2], t[i + 3], t[i + 4])  # result|success, score, holder, objective
                if t[i + 2] != "score":
                    store = None
                    i += 6 if t[i + 2] in ("entity", "block") else 5
                    if t[i - 1] in ("int", "double", "float", "byte", "short", "long"):
                        i += 1
                    continue
                i += 5
            else:
                raise CommandError(f"unknown execute subcommand {sub}")
            if not ctxs:
                return 0
        return len(ctxs)  # a bare condition

    def store(self, store, result, ctx):
        kind, _, holder, obj = store
        value = (1 if result else 0) if kind == "success" else (result or 0)
        for h in self.holders(holder, ctx):
            self.set_score(h, obj, value)

    def test_score(self, holder, obj, rng, ctx):
        hs = self.holders(holder, ctx)
        s = self.score(hs[0], obj) if hs else None
        return s is not None and in_range(s, rng)

    def test_cmp(self, t, ctx):
        a_h, a_o, op, b_h, b_o = t
        ah, bh = self.holders(a_h, ctx), self.holders(b_h, ctx)
        a = self.score(ah[0], a_o) if ah else None
        b = self.score(bh[0], b_o) if bh else None
        if a is None or b is None:
            return False
        return {"=": a == b, "<": a < b, "<=": a <= b, ">": a > b, ">=": a >= b}[op]


class CommandError(Exception):
    pass


def split_args(body):
    out, cur, depth = [], "", 0
    for ch in body:
        if ch in "{[":
            depth += 1
        elif ch in "}]":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur:
        out.append(cur)
    return out


def dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def look(src, dst):
    dx, dy, dz = (d - s for s, d in zip(src, dst))
    yaw = math.degrees(math.atan2(-dx, dz))
    pitch = math.degrees(-math.atan2(dy, math.sqrt(dx * dx + dz * dz)))
    return [yaw, pitch]


# --- scenarios ------------------------------------------------------------------------------------

def said(sim, who, needle, since=0):
    return [m for m in sim.log if m[0] >= since and m[1] == who and needle in m[3]]


def scenario_join():
    sim = Sim()
    steve = sim.add_player("Steve")
    sim.load()
    sim.tick(5)
    values = {e: sim.score("Steve", f"gl_e_{e}") for e in ("will", "fear", "rage", "greed", "hope", "love",
                                                            "compassion", "death")}
    ok = "gl_rolled" in steve.tags and all(v is not None and 10000 <= v <= 15000 for v in values.values())
    return ok, f"rolled emotions: {values}"


def scenario_offer(gamemode):
    sim = Sim()
    steve = sim.add_player("Steve", gamemode=gamemode)
    sim.load()
    sim.tick(30)
    for e in ("will", "fear", "rage", "greed", "hope", "love", "compassion"):
        sim.set_score("Steve", f"gl_e_{e}", 12000)
    t0 = sim.tick_no
    sim.set_score("Steve", "gl_e_will", 20000)
    sim.tick(25)
    offered = "gl_offer_green" in steve.tags and said(sim, "Steve", "Green Lantern ring streaks down", t0)
    if not offered:
        return False, f"[{gamemode}] no green ring offer within 25 ticks of willpower 20000 (tags {sorted(steve.tags)})"
    sim.set_score("Steve", "gl_accept", 1)
    sim.tick(2)
    joined = "gl_member_green" in steve.tags and said(sim, "Steve", "has been chosen by the Green Lantern Corps", t0)
    return bool(joined), f"[{gamemode}] offer at willpower 20000, then accepted: member={joined and True}"


def scenario_black():
    sim = Sim()
    steve = sim.add_player("Steve")
    sim.load()
    sim.tick(30)
    for e in ("will", "fear", "rage", "greed", "hope", "love", "compassion"):
        sim.set_score("Steve", f"gl_e_{e}", 14000)
    for e in ("will", "fear", "rage", "greed"):
        sim.set_score("Steve", f"gl_e_{e}", 10000)
    sim.tick(25)
    return "gl_offer_black" in steve.tags, "Black ring offer with four emotions at 10 000"


def scenario_quiet_join():
    """Nobody is hunted or challenged the day they join: no entity comes in the first minute."""
    sim = Sim(seed=7)
    for n in range(6):
        sim.add_player(f"P{n}", pos=(n * 50, 70, 0))
    sim.load()
    sim.tick(60 * 20)
    came = {k: sim.score(f"#state_{k}", "gl_ent") for k in ("ion", "parallax", "butcher", "ophidian", "adara",
                                                             "predator", "proselyte", "life", "nekron")}
    return all(v == 0 for v in came.values()), f"six new players, one minute: entity states {came}"


def scenario_entity(key, emotion, value=20000, wait=12 * 20):
    sim = Sim()
    steve = sim.add_player("Steve", pos=(0, 70, 0))
    steve.rot = [0, 0]
    sim.load()
    sim.tick(30)
    sim.set_score("Steve", f"gl_e_{emotion}", value)
    sim.set_score("Steve", "gl_offer", 0)
    for c in ("green", "yellow", "red", "orange", "blue", "violet", "indigo", "white", "black"):
        sim.set_score("Steve", f"gl_cd_{c}", 99999)  # keep ring offers out of the way
    t0 = sim.tick_no
    sim.tick(wait)
    came = sim.score(f"#state_{key}", "gl_ent")
    bodies = [e for e in sim.entities if f"gl_ent_{key}" in e.tags]
    if came not in (1, 2):
        return False, f"{key}: didn't come within {wait // 20} s (state {came})"
    near = min((dist(b.pos, steve.pos) for b in bodies), default=None)
    offered = said(sim, "Steve", "offers to make you its host", t0)
    hosted = "gl_host_" + key in steve.tags
    others = sorted(t for t in steve.tags if t.startswith("gl_host_") and t != f"gl_host_{key}")
    return (bool(offered) or hosted) and not others, (
        f"{key}: came (state {came}), nearest body {near and round(near, 1)} blocks, offered={bool(offered)}, "
        f"hosted={hosted}" + (f", but also hosts {others}" if others else ""))


def scenario_boss(key, emotion):
    """A boss comes for someone at 90%; worn down to 15%, it takes them (95%) as its host."""
    sim = Sim()
    steve = sim.add_player("Steve", pos=(0, 70, 0))
    sim.load()
    sim.tick(30)
    sim.set_score("Steve", f"gl_e_{emotion}", 19500)
    for c in ("green", "yellow", "red", "orange", "blue", "violet", "indigo", "white", "black"):
        sim.set_score("Steve", f"gl_cd_{c}", 99999)
    sim.tick(12 * 20)
    bodies = [e for e in sim.entities if f"gl_ent_{key}" in e.tags and e.alive]
    if not bodies:
        return False, f"{key}: the boss didn't come within 12 s"
    bodies[0].health = 10.0
    sim.tick(5)
    return f"gl_host_{key}" in steve.tags, f"{key}: boss came, worn down, host={f'gl_host_{key}' in steve.tags}"


def scenario_bond():
    """Two rings worn: the Spectrum Bond forms (its power, the actionbar); one taken off: it fades."""
    sim = Sim()
    steve = sim.add_player("Steve")
    sim.load()
    sim.tick(30)
    steve.rings = [f"{NS}:greenlanternring", f"{NS}:yellowlanternring"]
    t0 = sim.tick_no
    sim.tick(25)
    bonded = "gl_dual" in steve.tags and f"{NS}:spectrum_bond" in steve.powers and said(sim, "Steve", "Willpower", t0)
    steve.rings = [f"{NS}:greenlanternring"]
    sim.tick(25)
    faded = "gl_dual" not in steve.tags and f"{NS}:spectrum_bond" not in steve.powers
    return bool(bonded) and faded, f"Spectrum Bond with green + yellow: bonded={bool(bonded)}, faded after one={faded}"


def scenario_check():
    """/trigger gl_check (any player) runs the check: everything running, two slots, both rings on, the bond."""
    sim = Sim()
    steve = sim.add_player("Steve")
    sim.load()
    sim.tick(60)
    sim.set_score("#kubejs", "gl_cfg", 1)  # what the KubeJS script does when a player logs in
    steve.rings = [f"{NS}:greenlanternring", f"{NS}:yellowlanternring"]
    sim.tick(5)
    t0 = sim.tick_no
    sim.set_score("Steve", "gl_check", 1)  # what /trigger gl_check does once the datapack has enabled it
    sim.tick(1)
    want = ["Final Lanterns check", "The datapack is running.", "Chat phrases work", "Lantern Ring slots: ",
            "Green Lantern ring: worn, its power is on.", "Sinestro Corps ring: worn, its power is on.",
            "Spectrum Bond: on", "willpower ", "Ion: free: comes to the first player whose willpower reaches"]
    missing = [w for w in want if not said(sim, "Steve", w, t0)]
    wrong = [m[3][:60] for m in said(sim, "Steve", "✘", t0)]
    reset = sim.score("Steve", "gl_check") == 0
    return not missing and not wrong and reset, (
        f"/trigger gl_check: {len(said(sim, 'Steve', '', t0))} lines" + (f", missing {missing}" if missing else "")
        + (f", unexpected problems {wrong}" if wrong else "") + ("" if reset else ", trigger not reset"))


def scenario_check_broken():
    """When a main function failed to load, the check still answers and names it; one slot is reported."""
    sim = Sim()
    del sim.functions[f"{NS}:second"]
    steve = sim.add_player("Steve")
    steve.ring_slots = 1
    sim.load()
    sim.tick(60)
    t0 = sim.tick_no
    sim.set_score("Steve", "gl_check", 1)
    sim.tick(1)
    named = said(sim, "Steve", "once-a-second function isn't running", t0)
    slot = said(sim, "Steve", "only one Lantern Ring slot", t0)
    return bool(named and slot), f"check with second missing and one ring slot: names second={bool(named)}, " \
                                 f"reports one slot={bool(slot)}"


def main():
    results = [scenario_bond(), scenario_check(), scenario_check_broken(), scenario_join(), scenario_offer("survival"), scenario_offer("creative"), scenario_black(),
               scenario_quiet_join(), scenario_entity("ion", "will"), scenario_entity("adara", "hope"),
               scenario_entity("proselyte", "compassion"),
               scenario_entity("parallax", "fear", value=17000, wait=30 * 20),
               scenario_entity("predator", "love", value=17000, wait=30 * 20),
               scenario_boss("butcher", "rage"), scenario_boss("nekron", "death")]
    sim = Sim()
    sim.add_player("Steve")
    sim.load()
    sim.tick(400)
    failed = 0
    for ok, msg in results:
        print(("PASS " if ok else "FAIL ") + msg)
        failed += not ok
    if sim.unhandled:
        print("not simulated:", ", ".join(f"{k} x{v}" for k, v in sorted(sim.unhandled.items())))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
