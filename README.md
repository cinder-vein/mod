# Lantern Corps (Palladium addon)

The Lantern Corps of the emotional spectrum for **Minecraft Java 1.20.1 (Forge)**, built on
[Palladium](https://www.curseforge.com/minecraft/mc-mods/palladium). Gameplay is inspired by
*A New Corps*. All art and ability files here are original.

## Install

1. Use a Forge **1.20.1** profile (Forge 47.x) with **Palladium 4.x** (+ PalladiumCore).
2. Put `dist/greenlantern-6.0.0-forge-1.20.1.jar` in the `mods` folder. Remove any older version.
3. Optional: **Curios** to wear rings in a ring slot.

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
| Black Lantern | Death | Heart Rip, Death Aura | Blackest Night |

## How it plays

- **Wear a ring** in either hand (or a Curios ring slot). It shows as a small signet plate with the corps
  logo on the front of your right hand.
- **All ring powers work with or without the suit.** A charged ring gives **40 hearts** (Red: 30, but more
  strength) and netherite-level armor.
- **Suit Up** (bottom slot of the first ability page) toggles your suit on and off. Your face stays visible.
- **Suits and masks:** open Palladium's **accessories menu**. Your corps has a *Suit* slot (Corps Armor,
  Classic, Stealth) and a *Mask* slot (Domino Mask, Lens Goggles, Gem Cowl, or **No Mask**). Suits are
  two-layer skins with raised armor; your face always shows.
- **Greed Constructs (Orange):** every mob you defeat while wearing the Orange ring joins your hoard (up to 10).
  *Greed Construct Arrival* summons the hoard as orange hard-light constructs that fight for you for 30 seconds.
  Summoning puts you on the `gl_greed` team so your constructs never target you.
- **Recharge:** **right-click** with your corps' Power Battery in your main hand, or **right-click a placed one**.
  Either fully charges the ring and recites the oath.
- **Constructs are 3D:** fists, hammers, cages and walls of hard light appear in the world in your corps'
  color (Red makes claws, Star Sapphires make crystals), then fade after a few seconds.
- **Red rage** tints your screen red; the **Sinestro Corps** makes its victims hear Parallax.
- **Blue and Green** empower each other within 12 blocks (faster recharge, more damage) once the
  *Hope Amplified* / *Willpower Ignited* upgrade is bought.
- **Skill tree:** open Palladium's powers menu and spend **XP levels** to unlock upgrades:

| Branch | Upgrades (XP levels) |
|---|---|
| Vitality | +10 hearts (5) → +10 more (15) |
| Combat | +4 damage (5) → +4 more (15) |
| Capacity | 1500 charge (5) → 2000 charge (15) |
| Flight | Flight with trail and aura (5) |
| Constructs | Wheel + Blast (5) → Giant Fist (8) → Cage (10) → Hammer Slam (12) → Wall (10) |
| Force Field | Projectile, explosion and fire immunity (5) |
| Corps specials | After Force Field: each special in order (8, 12, 16), then the Ultimate (30) |

Beam, Ring Light, Suit Up and recharging are available from the start.

## Crafting

- **Ring:** corps item on top, then gold / eye of ender / gold, then gold at the bottom.
  Green emerald block, Yellow gold block, Red redstone block, Orange raw gold block, Blue diamond block,
  Violet amethyst block, Indigo lapis block, Black wither skeleton skull.
- **White Lantern Ring:** shapeless: the seven spectrum rings + nether star + totem of undying.
- **Power Battery:** corps glass / corps item / corps glass, then deepslate / lantern / deepslate, then 3 polished deepslate.

## Editing

- `tools/gen_corps.py`: corps table, oaths, the shared kit, the skill tree and each corps' specials.
- `tools/art.py`: logos, suit designs, the worn ring, ring icons and the lantern block model.
- Run `python3 tools/gen_corps.py`, then `python3 tools/build.py`, which validates every cross-reference and builds the jar.
