"""Shared tables and helpers for the Final Lanterns generators.

Final Lanterns is based on A New Corps: its rings, powers, suits, models and icons come from base/ (see
import_anc.py). Our systems (emotions, ring offers and binding, recall, the emotional spectrum entities and their
hosts) are generated on top of it, in the same final_lanterns namespace.
"""
import json

NS = "final_lanterns"
SPECTRUM = ["green", "yellow", "red", "orange", "blue", "violet", "indigo"]

# The nine corps our systems know, mapped onto A New Corps' rings, powers, energy bars and lantern batteries.
# ring/power are ids in the final_lanterns namespace; battery is a full item id (the batteries are KubeJS blocks);
# beam is the ANC beam ability copied into the matching entity host's power; forge is the ANC ring-forging function.
CORPS = {
    "green": {"name": "Green Lantern", "title": "Green Lantern Corps", "emotion": "Willpower", "color": (46, 200, 70),
              "ring": "greenlanternring", "power": "greenlantern", "bar": "will_power",
              "battery": "kubejs:greenlanternbattery", "battery_model": f"{NS}:block/greenlanternbattery",
              "beam": "willpowerbeam", "forge": "greenlanternconstruction",
              "oath": ["In brightest day, in blackest night,", "No evil shall escape my sight.",
                       "Let those who worship evil's might,", "Beware my power... Green Lantern's light!"]},
    "yellow": {"name": "Sinestro Corps", "title": "Sinestro Corps", "emotion": "Fear", "color": (245, 205, 30),
               "ring": "yellowlanternring", "power": "yellowlantern", "bar": "fear",
               "battery": "kubejs:yellowlanternbattery", "battery_model": f"{NS}:block/yellowlanternbattery",
               "beam": "fearbeam", "forge": "yellowlanternconstruction",
               "oath": ["In blackest day, in brightest night,", "Beware your fears made into light.",
                        "Let those who try to stop what's right,", "Burn like my power... Sinestro's might!"]},
    "red": {"name": "Red Lantern", "title": "Red Lantern Corps", "emotion": "Rage", "color": (220, 30, 35),
            "ring": "redlanternring", "power": "redlantern", "bar": "rage",
            "battery": "kubejs:redlanternbattery", "battery_model": f"{NS}:block/redlanternbattery",
            "beam": "bloodvomit", "forge": "redlanternconstruction",
            "oath": ["With blood and rage of crimson red,", "Ripped from a corpse so freshly dead,",
                     "Together with our hellish hate,", "We'll burn you all... that is your fate!"]},
    "orange": {"name": "Orange Lantern", "title": "Orange Lanterns", "emotion": "Avarice", "color": (250, 130, 20),
               "ring": "orangelanternring", "power": "orangelantern", "bar": "greed",
               "battery": "kubejs:orangelanternbattery", "battery_model": f"{NS}:block/orangelanternbattery",
               "beam": "greedbeam", "forge": "orangelanternconstruction",  # added by gen_final.py
               "oath": ["What's mine is mine,", "and mine,", "and mine...", "and mine! And not yours!"]},
    "blue": {"name": "Blue Lantern", "title": "Blue Lantern Corps", "emotion": "Hope", "color": (40, 130, 255),
             "ring": "bluelanternring", "power": "bluelantern", "bar": "hope",
             "battery": "kubejs:bluelanternbattery", "battery_model": f"{NS}:block/bluelanternbattery",
             "beam": "hopebeam", "forge": "bluelanternconstruction",
             "oath": ["In fearful day, in raging night,", "With strong hearts full, our souls ignite,",
                      "When all seems lost in the War of Light,", "Look to the stars... for hope burns bright!"]},
    "violet": {"name": "Star Sapphire", "title": "Star Sapphires", "emotion": "Love", "color": (215, 55, 220),
               "ring": "pinklanternring", "power": "pinklantern", "bar": "love",
               "battery": "kubejs:pinklanternbattery", "battery_model": f"{NS}:block/pinklanternbattery",
               "beam": "lovebeam", "forge": "pinklanternconstruction",
               "oath": ["For hearts long lost and full of fright,", "For those alone in blackest night,",
                        "Accept our ring and join our fight,", "Love conquers all... with violet light!"]},
    "indigo": {"name": "Indigo Tribe", "title": "Indigo Tribe", "emotion": "Compassion", "color": (105, 60, 230),
               "ring": "indigolanternring", "power": "indigolantern", "bar": "compassion",
               "battery": f"{NS}:indigostaff", "battery_model": f"{NS}:item/indigostaff",
               "beam": "beam", "forge": "indigolanternconstruction",
               "oath": ["Tor lowar lan, Abin Sur,", "Ak wo tauva, Ihla wo nauva,",
                        "Natromo faan, Dur ak naja,", "Ono ot vauva, Abin Sur."]},
    "white": {"name": "White Lantern", "title": "White Lantern Corps", "emotion": "Life", "color": (235, 242, 250),
              "ring": "whitelanternring", "power": "whitelantern", "bar": "life",
              "battery": "kubejs:whitelanternbattery", "battery_model": f"{NS}:block/whitelanternbattery",
              "beam": "beam", "forge": "whitelanternconstruction",
              "oath": ["From the light of creation,", "every color of the spectrum,", "all life, as one,",
                       "...shines White!"]},
    "black": {"name": "Black Lantern", "title": "Black Lantern Corps", "emotion": "Death", "color": (95, 98, 110),
              "ring": "blacklanternring", "power": "blacklantern", "bar": "death",
              "battery": "kubejs:blacklanternbattery", "battery_model": f"{NS}:block/blacklanternbattery",
              "beam": "deathbeam", "forge": "blacklanternconstruction",
              "oath": ["The Blackest Night falls from the skies,", "The darkness grows as all light dies,",
                       "We crave your hearts and your demise,", "By my black hand, the dead shall rise!"]},
}


def ring_item(c):
    return f"{NS}:{CORPS[c]['ring']}"


def ring_power(c):
    return f"{NS}:{CORPS[c]['power']}"


def hexcolor(rgb):
    return "#%02X%02X%02X" % tuple(rgb[:3])


def text_color(c):
    """Chat color for a corps (Black Lantern grey, so it reads on the dark chat background)."""
    return hexcolor(CORPS[c]["color"] if c != "black" else (170, 175, 190))


def dust(rgb, size=1.0):
    return "%.2f %.2f %.2f %.1f" % (rgb[0] / 255, rgb[1] / 255, rgb[2] / 255, size)


def burst(rgb, size=2.0, spread="1 1 1", count=80, at="~ ~1 ~"):
    return f"particle minecraft:dust {dust(rgb, size)} {at} {spread} 0 {count} force"


def sound(snd, pitch=1.0):
    return f"playsound {snd} player @a[distance=..24] ~ ~ ~ 1 {pitch}"


def tellraw(target, parts):
    return f"tellraw {target} " + json.dumps(parts, separators=(",", ":"))


def actionbar(parts):
    return "title @s actionbar " + json.dumps(parts, separators=(",", ":"))


# Nekron's risen dead (and a boss's minions) are never targets of their own side
OWN_ARMY = "tag=!gl_dead_minion"
# creatures near a point (not items, frames, paintings, boats, minecarts or projectiles), never the user (tagged
# gl_user while an ability runs) or their own army
TARGETS = f"@e[type=!#{NS}:not_creatures,tag=!gl_user,{OWN_ARMY},distance=..{{r}}"
HOSTILE = f"@e[type=#{NS}:hostile_prey,{OWN_ARMY},distance=..{{r}}]"
NOT_CREATURES = [f"minecraft:{t}" for t in (
    "area_effect_cloud", "armor_stand", "arrow", "block_display", "boat", "chest_boat", "chest_minecart",
    "command_block_minecart", "dragon_fireball", "egg", "end_crystal", "ender_pearl", "evoker_fangs",
    "experience_bottle", "experience_orb", "eye_of_ender", "falling_block", "fireball", "firework_rocket",
    "fishing_bobber", "furnace_minecart", "glow_item_frame", "hopper_minecart", "interaction", "item", "item_display",
    "item_frame", "leash_knot", "lightning_bolt", "llama_spit", "marker", "minecart", "painting", "potion",
    "shulker_bullet", "small_fireball", "snowball", "spawner_minecart", "spectral_arrow", "text_display", "tnt",
    "tnt_minecart", "trident", "wither_skull")] + ["palladium:custom_projectile"]
HOSTILE_PREY = [f"minecraft:{m}" for m in (
    "zombie", "husk", "drowned", "skeleton", "stray", "spider", "cave_spider", "creeper", "witch", "slime",
    "magma_cube", "phantom", "silverfish", "endermite", "pillager", "vindicator", "evoker", "ravager", "blaze",
    "ghast", "hoglin", "piglin_brute", "zoglin", "wither_skeleton", "guardian", "shulker", "vex", "enderman")]
