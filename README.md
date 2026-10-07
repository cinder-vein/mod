# Lantern Corps (Palladium addon)

The Lantern Corps of the emotional spectrum for **Minecraft Java 1.20.1 (Forge)**, built on
[Palladium](https://www.curseforge.com/minecraft/mc-mods/palladium). Gameplay is inspired by
*A New Corps*, and the construct system by the Green Lantern mod showcase. All art and ability files here are original.

## Install

1. Use a Forge **1.20.1** profile (Forge 47.x) with **Palladium 4.x** (+ PalladiumCore) and **Curios** (rings are
   worn in its ring slots).
2. Put `dist/greenlantern-10.0.0-forge-1.20.1.jar` in the `mods` folder. Remove any older version.
3. Optional: **KubeJS** adds the `/lantern` admin command, `/ring recall|forge`, `/emotions`, and looser chat wordings
   for calling your ring and speaking your oath. Installed on the client too, it lets you switch ring modes with
   **Ctrl** (otherwise you sneak instead).
   - Palladium loads the KubeJS scripts from the mod jar. If `/ring` or `/lantern` is still an unknown command with
     KubeJS installed, copy the files from this repository's `kubejs/server_scripts` into your game's
     `kubejs/server_scripts` folder (and `kubejs/client_scripts` into `kubejs/client_scripts`), then restart.
     `logs/kubejs/server.log` says *"[Lantern Corps] KubeJS script loaded"* when it works.

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

- **Wearing a ring:** a ring only works worn in a **Curios ring slot** (there are two). Held in a hand or carried, it
  does nothing. It shows on your hand like in the showcase: a signet with your corps' logo on the outside of the
  hand, at the base of the fingers, and a band across the front of the index finger. A second ring shows on your left
  hand. **All powers work with or without the suit.**
- **Charge bonus:** a charged ring gives **40 hearts** and netherite-level armor. Red gives 30 hearts, but
  more strength.
- **Ownership:** a ring binds to the first player who carries it (picks it up, holds it or is given it), and shows
  *Bound to &lt;name&gt;* on it. A ring must be bound to you before you can wear it.
  - If anyone else holds or wears it, it leaves them and flies back to its bearer, in any dimension.
  - If the bearer is offline it waits where it fell. It never despawns, and only its bearer can pick it up.
  - Ownership follows the player, not their name, so a renamed player keeps their rings.
  - You bear one ring per corps. Another ring of a corps you already bear (one you crafted or picked up) won't bind to
    you: you can carry it, but if you hold or wear it, it drops at your feet and waits for another bearer. A lost ring
    is replaced by calling it back.
- **Calling your ring back:** anyone can call the rings that chose them, from anywhere.
  - `/trigger gl_recall` calls every ring you're the bearer of. It works for every player and needs no extra mods.
    `/trigger gl_recall set 11` to `19` calls one ring (11 green, 12 yellow, 13 red, 14 orange, 15 blue, 16 violet,
    17 indigo, 18 white, 19 black).
  - **Say it in chat** (no extra mods needed): *"ring, come to me"*, *"ring, return to me"*, *"come to me, ring"*,
    *"ring, come back"*, *"I summon my ring"* or *"I call my ring"* call every ring. *"green ring, come to me"*,
    *"come to me, blue ring"* or *"return to me, star sapphire ring"* call one. Capitals don't matter; the commas and
    an ending "!" must be as shown.
  - With KubeJS you can also run `/ring recall` or `/ring recall <corps>`, and any chat message with "ring" and a
    calling word works (*"come back blue ring"*). Naming a corps or its emotion calls just that ring.
  - A ring **lying anywhere in a loaded area**, in any dimension, flies back to you. A ring in **your ender chest** comes
    out at your feet.
  - A ring **stored in a chest**, left in an unloaded area or lost can't be reached by commands. Instead a new ring
    forms on you, and the one you left behind **goes dark for good**. It crumbles to dust if anyone wears it, so rings
    never duplicate.
  - There's a 10-second wait between calls. A ring revoked by a leader or removed by an admin can't be called back.
  - A ring bound before 9.0 can be called back once you've worn it since updating.
- **Forging a new ring (for a recruit):** speak your corps' oath while wearing your ring, and your ring forges a new
  one.
  - Type the oath in chat, word for word. It's shown in chat every time you recharge. Capitals and punctuation don't
    matter. With KubeJS, small slips are fine too.
  - Or use `/trigger gl_forge` (with KubeJS also `/ring forge [corps]`). Both recite the oath for you.
  - It costs **500 charge**, and the ring needs **5 minutes** to rest before forging again.
  - The new ring is **unbound** and remembers who forged it. It never binds to you, so it can't replace or darken your
    own ring. You can carry it; drop it (Q) for your recruit. It binds to the next player who carries it.
  - Admins: `/lantern forging on|off` and `/lantern forgecooldown <seconds>`.
- **Two rings at once** merge into the **Spectrum Bond**, with its own bar and skill tree (see below).
- **Recharging:**
  - **Right-click** with your corps' Power Battery in your main hand, or **right-click a placed battery**.
    Either way the ring charges fully and you recite the oath.
  - A ring doesn't recharge on its own until you buy **Passive Recharge** in its skill tree (see Skill tree).
  - Charge is kept when you take the ring off or log out.
- **Beams** fire from the ring hand. Your arm raises and points where you look.
- **Beam mode and blast mode:** hold **Ctrl** and press the first ability key (default **V**). The first slot turns
  into *Switch Mode* while Ctrl is held.
  - **Beam mode** (the default): Beam and the Construct Wheel.
  - **Blast mode:** **Energy Blast** (a bolt of hard light, 40 charge) and **Scan** (the health and armor of what
    you look at, up to 24 blocks; it glows for 10 seconds; 10 charge).
  - Ctrl needs KubeJS installed on your client and the server. Without it, sneak and press the first ability key.

## The ring chooses you

Every player builds up eight emotions just by playing.

**The Emotional Spectrum menu** shows them. Open it by saying *"emotions"* in chat, with `/trigger gl_emotions`, with
`/emotions` (KubeJS), or with the *Emotional Spectrum* button on the last page of a ring's bar. It's a clickable chat
menu:
- **Main page:** each emotion's bar, its percentage of the threshold (the ring comes at 100%), its level (one per 10%)
  and the amount itself.
- **Click an emotion** for its page:
  - **What raised it:** every action that feeds it, with the points it has earned you so far and how much each gives.
  - **Its quests:** three per emotion, done in order. They track themselves; finishing one gives its reward and starts
    the next.

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

| Emotion | Quests (reward: 1 500 → 3 000 → 6 000) |
|---|---|
| Willpower | Block 25 hearts of damage with a shield → take 150 hearts of damage → defeat the Ender Dragon |
| Fear | Sneak for 10 minutes → defeat 10 phantoms → defeat the Warden |
| Rage | Deal 200 hearts of damage → defeat 150 mobs → defeat 3 ravagers |
| Avarice | Trade 30 times → mine 24 diamond ore → mine 12 ancient debris |
| Hope | Sleep in a bed 7 times → ring a bell 25 times → win 2 raids |
| Love | Breed 20 animals → eat 14 slices of cake → breed 100 animals |
| Compassion | Talk to villagers 40 times → pot 12 flowers → brew at a brewing stand 25 times |
| Death | Defeat 100 mobs → defeat 40 zombies or skeletons → defeat the Wither |

When an emotion reaches the **threshold (20 000)** while you're in survival, that corps' ring streaks down to you:
*"&lt;Name&gt;, you have great willpower. Welcome to the Green Lantern Corps. Do you accept?"*

- Click **[ACCEPT]** or **[DECLINE]**, or type **yes** / **no** in chat.
- If you accept, the ring is bound to you, it brings its **Power Battery** with you, and the server announces it.
  If your inventory is full, they drop at your feet.
- If you decline, or wait 60 seconds, the ring flies away and doesn't return for an hour.
- The **White** ring only comes to someone who has reached the threshold in all seven spectrum emotions.

## Corps leaders

An admin appoints leaders (`/lantern leader <player> <corps>`). A leader can revoke the ring of a member of
their own corps, in two ways:
- the **Revoke Ring** ability, which takes the ring of the nearest member within 8 blocks;
- `/trigger gl_roster`, which lists online members with their ids, then `/trigger gl_revoke set <id>`.

The revoked ring goes to the leader, unbound. It won't bind to the leader, so they can drop it for a new recruit.
Anyone who isn't a valid bearer of that corps (a revoked member, or after `/lantern unbind`) can't wield an unbound
ring they handed on: it drops at their feet.
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
| `/lantern unbind <player>` | unbind the ring in their main hand (it binds to the next player who carries it) |
| `/lantern reset <player>` / `cooldowns <player>` / `show <player>` | reset emotions, clear decline cooldowns, show emotions |
| `/lantern threshold <n>` | change the threshold (`scoreboard players set #threshold gl_cfg <n>`) |
| `/lantern enable` / `disable` | turn emotions and ring offers on or off |
| `/lantern forging on\|off`, `/lantern forgecooldown <seconds>` | allow forging rings by oath; time between forgings (default 300) |

- **Emotion names:** will, fear, rage, greed, hope, love, compassion, death.
- **Corps names:** green, yellow, red, orange, blue, violet, indigo, white, black.
- **Ring charge:** Palladium's own command sets it, e.g.
  `energybar value set <player> greenlantern:green_lantern ring_charge 1000`.

## Constructs

Constructs work like the Green Lantern mod showcase:

- **The Construct Wheel** (second slot of the first page) holds every construct. Hold its key and pick one with the
  mouse. Constructs you haven't unlocked are greyed out.
- **Held constructs** are real weapons and tools. They form in your empty hand, or the item in that hand moves to a
  free slot. If there's no room, nothing forms and no charge is spent.
  - Pick them on the wheel again to dismiss them.
  - Each one (and Scuba Gear) costs its ring 3 charge a second.
  - They dissolve when that ring runs dry, when you wear no ring at all, or when they're dropped.
  - Weapons and tools wear out like netherite gear; form a fresh one when they break.
- **Hard light** (Barrier Wall, Dome, Bridge) only fills air and vanishes on its own. While it lasts it can't be
  broken or pushed by pistons.

| Category | Construct | Charge | Unlocked by |
|---|---|---|---|
| Melee | Sword | 30 | Constructs |
| Melee | Sword & Shield, Mace, Battle Axe | 40-50 | Melee Constructs I |
| Melee | Giant Fist, Hammer Slam | 100-120 | Melee Constructs II |
| Ranged | Gatling (hold right-click; 3 charge a shot), Missile Barrage | 40-120 | Ranged Constructs I |
| Ranged | Cannon | 150 | Ranged Constructs II |
| Defense | Tower Shield | 30 | Constructs |
| Defense | Barrier Wall (15 s), Cage | 100-150 | Defense Constructs I |
| Defense | Dome (15 s) | 200 | Defense Constructs II |
| Utility | Construct Blocks (64 placeable blocks) | 60 | Constructs |
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

Passive gifts, with or without the suit. The skill tree lists them on either side of its root.

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
- While you wear two rings, the **Spectrum Suit** and **Spectrum Mask** slots hold merged suits in both rings'
  colors. "First ring" means the one on your right hand, "second" the one on your left:
  - **Split Light:** your right side in the first ring's colors, your left side in the second's.
  - **Fusion Uniform:** the first ring's panels, with the second ring's gloves, emblem and under-suit.
  - **Fusion Uniform (Reversed):** the same, colors swapped.
  - **Twin Halves:** the first ring's colors above the belt, the second's below.
  - **Spectrum Shadow:** *Split Light* on a pitch-black under-suit.
  - Masks: *Split Mask*, *Twin Domino*, *Twin Lens Goggles*, *Twin Gem Cowl* or *No Mask*.

## Skill tree

Open Palladium's powers menu and spend **XP levels**:

| Branch | Upgrades (XP levels) |
|---|---|
| Vitality | +10 hearts (5) → +10 more (15) |
| Combat | +4 damage (5) → +4 more (15) |
| Capacity | 1500 charge (5) → 2000 charge (15) |
| Passive Recharge | I: 2 charge a second (60) → II: 4 (60) → III: 8 (60) → IV: 16 (60). Each tier replaces the last |
| Flight | Flight with trail and aura (5) |
| Constructs | Constructs (5): the wheel and the basics → one branch each for Melee, Ranged, Defense and Utility: I (8) → II (12) → Signature construct (20, needs all four) |
| Force Field | Projectile, explosion and fire immunity (5) |
| Corps specials | After Force Field: each special in order (8, 12, 16), then the Ultimate (30) |

Beam, Energy Blast, Scan, Ring Light, Suit Up and recharging at a battery are available from the start.

The ability bar's pages (switch with **X**):
1. Beam / Energy Blast, Construct Wheel / Scan, Force Field, Ring Light, Suit Up.
2. Your corps' specials and Ultimate (plus Emotional Sight for Black).
3. Emotional Spectrum (opens the emotions menu), and Revoke Ring for leaders.

Every ability slot has its own icon in the corps' colors.

## Two rings: the Spectrum Bond

Wear two rings (in your two Curios ring slots) and they bond. The first ring in this order is your **first
ring** (right hand): green, yellow, red, orange, blue, violet, indigo, white, black. The other is your **second
ring** (left hand). With three rings, the first two in that order bond.

- **One merged bar** replaces both rings' first page; each ring keeps its own specials page.
  - **Spectrum Beam:** a beam from each hand, each in its ring's color. Each ring pays for its own beam.
  - **Twin Blast** in blast mode: one bolt from each hand (20 charge from each ring). **Scan** costs 5 from each.
  - **Construct Wheel:** every construct either ring has unlocked. It forms from your first ring if that ring has
    it, otherwise from your second, in that ring's color and at its cost. The wheel also has your **Signature
    Construct** (and, with *Twin Signatures*, your second ring's).
  - **Force Field:** needs Force Field in either ring; it drains both rings.
  - **Ring Light** and **Suit Up**: Suit Up wears your merged suit (see Suits and masks).
  - Page 2: **Spectrum Fusion** and **Spectrum Overload** once you've bought them.
- **Spectrum Charge:** the bond's bar shows both rings' charge added together. Each ring still has its own charge.
- **Its own skill tree** (powers menu, *Spectrum Bond*), bought with XP levels. It's kept when you take a ring off:

| Branch | Upgrades (XP levels) |
|---|---|
| Harmony | Shared Light: charge flows from the fuller ring to the emptier one (5) → Twin Batteries: recharging either ring at its battery fills both (10) → Resonance: both rings regain 2 extra charge a second (15) |
| Body | Dual Vitality: +10 hearts (8) → Twin Strength: +3 attack and punch damage (12) → Spectrum Flight: fly 50% faster (12) |
| Fusion | Spectrum Fusion (8) → Fusion Mastery: every 15 s instead of 30, and cheaper (15) → Spectrum Overload, the ultimate (30) |
| Twin Constructs | Twin Constructs: constructs cost a quarter less (8) → Prismatic Shield: the force field also gives Resistance II (12) → Twin Signatures: your second ring's signature construct on the wheel (15) |

- **Spectrum Fusion** costs 125 charge from each ring. Every pair of corps has its own fusion, combining both rings'
  signature effects, for example *Hope Ignites Will* (Green + Blue) or *Life and Death* (White + Black).
- **Spectrum Overload** costs 400 from each ring, once a minute. It hits everything within 12 blocks for heavy damage
  and throws it into the air, and gives you Strength II, Resistance II and Speed II for 15 seconds.
- Hearts and armor from the rings themselves don't stack.

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

- `tools/gen_corps.py`: the corps table, oaths, shared kit, skill tree, specials, the Spectrum Bond power, fusions and
  the datapack wiring.
- `tools/constructs.py`: the construct catalog, every construct's effect, and Energy Blast and Scan.
- `tools/spectrum.py`: the Spectrum Bond's datapack side (bonding, merged constructs, fusions, Harmony skills), ring
  modes, and the KubeJS scripts for the Ctrl key.
- `tools/icons.py` and `tools/icon_glyphs/`: the ability icons, drawn as 32x32 pixel-art maps and recolored per corps.
  `python3 tools/icons.py preview.png` renders them all.
- `tools/systems.py`: ownership, emotions, ring offers, leaders, admin functions, the chat phrases and the KubeJS script.
- `tools/emotions.py`: the Emotional Spectrum menu, the tracking of what raised each emotion, and the quests.
- `tools/art.py`: logos, suit recoloring, masks, merged suits, the worn ring, ring icons, the lantern and construct
  models.
- **To rebuild:** run `python3 tools/gen_corps.py`, then `python3 tools/build.py`. The build checks every
  cross-reference and builds the jar.
- `python3 tools/lint_commands.py` (needs `pip install mecha`) syntax-checks every command against Minecraft's
  command tree.
