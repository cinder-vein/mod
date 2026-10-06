# Lantern Corps (Palladium addon)

The Lantern Corps of the emotional spectrum for **Minecraft Java 1.20.1 (Forge)**, built on
[Palladium](https://www.curseforge.com/minecraft/mc-mods/palladium). Gameplay is inspired by
*A New Corps*. All art and ability files here are original.

## Install

1. Use a Forge **1.20.1** profile (Forge 47.x) with **Palladium 4.x** (+ PalladiumCore).
2. Put `dist/greenlantern-3.0.0-forge-1.20.1.jar` in the `mods` folder. Remove any older version.
3. Optional: **Curios** to wear rings in a ring slot.

## The corps

| Corps | Emotion | Specials | Ultimate |
|---|---|---|---|
| Green Lantern | Willpower | Roar | Emerald Nova |
| Sinestro Corps | Fear | Inflict Fear, Nightmare | Fear Incarnate |
| Red Lantern | Rage | Napalm, Rage, Roar | Blood Rage |
| Orange Lantern | Avarice | Avarice (passive), Hoard, Life Drain | Consume |
| Blue Lantern | Hope | Aura of Hope, Rekindle | Hope Burns Bright |
| Star Sapphire | Love | Crystal Prison, Love's Embrace, Charm | Love Conquers All |
| Indigo Tribe | Compassion | Phase, Compassion, Healing Touch | Staff of Compassion |
| White Lantern | Life | Life Growth, Aura of Life | Light of the Entity |
| Black Lantern | Death | Heart Rip, Death Aura | Blackest Night |

## How it plays

- **Wear a ring** in either hand (or a Curios ring slot). It shows on your right hand.
- **A charged ring** gives you **40 hearts** and netherite-level armor (20 armor, 12 toughness, knockback resistance).
- **Suit Up** (bottom slot of the first ability page) toggles a full-body uniform on and off. Most powers need it.
- **Recharge:** hold your corps' **Power Battery** in your main hand and press Recharge to **fully** charge the ring.
  Batteries are also placeable lantern blocks.
- **Skill tree:** open Palladium's powers menu and spend **XP levels** to unlock upgrades:

| Branch | Upgrades (XP levels) |
|---|---|
| Vitality | 50 hearts (5) → 60 hearts (15) |
| Combat | +4 damage (5) → +4 more (15) |
| Capacity | 1500 charge (5) → 2000 charge (15) |
| Flight | Flight with trail and aura (5) |
| Constructs | Wheel + Blast (5) → Giant Fist (8) → Cage (10); Hammer Slam (12) |
| Force Field | Projectile, explosion and fire immunity (5) |
| Corps specials | Each special in order (8, 12, 16), then the Ultimate (30, also needs Combat II) |

Beam, Ring Light and Recharge are available from the start.

## Crafting

- **Ring:** corps item on top, then gold / eye of ender / gold, then gold at the bottom.
  Green emerald block, Yellow gold block, Red redstone block, Orange raw gold block, Blue diamond block,
  Violet amethyst block, Indigo lapis block, Black wither skeleton skull.
- **White Lantern Ring:** shapeless: the seven spectrum rings + nether star + totem of undying.
- **Power Battery:** corps glass / corps item / corps glass, then deepslate / lantern / deepslate, then 3 polished deepslate.

## Editing

- `tools/gen_corps.py`: corps table, oaths, the shared kit, the skill tree and each corps' specials.
- `tools/art.py`: logos, uniforms, rings, the lantern block model.
- Run `python3 tools/gen_corps.py`, then `python3 tools/build.py`, which validates every cross-reference and builds the jar.
