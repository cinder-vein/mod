# Green Lantern (Palladium addon)

A Green Lantern mod for **Minecraft Java 1.20.1 (Forge)**, built on the
[Palladium](https://www.curseforge.com/minecraft/mc-mods/palladium) superpower framework.

> In brightest day, in blackest night, no evil shall escape my sight!

## Install

1. Install Forge for 1.20.1 and **Palladium 4.x** (plus its dependency PalladiumCore).
2. Download `dist/greenlantern-1.0.0-forge-1.20.1.jar` and put it in your `mods` folder
   (in the CurseForge app: your profile → `...` → *Open Folder* → `mods`).
3. Optional: install **Curios** to wear the ring in a ring slot.

## How to play

| Item | Recipe |
|---|---|
| **Green Lantern Power Ring** | emerald block (top), gold / eye of ender / gold (middle), gold (bottom) |
| **Power Battery** | gold, emerald block, gold / lime glass, lantern, lime glass / 3 iron ingots |

- Hold the ring in **either hand** (or wear it in a Curios ring slot) to get the Green Lantern power.
- Use Palladium's ability keys to activate powers (open the powers menu to see them).
- **Lantern Uniform** (toggle) puts on the uniform. Every other power needs it switched on.
- Powers use **Willpower** (the green bar). It refills slowly by itself. To refill it fast, hold the
  **Power Battery** in your main hand (with the ring in your offhand or a ring slot) and hold **Recharge**. You'll recite the oath.

| Ability | Type | Cost |
|---|---|---|
| Lantern Uniform | toggle | – |
| Flight (heroic flight) | passive while suited | slow drain while flying |
| Willpower Beam | hold | 3 / tick |
| Construct Blast | press | 40 |
| Construct: Giant Fist | press | 100 |
| Construct: Cage | press | 150 |
| Force Field (immune to projectiles, explosions, fire) | toggle | 2 / tick |
| Ring Light (night vision) | toggle | – |
| Recharge | hold, needs Power Battery | refills 10 / tick |
| Passive: hard-light armor, stronger punches, no drowning/fall/freeze damage | while suited | – |

## Editing

Everything is plain JSON and PNG under `src/`. The mod contains no Java code.

- `src/data/greenlantern/palladium/powers/green_lantern.json`: all abilities, costs and cooldowns
- `src/addon/greenlantern/items/`: items
- `src/assets/greenlantern/`: textures, language, beam/suit visuals
- `tools/make_textures.py`: regenerates the placeholder textures (`python3 tools/make_textures.py`)
- `tools/build.py`: validates all cross-references and builds the jar into `dist/` (`python3 tools/build.py`)
