# Lantern Corps (Palladium addon)

The Lantern Corps of the emotional spectrum for **Minecraft Java 1.20.1 (Forge)**, built on
[Palladium](https://www.curseforge.com/minecraft/mc-mods/palladium). Gameplay is inspired by
*A New Corps*, and the construct system by the Green Lantern mod showcase. All art and ability files here are original.

## Install

1. Use a Forge **1.20.1** profile (Forge 47.x) with **Palladium 4.x** (+ PalladiumCore).
2. Put `dist/greenlantern-9.0.0-forge-1.20.1.jar` in the `mods` folder. Remove any older version.
3. Optional:
   - **Curios** gives you two ring slots.
   - **KubeJS** adds the `/lantern` admin command and lets players answer a ring by typing *yes* / *no*.

## The corps

| Corps | Emotion | Specials | Ultimate |
|---|---|---|---|
| Green Lantern | Willpower | Roar | Emerald Nova |
| Sinestro Corps | Fear | Inflict Fear, Nightmare | Fear Incarnate |
| Red Lantern | Rage | Napalm, Rage, Roar | Blood Rage |
| Orange Lantern | Avarice | Avarice (passive), Hoard, Life Drain, Greed Construct Arrival | Consume |
| Blue Lantern | Hope | Aura of Hope, Rekindle | Hope Burns Bright |
| Star Sapphire | Love | Crystal Prison, Love's Embrace, Charm | Love Conquers All |
| Indigo Tribe | Compassion | Phase, Compassion, Healing Touch | Staff of Compassion |
| White Lantern | Life | Life Growth, Aura of Life | Light of the Entity |
| Black Lantern | Death | Heart Rip, Death Aura, Raise the Dead, Undying (passive), Emotional Sight | Blackest Night |

## Rings

- **Wearing a ring:** hold it in either hand, or wear it in a Curios ring slot (best: it keeps your hands free
  for constructs). It shows on your hand like in the showcase: a signet with your corps' logo on the outside of the
  hand, at the base of the fingers, and a band across the front of the index finger. A second ring shows on your left
  hand. **All powers work with or without the suit.**
- **Charge bonus:** a charged ring gives **40 hearts** and netherite-level armor. Red gives 30 hearts, but
  more strength.
- **Ownership:** a ring binds to the first player who holds it, and shows *Bound to &lt;name&gt;* on it.
  - If anyone else holds or wears it, it leaves them and flies back to its bearer, in any dimension.
  - If the bearer is offline it waits where it fell. It never despawns, and only its bearer can pick it up.
  - Ownership follows the player, not their name, so a renamed player keeps their rings.
- **Two rings at once:** wear two rings (both hands, or two Curios ring slots) and you get **Spectrum Fusion**.
  - Every pair of corps has its own fusion. For example *Hope Ignites Will* (Green + Blue) and
    *Life and Death* (White + Black).
  - Each fusion combines both rings' signature effects.
  - Hearts and armor don't stack. Only one suit can be up at a time.
  - Press **X** to switch between the two rings' ability bars.
- **Recharging:**
  - **Right-click** with your corps' Power Battery in your main hand, or **right-click a placed battery**.
    Either way the ring charges fully and you recite the oath.
  - Charge is kept when you take the ring off or log out.
- **Beams** fire from the ring hand. Your arm raises and points where you look.

## The ring chooses you

Every player builds up eight emotions just by playing. Check yours with `/trigger gl_emotions`.

| Emotion | Corps | Grows from |
|---|---|---|
| Willpower | Green | taking and blocking damage |
| Fear | Sinestro | dying, sneaking |
| Rage | Red | dealing damage, killing players |
| Avarice | Orange | trading, opening chests and barrels, mining diamonds, emeralds, gold and ancient debris |
| Hope | Blue | winning raids, sleeping, ringing bells, time played |
| Love | Star Sapphire | breeding animals, eating cake |
| Compassion | Indigo | talking to villagers, potting flowers, filling cauldrons |
| Death | Black | killing mobs, dying |

When an emotion reaches the **threshold (20 000)** while you're in survival, that corps' ring streaks down to you:
*"&lt;Name&gt;, you have great willpower. Welcome to the Green Lantern Corps. Do you accept?"*

- Click **[ACCEPT]** or **[DECLINE]**, or type **yes** / **no** (typing needs KubeJS).
- If you accept, the ring is bound to you, it brings its **Power Battery** with you, and the server announces it.
  If your inventory is full, they drop at your feet.
- If you decline, or wait 60 seconds, the ring flies away and doesn't return for an hour.
- The **White** ring only comes to someone who has reached the threshold in all seven spectrum emotions.

## Corps leaders

An admin appoints leaders (`/lantern leader <player> <corps>`). A leader can revoke the ring of a member of
their own corps, in two ways:
- the **Revoke Ring** ability, which takes the ring of the nearest member within 8 blocks;
- `/trigger gl_roster`, which lists online members with their ids, then `/trigger gl_revoke set <id>`.

The revoked ring goes to the leader, unbound. It won't bind to the leader, so they can hand it to a new recruit.
Leaders can't revoke each other. Revoking also reaches rings worn in Curios slots.

## Admin commands

With KubeJS: `/lantern` (operators only). Without it, run the matching function on the player, e.g.
`execute as Steve run function greenlantern:admin/give/green`.

| Command | What it does |
|---|---|
| `/lantern give <player> <corps>` | give a ring already bound to the player |
| `/lantern unbound <player> <corps>` | give an unbound ring |
| `/lantern battery <player> <corps>` | give a power battery |
| `/lantern emotion <player> <emotion> set\|add <n>` | change an emotion (`scoreboard players set <player> gl_e_<emotion> <n>`) |
| `/lantern offer <player> <corps>` | make that ring choose the player now |
| `/lantern leader\|unleader <player> <corps>` | appoint or remove a corps leader |
| `/lantern remove <player> <corps>` / `removeall <player>` | take rings away (inventory, hands and Curios) |
| `/lantern unbind <player>` | unbind the ring in their main hand (it binds to the next player who holds it) |
| `/lantern reset <player>` / `cooldowns <player>` / `show <player>` | reset emotions, clear decline cooldowns, show emotions |
| `/lantern threshold <n>` | change the threshold (`scoreboard players set #threshold gl_cfg <n>`) |
| `/lantern enable` / `disable` | turn emotions and ring offers on or off |

- **Emotion names:** will, fear, rage, greed, hope, love, compassion, death.
- **Corps names:** green, yellow, red, orange, blue, violet, indigo, white, black.
- **Ring charge:** Palladium's own command sets it, e.g.
  `energybar value set <player> greenlantern:green_lantern ring_charge 1000`.

## Constructs

Constructs work like the Green Lantern mod showcase:

- **Five construct slots.** The second page of the ability bar holds *Construct 1* to *Construct 5*. Each one forms
  whatever construct you put in that slot. Press **X** (Palladium's "switch list" key) to reach the page, and rebind
  the keys in Controls like any Palladium ability.
- **Configure Constructs** (fourth bar page, or `/trigger gl_construct`) opens the *Construct Configuration* menu in
  chat. Click a slot, pick a category tab (Melee, Ranged, Defense, Utility), then click a construct. New players start
  with Sword, Blast, Tower Shield, Construct Blocks and Scan.
- **The Construct Wheel** (first page) lists the whole catalog. Hold its key and pick one with the mouse.
- **Held constructs** are real weapons and tools. They form in your empty hand, or the item in that hand moves to a
  free slot. A ring held in your hand is never moved: the construct goes to your inventory instead. Press the slot again
  to dismiss them. They drain 1 charge a second, and they dissolve when the ring runs dry, when you take the ring off,
  or if they're dropped.
- **Hard light** (Barrier Wall, Dome, Bridge) only fills air and vanishes on its own.

| Category | Construct | Charge | Unlocked by |
|---|---|---|---|
| Melee | Sword | 30 | Constructs |
| Melee | Sword & Shield, Mace, Battle Axe | 40-50 | Melee Constructs I |
| Melee | Giant Fist, Hammer Slam | 100-120 | Melee Constructs II |
| Ranged | Blast | 40 | Constructs |
| Ranged | Gatling (hold right-click; 3 charge a shot), Missile Barrage | 40-120 | Ranged Constructs I |
| Ranged | Cannon | 150 | Ranged Constructs II |
| Defense | Tower Shield | 30 | Constructs |
| Defense | Barrier Wall (15 s), Cage | 100-150 | Defense Constructs I |
| Defense | Dome (15 s) | 200 | Defense Constructs II |
| Utility | Construct Blocks (64 placeable blocks), Scan (health and armor of what you look at) | 10-60 | Constructs |
| Utility | Scuba Gear (breathe, see and swim underwater; toggle), Mining Drill | 20-30 | Utility Constructs I |
| Utility | Bridge (16 blocks, 30 s) | 80 | Utility Constructs II |

Missiles and the Cannon never break blocks.

Every corps also has a **signature construct**, unlocked after all four branches:

| Corps | Signature construct |
|---|---|
| Green | Construct Train: smashes through everything in a line 14 blocks ahead |
| Sinestro | Fear Spikes: a ring of spikes that hurts and terrifies everything within 5 blocks |
| Red | Blood Claws: fast burning claws (Fire Aspect II) |
| Orange | Grasping Hands: drag every hostile mob within 14 blocks to your feet |
| Blue | Sanctuary: a dome that heals and protects every player inside |
| Star Sapphire | Crystal Spear: seals whatever it hits in crystal |
| Indigo | Indigo Staff: long reach, and it heals the players around you |
| White | Radiant Aegis: 12 extra hearts for you and the players around you |
| Black | Black Hand: drags the nearest creature to you and withers it |

## Ring benefits

Passive gifts, with or without the suit. The skill tree lists them next to Suit Up.

- **Every ring (while charged):**
  - 40 hearts and netherite-level armor.
  - No drowning, falling or freezing damage.
  - **Universal Translator:** villagers trade with you as a Hero of the Village.
- **Each corps:**

| Corps | Gift |
|---|---|
| Green | Fearless Will: no blindness, darkness or nausea |
| Sinestro | Terror Aura: hostile mobs within 8 blocks are weakened |
| Red | Burning Blood: immune to fire, lava and poison |
| Orange | Avarice: XP orbs fly to you, plus extra luck for better loot |
| Blue | Hope Springs Eternal: below 10 hearts you keep regenerating |
| Star Sapphire | Love's Bond: you, nearby players and pets regenerate |
| Indigo | Empathic Link: mobs near you are weakened when you're hurt |
| White | Font of Life: constant regeneration, never hungry |
| Black | Undead Body: never hungry, no wither or poison |

## Suits and masks

**Suit Up** is the bottom slot of the first ability page. It toggles your suit on and off.

Open Palladium's **accessories menu** to choose:
- **Suit** slot: *Corps Uniform*, *Shadow* or *Classic*. All three are built from the hand-made template in
  `tools/templates/suit_base.png` and recolored for each corps.
- **Mask** slot: *Corps Mask*, *Domino Mask*, *Lens Goggles*, *Gem Cowl* or *No Mask*. Black also has
  *Deathly Pallor*.

## Skill tree

Open Palladium's powers menu and spend **XP levels**:

| Branch | Upgrades (XP levels) |
|---|---|
| Vitality | +10 hearts (5) → +10 more (15) |
| Combat | +4 damage (5) → +4 more (15) |
| Capacity | 1500 charge (5) → 2000 charge (15) |
| Flight | Flight with trail and aura (5) |
| Constructs | Constructs (5): slots, wheel and basics → one branch each for Melee, Ranged, Defense and Utility: I (8) → II (12) → Signature construct (20, needs all four) |
| Force Field | Projectile, explosion and fire immunity (5) |
| Corps specials | After Force Field: each special in order (8, 12, 16), then the Ultimate (30) |

Beam, Ring Light, Suit Up and recharging are available from the start.

The ability bar has four pages (switch with **X**):
1. Beam, Construct Wheel, Force Field, Ring Light, Suit Up.
2. Construct 1 to 5.
3. Your corps' specials and Ultimate (plus Emotional Sight for Black).
4. Configure Constructs, Spectrum Fusion, and Revoke Ring for leaders.

## Crafting

- **Ring:** the corps item on top, then gold / eye of ender / gold, then gold at the bottom. Corps items:
  - Green: emerald block
  - Yellow: gold block
  - Red: redstone block
  - Orange: raw gold block
  - Blue: diamond block
  - Violet: amethyst block
  - Indigo: lapis block
  - Black: wither skeleton skull
- **White Lantern Ring:** shapeless, from the seven spectrum rings + a nether star + a totem of undying.
- **Power Battery:** corps glass / corps item / corps glass, then deepslate / lantern / deepslate, then three polished deepslate.
  It's a small lantern with a glowing chamber, side lenses and a wire handle. Place it on a block or a pedestal.

## Editing

- `tools/gen_corps.py`: the corps table, oaths, shared kit, skill tree, specials, fusions and the datapack wiring.
- `tools/constructs.py`: the construct catalog, slots, configuration menu and every construct's effect.
- `tools/systems.py`: ownership, emotions, ring offers, leaders, admin functions and the KubeJS script.
- `tools/art.py`: logos, suit recoloring, masks, the worn ring, ring icons, the lantern and construct models.
- **To rebuild:** run `python3 tools/gen_corps.py`, then `python3 tools/build.py`. The build checks every
  cross-reference and builds the jar.
- `python3 tools/lint_commands.py` (needs `pip install mecha`) syntax-checks every command against Minecraft's
  command tree.
