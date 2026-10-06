# Lantern Corps (Palladium addon)

The Lantern Corps of the emotional spectrum for **Minecraft Java 1.20.1 (Forge)**, built on
[Palladium](https://www.curseforge.com/minecraft/mc-mods/palladium). Gameplay is inspired by
*A New Corps*. All art and ability files here are original.

## Install

1. Use a Forge **1.20.1** profile (Forge 47.x) with **Palladium 4.x** (+ PalladiumCore).
2. Put `dist/greenlantern-2.0.0-forge-1.20.1.jar` in the `mods` folder.
3. Optional: **Curios** to wear rings in a ring slot.

## The corps

| Corps | Emotion | Special abilities | Ultimate |
|---|---|---|---|
| Green Lantern | Willpower | Roar | Emerald Nova |
| Sinestro Corps (yellow) | Fear | Inflict Fear, Nightmare | Fear Incarnate |
| Red Lantern | Rage | Napalm (fire beam), Rage (Strength + Speed), Roar | Blood Rage |
| Orange Lantern | Avarice | Avarice (fast mining), Hoard (pull items), Life Drain | Consume |
| Blue Lantern | Hope | Aura of Hope (team regen), Rekindle (team heal) | Hope Burns Bright |
| Indigo Tribe | Compassion | Phase (teleport), Compassion, Healing Touch | Staff of Compassion |
| Star Sapphire (violet) | Love | Crystal Prison, Love's Embrace, Charm | Love Conquers All |
| White Lantern | Life | Life Growth (crouch), Aura of Life | Light of the Entity |

**Every ring also has:** Suit Up (uniform + suit-up burst), flight with a colored trail and aura,
a beam, a **construct wheel** (Blast, Giant Fist, Cage, Hammer Slam), Force Field, Ring Light,
Recharge with oath, and passive armor, punch damage and protection from drowning, falling and freezing.

## How to play

- Hold a ring in **either hand** (or a Curios ring slot). Open Palladium's powers menu to see the abilities and keys.
- **Suit Up** first. The ring's powers only work while suited up.
- The bar is your **ring charge**. It refills slowly. To refill fast, hold your corps' **Power Battery**
  in your main hand (ring in the offhand or a ring slot) and hold **Recharge**. You'll recite the corps' oath.
- **Constructs:** hold the Constructs key to open the wheel and pick one.

## Crafting

- **Ring:** corps block on top, then gold / eye of ender / gold, then gold at the bottom.
  Blocks: Green emerald, Yellow gold, Red redstone, Orange raw gold, Blue diamond, Indigo lapis, Violet amethyst.
- **Power Battery:** gold / corps block / gold, corps glass / lantern / corps glass, 3 iron.
- **White Lantern Ring:** shapeless: all seven corps rings + nether star + totem of undying.

## Editing

The corps are generated from one table:

- `tools/gen_corps.py`: corps colors, oaths, emblems, the shared kit and each corps' special abilities.
  Run `python3 tools/gen_corps.py` after editing.
- `tools/build.py`: validates every cross-reference and builds the jar into `dist/`.
