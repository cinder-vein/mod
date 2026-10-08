"""Hard light: the 3D construct shapes shown by item_display entities, their textures, and the world constructs an
entity's host forms (a giant fist, a construct train, fear spikes, a black hand, a crystal cage).

A construct shape is one hidden item per shape (final_lanterns:construct_<shape>); CustomModelData picks the corps
color (1-9 in common.CORPS order). The datapack grows a new display in and removes it when its time is up.
"""
from PIL import Image

from common import CORPS, NS, TARGETS, burst, sound

CORPS_ORDER = list(CORPS)

def _box(frm, to):
    return {"from": frm, "to": to, "faces": {f: {"texture": "#0", "uv": [0, 0, 16, 16]}
                                             for f in ("north", "south", "east", "west", "up", "down")}}


def construct_shapes():
    """Shape name -> list of elements in a 16x16x16 box, centered on (8, 8, 8). Shapes face -z:
    an item_display turns its item half a turn, so a model's -z side faces the entity's facing
    direction (the fist's knuckles sit at low z for that reason)."""
    fist = [
        _box([3, 3, 5], [13, 11, 13]),     # back of the hand
        _box([3, 11, 4], [5.4, 14, 11]),   # four curled fingers
        _box([5.6, 11, 4], [8, 14.5, 11]),
        _box([8.2, 11, 4], [10.6, 14.5, 11]),
        _box([10.8, 11, 4], [13, 14, 11]),
        _box([3, 9, 2], [13, 11.5, 5]),    # knuckle ridge
        _box([12.5, 5, 6], [15, 10, 11]),  # thumb
        _box([5, 0, 6], [11, 3, 12]),      # wrist
    ]
    hammer = [
        _box([7, 0, 7], [9, 10, 9]),       # handle
        _box([2, 10, 4], [14, 16, 12]),    # head
        _box([1, 11, 5], [2, 15, 11]),     # striking faces
        _box([14, 11, 5], [15, 15, 11]),
    ]
    cage = []
    for x, z in ((1, 1), (14, 1), (1, 14), (14, 14), (7.5, 1), (7.5, 14), (1, 7.5), (14, 7.5)):
        cage.append(_box([x, 0, z], [x + 1, 16, z + 1]))  # bars
    cage += [_box([1, 0, 1], [15, 1, 15]), _box([1, 15, 1], [15, 16, 15])]  # floor and roof frame
    wall = [
        _box([0, 0, 7], [16, 16, 9]),      # slab
        _box([0, 0, 6.5], [16, 1, 9.5]), _box([0, 15, 6.5], [16, 16, 9.5]),  # frame
        _box([0, 0, 6.5], [1, 16, 9.5]), _box([15, 0, 6.5], [16, 16, 9.5]),
        _box([5, 5, 6], [11, 11, 10]),     # boss in the middle
    ]
    claw = [
        _box([7, 0, 7], [9, 8, 9]),        # shaft
        _box([3, 8, 7], [13, 10, 9]),      # crossbar
        _box([3, 10, 7], [5, 15, 9]), _box([3.5, 15, 7.5], [4.5, 16, 8.5]),   # three hooked prongs
        _box([7, 10, 7], [9, 16, 9]),
        _box([11, 10, 7], [13, 15, 9]), _box([11.5, 15, 7.5], [12.5, 16, 8.5]),
    ]
    crystal = [
        _box([6, 0, 6], [10, 14, 10]), _box([7, 14, 7], [9, 16, 9]),          # central spire
        _box([2, 0, 3], [5, 9, 6]), _box([2.8, 9, 3.8], [4.2, 11, 5.2]),        # side shards
        _box([11, 0, 9], [14, 10, 12]), _box([11.8, 10, 9.8], [13.2, 12, 11.2]),
        _box([9, 0, 2], [11, 6, 4]), _box([4, 0, 11], [7, 7, 14]),
    ]
    spike = [_box([5.5, 0, 5.5], [10.5, 6, 10.5]), _box([6.5, 6, 6.5], [9.5, 11, 9.5]),
             _box([7.25, 11, 7.25], [8.75, 15, 8.75]), _box([7.6, 15, 7.6], [8.4, 16, 8.4])]
    hand = [_box([3, 2, 6], [13, 10, 10]),                       # palm, reaching out
            _box([5, -1, 6.5], [11, 2, 9.5]),                    # wrist
            _box([13, 4, 6.5], [15.5, 9, 9.5]), _box([14.5, 9, 6.5], [16, 11, 9.5])]   # thumb
    for x0, x1 in ((3, 5.2), (5.6, 7.8), (8.2, 10.4), (10.8, 13)):  # grasping fingers
        hand += [_box([x0, 10, 6.5], [x1, 15, 9.5]), _box([x0, 15, 9.5], [x1, 16.5, 12.5])]
    # the train (and the grasping hand above) are built facing +z, then mirrored to face -z; the
    # train is lifted 8 units so its wheels sit at the display's feet
    train = [_box([2, 0, -4], [14, 2, 20]),                       # chassis
             _box([3, 2, -4], [13, 12, 4]), _box([2, 12, -5], [14, 13, 5]),    # cab and roof
             _box([4, 2, 4], [12, 10, 18]),                      # boiler
             _box([6.5, 10, 13], [9.5, 15, 16]),                 # smokestack
             _box([3, 0, 18], [13, 3, 21]),                      # cowcatcher
             _box([6, 5, 18], [10, 8, 18.5])]                    # headlamp
    for z in (-2, 6, 14):
        train += [_box([1, -2, z], [2, 2, z + 4]), _box([14, -2, z], [15, 2, z + 4])]  # wheels
    train = [_moved(_mirrored_z(e), dy=8) for e in train]
    hand = [_mirrored_z(e) for e in hand]
    ball = [_box([3, 3, 3], [13, 13, 13]), _box([5, 1, 5], [11, 15, 11]),
            _box([1, 5, 5], [15, 11, 11]), _box([5, 5, 1], [11, 11, 15])]
    shapes = {"fist": fist, "hammer": hammer, "cage": cage, "wall": wall, "claw": claw, "crystal": crystal,
              "spike": spike, "hand": hand, "train": train, "ball": ball}
    for elements in shapes.values():  # hard light glows wherever it is drawn (displays, projectiles)
        for e in elements:
            e["shade"] = False
            e["forge_data"] = {"block_light": 15, "sky_light": 15}
    return shapes


def _mirrored_z(e):
    e = dict(e)
    e["from"], e["to"] = [e["from"][0], e["from"][1], 16 - e["to"][2]], [e["to"][0], e["to"][1], 16 - e["from"][2]]
    return e


def _moved(e, dy):
    e = dict(e)
    e["from"], e["to"] = [e["from"][0], e["from"][1] + dy, e["from"][2]], [e["to"][0], e["to"][1] + dy, e["to"][2]]
    return e



# How big each shape grows and how many ticks it lasts.
SHAPES = {
    "fist": {"name": "Fist", "scale": 2.6, "life": 24},
    "hammer": {"name": "Hammer", "scale": 3.2, "life": 24},
    "cage": {"name": "Cage", "scale": 2.4, "life": 120},
    "wall": {"name": "Wall", "scale": 3.2, "life": 100},
    "claw": {"name": "Claw", "scale": 2.8, "life": 24},
    "crystal": {"name": "Crystal", "scale": 2.6, "life": 160},
    "spike": {"name": "Spike", "scale": 2.2, "life": 40},
    "hand": {"name": "Hand", "scale": 2.8, "life": 30},
    "train": {"name": "Train", "scale": 2.4, "life": 14},
    "ball": {"name": "Cannonball", "scale": 1.0, "life": 1},
}
GROWING = [s for s in SHAPES if s not in ("train", "ball")]  # the train slides instead


def _shade(rgb, f):
    if f >= 1:
        return tuple(int(v + (255 - v) * (f - 1)) for v in rgb[:3])
    return tuple(int(v * f) for v in rgb[:3])


def construct_texture(corps, rgb):
    """Translucent hard light: bright edges, softer middle. Black Lantern constructs are corrupted: near-black with
    pale cracks running through them."""
    img = Image.new("RGBA", (16, 16))
    if corps == "black":
        for y in range(16):
            for x in range(16):
                crack = (x * 3 + y * 5) % 13 == 0 or (x - y) % 11 == 0
                edge = x in (0, 15) or y in (0, 15)
                c = (190, 196, 210) if crack else ((70, 72, 82) if edge else (24, 24, 30))
                img.putpixel((x, y), c + (235 if edge or crack else 205,))
        return img
    if corps == "white":
        main, light, glow = (236, 239, 244), (255, 255, 255), (255, 255, 255)
    else:
        main, light, glow = _shade(rgb, 1.0), _shade(rgb, 1.28), _shade(rgb, 1.4)
    for y in range(16):
        for x in range(16):
            edge = x in (0, 15) or y in (0, 15)
            c = light if edge else (glow if (x + y) % 6 == 0 else main)
            img.putpixel((x, y), c + ((235,) if edge else (170,)))
    return img


def construct_cmds(corps, shape, where, extra_tags=()):
    """Commands that spawn a display construct. `where` is an `execute ...` prefix that sets the position."""
    n = CORPS_ORDER.index(corps) + 1
    tags = ",".join(f'"{t}"' for t in ["gl_construct", "gl_new", f"gl_{shape}", *extra_tags])
    nbt = ('{Tags:[%s],item:{id:"%s:construct_%s",Count:1b,tag:{CustomModelData:%d}},'
           'item_display:"none",brightness:{sky:15,block:15},view_range:2f,'
           'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],'
           'scale:[0.2f,0.2f,0.2f]}}') % (tags, NS, shape, n)
    newest = "@e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest]"
    return [f"{where} run summon minecraft:item_display ~ ~ ~ {nbt}",
            f"{where} run tp {newest} ~ ~ ~ ~ 0"]


def _fx(corps):
    rgb = CORPS[corps]["color"]
    return rgb if corps != "black" else (150, 155, 170)


def world_constructs():
    """{function path: lines} for the world constructs entity hosts form. Run as the host (tagged gl_user)."""
    fn = {}
    front = "execute anchored eyes positioned ^ ^ ^3"
    hit = TARGETS.format(r=2.5) + "]"
    fx = _fx("green")
    fn["host_cx/green/fist"] = [
        *construct_cmds("green", "fist", "execute anchored eyes positioned ^ ^-0.4 ^2.6"),
        f"{front} run {burst(fx, 2.5, '0.8 0.8 0.8', 60, '~ ~ ~')}",
        f"{front} as {hit} run damage @s 12 minecraft:player_attack by @p[tag=gl_user]",
        f"{front} run effect give {hit} minecraft:levitation 1 3 true",
        sound("minecraft:entity.iron_golem.attack", 0.6)]
    train = [*construct_cmds("green", "train", "execute rotated ~ 0 positioned ^ ^0.3 ^1.5", extra_tags=["gl_train_new"]),
             sound("minecraft:entity.minecart.riding", 0.6), sound("minecraft:block.bell.use", 0.5)]
    for d in range(2, 16, 2):
        at = f"execute rotated ~ 0 positioned ^ ^0.5 ^{d}"
        tgt = TARGETS.format(r=2) + "]"
        train += [f"{at} as {tgt} run damage @s 14 minecraft:player_attack by @p[tag=gl_user]",
                  f"{at} run effect give {tgt} minecraft:levitation 1 4 true",
                  f"{at} run {burst(fx, 2.0, '0.6 0.6 0.6', 20, '~ ~ ~')}"]
    fn["host_cx/green/train"] = train
    for corps in ("yellow", "black"):  # a ring of spikes: fear, or the grave
        spikes = []
        for a in range(0, 360, 45):
            spikes += construct_cmds(corps, "spike", f"execute rotated {a} 0 positioned ^ ^ ^3")
        around = TARGETS.format(r=5) + "]"
        fn[f"host_cx/{corps}/spikes"] = spikes + [
            f"execute as {around} run damage @s 10 minecraft:player_attack by @p[tag=gl_user]",
            f"effect give {around} minecraft:slowness 6 2 true",
            f"effect give {around} minecraft:{'darkness' if corps == 'yellow' else 'wither'} 6 0 true",
            f"effect give {around} minecraft:weakness 6 1 true",
            burst(_fx(corps), 2.0, "3 0.5 3", 150, "~ ~0.5 ~"), sound("minecraft:block.pointed_dripstone.land", 0.6),
            sound("minecraft:entity.warden.sonic_charge", 1.4)]
    target = TARGETS.format(r=12) + ",limit=1,sort=nearest]"
    fn["host_cx/black/hand"] = [
        *construct_cmds("black", "hand", f"execute at {target} positioned ~ ~1 ~"),
        f"execute as {target} at @s run particle minecraft:soul ~ ~1 ~ 0.3 0.6 0.3 0.03 40 force",
        f"execute rotated ~ 0 positioned ^ ^ ^1.5 run tp {target} ~ ~ ~",
        f"execute as {target} run damage @s 8 minecraft:magic by @p[tag=gl_user]",
        f"effect give {target} minecraft:wither 6 2 true",
        "effect give @s minecraft:instant_health 1 0 true",
        sound("minecraft:entity.wither.shoot", 0.6)]
    for corps, shape in (("violet", "crystal"), ("black", "cage"), ("indigo", "cage"), ("orange", "hand")):
        cage = [*construct_cmds(corps, shape, f"execute at {target} positioned ~ ~1 ~"),
                f"execute as {target} at @s run {burst(_fx(corps), 2.0, '0.6 1.0 0.6', 120, '~ ~1 ~')}",
                *[f"effect give {target} minecraft:{x} 8 {a} true" for x, a in
                  (("slowness", 255), ("jump_boost", 250), ("mining_fatigue", 4), ("glowing", 0))],
                sound("minecraft:block.amethyst_cluster.place" if corps == "violet" else
                      "minecraft:block.amethyst_block.resonate", 0.8)]
        if shape == "hand":  # Ophidian's grasping hand drags its prey in first
            cage.insert(2, f"execute rotated ~ 0 positioned ^ ^ ^2 run tp {target} ~ ~ ~")
        fn[f"host_cx/{corps}/{shape}"] = cage
    return fn


def tick_lines():
    """Grow new displays in, slide trains, and remove constructs whose time is up (run every tick)."""
    tick = []
    for shape in GROWING:
        cfg = SHAPES[shape]
        sel = f"@e[type=minecraft:item_display,tag=gl_new,tag=gl_{shape}]"
        sc = f"{cfg['scale']}f"
        tick += [f"scoreboard players set {sel} gl_life {cfg['life']}",
                 f"execute as {sel} run data merge entity @s {{start_interpolation:0,interpolation_duration:5,"
                 f"transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],"
                 f"scale:[{sc},{sc},{sc}]}}}}"]
    tick += [
        "scoreboard players set @e[type=minecraft:item_display,tag=gl_train_new] gl_life 14",
        "execute as @e[type=minecraft:item_display,tag=gl_train_new] run data merge entity @s {start_interpolation:0,"
        "interpolation_duration:12,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],"
        "translation:[0f,0f,13f],scale:[2.4f,2.4f,2.4f]}}",
        "tag @e[type=minecraft:item_display,tag=gl_train_new] remove gl_train_new",
        "tag @e[type=minecraft:item_display,tag=gl_new] remove gl_new",
        "scoreboard players remove @e[type=minecraft:item_display,tag=gl_construct] gl_life 1",
        "kill @e[type=minecraft:item_display,tag=gl_construct,scores={gl_life=..0}]",
    ]
    return tick


def item_files(write, save, lang):
    """The hidden construct-shape items, their per-corps models and the hard-light textures."""
    for c, data in CORPS.items():
        save(construct_texture(c, data["color"]), f"assets/{NS}/textures/item/construct/{c}.png")
    glow = Image.new("RGBA", (16, 16), (255, 252, 235, 255))
    save(glow, f"assets/{NS}/textures/item/construct/glow.png")
    items = []
    for shape, elements in construct_shapes().items():
        item = f"construct_{shape}"
        items.append(item)
        write(f"addon/{NS}/items/{item}.json", {"type": "palladium:default", "max_stack_size": 1})
        lang[f"item.{NS}.{item}"] = f"{SHAPES[shape]['name']} Construct"
        write(f"assets/{NS}/models/item/{item}_base.json", {
            "render_type": "minecraft:translucent",
            "textures": {"0": f"{NS}:item/construct/green", "particle": f"{NS}:item/construct/green"},
            "elements": elements})
        write(f"assets/{NS}/models/item/{item}.json", {
            "parent": f"{NS}:item/{item}_base",
            "overrides": [{"predicate": {"custom_model_data": i + 1}, "model": f"{NS}:item/{item}_{c}"}
                          for i, c in enumerate(CORPS_ORDER)]})
        for c in CORPS_ORDER:
            write(f"assets/{NS}/models/item/{item}_{c}.json", {
                "parent": f"{NS}:item/{item}_base",
                "textures": {"0": f"{NS}:item/construct/{c}", "particle": f"{NS}:item/construct/{c}"}})
    return items
