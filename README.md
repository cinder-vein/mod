# Final Lanterns

The Lantern Corps of the emotional spectrum, and the entities behind it, for **Minecraft Java 1.20.1 (Forge)**,
built on [Palladium](https://www.curseforge.com/minecraft/mc-mods/palladium). Based on *A New Corps*.

## Install

Use a Forge **1.20.1** profile (Forge 47.x) with these mods:

- **Palladium 4.x** (with PalladiumCore and Architectury)
- **GeckoLib**
- **GraveCore 1.2.1+**
- **Curios**: rings are worn in the *Lantern Ring* slot
- **KubeJS** (with Rhino)

Then put `dist/final_lanterns-1.1.0-forge-1.20.1.jar` in the `mods` folder. Remove the old *Lantern Corps*
(`greenlantern-*.jar`) and *A New Corps* jars: Final Lanterns replaces both.

**Coming from Lantern Corps 10:** delete `lantern_commands.js` and `lantern_keys.js` from your game's
`kubejs/server_scripts` and `kubejs/client_scripts` folders. Those old copies call the old `greenlantern` functions,
so `/lantern` and `/ring` silently do nothing while they're there.

**Check it works:** say ***lantern check*** in chat (or `/function final_lanterns:check`). It says whether the
datapack is running, whether the KubeJS commands are loaded, and for each corps how close you are to its ring (or why it
won't come yet).

Palladium loads the mod's KubeJS script (`/lantern`, `/ring`, `/emotions`) from the jar. If the check says it isn't
loaded, copy `kubejs/server_scripts/lantern_commands.js` from this repository into your game's `kubejs/server_scripts`
folder and restart. Everything also works without it: through chat, `/trigger`, and `/function` for admins (see Admin
commands).

## The rings

The rings, their powers, skill trees, suits, masks, capes, constructs, beams, lanterns and icons are A New Corps':
Willpower (green), Fear (yellow), Rage (red), Avarice (orange), Hope (blue), Love (pink), Compassion (indigo),
Life (white) and Death (black), plus Righteousness (gold), Sorrow, Pride, Mischief, Balance, the Djinn, Corrupted Fate
and Starheart rings.

- **Wear a ring in the Lantern Ring slot** (Curios) for its power. Choose its suit, mask and cape in the accessories
  menu.
- **Recharge** at its lantern: right-click the lantern (placed, or held in your hand) to speak the oath.
- The nine spectrum rings' bars have an **Emotional Spectrum** button (see below).
- The Lantern Ring slot holds **two rings**: see *Two rings: the Spectrum Bond*.

Final Lanterns adds these to the nine spectrum rings:

- **Ownership:** a ring binds to the first player who carries it (picks it up, holds it or is given it), and shows
  *Bound to &lt;name&gt;* on it. A ring must be bound to you before you can wear it.
  - If anyone else holds or wears it, it leaves them and flies back to its bearer, in any dimension.
  - If the bearer is offline it waits where it fell. It never despawns, and only its bearer can pick it up.
  - Ownership follows the player, not their name, so a renamed player keeps their rings.
  - You bear one ring per corps. A spare ring of a corps you already bear won't bind to you: it waits for another
    bearer.
- **Calling your ring back:** anyone can call the rings that chose them, from anywhere.
  - Say it in chat (no extra setup): *"ring, come to me"*, *"ring, return to me"*, *"come to me, ring"*,
    *"ring, come back"*, *"I summon my ring"* or *"I call my ring"* call every ring. *"green ring, come to me"*,
    *"come to me, blue ring"* or *"return to me, star sapphire ring"* call one. Capitals don't matter.
  - `/trigger gl_recall` calls every ring; `/trigger gl_recall set 11` to `19` calls one (11 green, 12 yellow, 13 red,
    14 orange, 15 blue, 16 violet, 17 indigo, 18 white, 19 black).
  - With KubeJS: `/ring recall [corps]`, and looser wordings in chat (*"come back blue ring"*).
  - A ring lying anywhere in a loaded area, in any dimension, flies back to you. One in your ender chest comes out at
    your feet. Anywhere else (a chest, an unloaded area), a new ring forms on you and the one left behind goes dark.

## Two rings: the Spectrum Bond

Wear two of the nine spectrum rings (both Lantern Ring slots) and they bond. Each ring keeps its own power and bar; the
**Spectrum Bond** adds a bar and a skill tree of its own (powers menu), and merged suits.

- **The bar:**
  - **Twin Beam** (hold): both rings' beams at once, the first ring's from your right hand, the second's from your
    left. Each ring pays for its own beam.
  - **Twin Constructs** (hold the key): one wheel with both corps' construct weapons.
  - **Spectrum Fusion:** a burst that fuses both emotions; every pair has its own (*Will Over Fear*, *Rage Tempered
    by Hope*, *Life and Death*...). 125 charge from each ring, every 30 seconds; Fusion Mastery makes it 75 every 15.
  - **Prismatic Shield** (toggle): Resistance II in both colors; each ring pays a charge a tick.
  - **Spectrum Overload** (ultimate): everything within 12 blocks is blasted into the air, and you get Strength II,
    Resistance II and Speed II for 15 seconds. 400 charge from each ring, once a minute.
  - Second page: the Emotional Spectrum menu.
- **The skill tree** (XP levels): Twin Beam → Twin Constructs → Prismatic Shield; Spectrum Fusion → Fusion Mastery →
  Spectrum Overload; **Shared Light** (charge flows from the fuller ring to the emptier one) → **Twin Lanterns**
  (recharging either ring at its lantern fills both) → **Resonance** (both rings regain 20 charge a second); Dual
  Vitality (+10 hearts) → Twin Strength (+3 damage) → Spectrum Flight (faster flight).
- **Merged suits:** the accessories menu gets a *Spectrum Suit* slot. Both corps' suits split down the middle
  (*Split Light*) or at the belt (*Above and Below*), each either way round, or *Own Suits* to keep each ring's own.
  It shows while either ring's suit is on.
- The first ring in this order is the right-hand one: green, yellow, red, orange, blue, violet, indigo, white, black.

## Your emotions

Every player has eight emotions: willpower, fear, rage, avarice, hope, love, compassion and death.

- **The day you first join**, each starts at a random **10 000 to 15 000**.
- They grow as you play (below) and with quests.
- **The Emotional Spectrum menu** shows them. Open it by saying *"emotions"* in chat, with `/trigger gl_emotions`,
  with `/emotions` (KubeJS), or with the *Emotional Spectrum* button on a ring's or a host's bar. It's a clickable
  chat menu:
  - **Main page:** each emotion's bar, its percentage of the threshold (20 000), its level (one per 10%) and the amount
    itself. It also tells you which entity you host, and how long until an entity may choose you again.
  - **Click an emotion** for its page: what you were born with, every action that raised it (with the points each
    has earned you), and its three quests. Quests track themselves; finishing one gives its reward and starts the
    next.

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

## The ring chooses you

When an emotion reaches the **threshold (20 000)** while you're **in survival**, that corps' ring streaks down to you
within a second: *"&lt;Name&gt;, you have great willpower. Welcome to the Green Lantern Corps. Do you accept?"*
Everyone starts between 10 000 and 15 000, so the first ring comes after some play (or a quest or two). Say
*lantern check* to see how far each corps is. To try it straight away, an admin can run
`/lantern offer <player> <corps>` or set an emotion to 20 000.

- Click **[ACCEPT]** or **[DECLINE]**, or type **yes** / **no** in chat.
- If you accept, the ring is bound to you and brings its lantern. If your inventory is full, they drop at your feet.
- If you decline, or wait 60 seconds, the ring flies away and doesn't return for an hour.
- The **White** ring only comes to someone who has reached the threshold in all seven spectrum emotions.
- The **Black** ring comes to the emotionally dead: someone with **more than three of the seven spectrum emotions
  still at the 10 000 floor** (below 11 000). Since everyone starts between 10 000 and 15 000, a few players get it
  the day they join; the rest never will unless an admin lowers their emotions. Admins can move the floor with
  `/lantern blackfloor <n>`.

## The emotional spectrum entities

Nine beings of pure emotion roam the world, one of each. Each is either free, out in the world, inside a host, or
sealed in a lantern. You don't need a ring to host one: only the emotion.

| Entity | Emotion | How it comes | Where |
|---|---|---|---|
| Ion | Willpower | offers itself to someone with 100% willpower | in the sky |
| Parallax | Fear | hunts someone with 60% fear and possesses them (or: sacrifice ten rings to the yellow lantern) | anywhere in the Overworld |
| The Butcher | Rage | a boss: bring it down, and it takes the nearest player with 50% rage | the Nether |
| Ophidian | Avarice | offers itself to someone with 100% avarice, once they throw it a **block of gold** | caves (below y 30) |
| Adara | Hope | offers itself to someone with 100% hope | in the sky |
| The Predator | Love | hunts someone with 60% love and possesses them | anywhere in the Overworld |
| The Proselyte | Compassion | offers itself to someone with 100% compassion | in the sky |
| The Life Entity | Life | offers itself to someone with all seven spectrum emotions at 100% | in the sky |
| Nekron | Death | a boss: bring it down, and it takes the nearest player with 50% death | the deep dark (below y 0) |

- **One at a time:** a host can't take a second entity. After you lose yours (released, drawn out with a lantern, or
  taken back by an admin), **no entity will choose you for an hour**.
- **Testing:** `/lantern entity summon <entity>` makes it appear right in front of you; chat says who it chooses and
  has a **[Make me its host now]** button. `/lantern entity host <player> <entity>` does the same for anyone.
- **When they come:** once a minute, each free entity has a chance (about 1 in 6) to come to a player it can draw:
  100% of its emotion for the ones that offer, 60% for the hunters, 25% for the bosses. It stays 10 minutes (20 for
  hunters and bosses), then fades away until next time.
- **Offers:** click **[ACCEPT]** or **[DECLINE]** in chat. Declining keeps it away from you for 30 minutes.
- **Hunters** come from behind and fly at you; if one reaches you, it possesses you. A host of a hunter is sometimes
  overtaken by it.
- **Bosses** fight back and show a boss bar. At 15% health one takes the nearest worthy player as its host;
  otherwise it vanishes.
- **A free entity strengthens its own rings:** while it's out in the world, bearers of its color within 24 blocks
  recharge.

### Hosting

You get the entity's power, with its own bar and skill tree (powers menu). No ring needed.

- **Always:** +10 hearts and armor, the entity's aura, and **its suit**: the entity's look from A New Corps' suits
  (Ion: Ion, Parallax: Parallax with its cape, the Butcher: Atrocitus, Ophidian: Larfleeze, Adara: Saint Walker, the
  Predator: Carol Ferris, the Proselyte: Indigo-1, the Life Entity: White Lantern, Nekron: Black Lantern). *Mortal
  Form* (last page) hides it.
- **Its power refills on its own, always**, faster than any ring (60 a second, 120 with Wellspring), and is full
  whenever the entity comes to you.
- **Skill tree** (XP levels):
  - the body: Vitality I/II (+10 hearts each), Might I/II (+4 damage each), Flight, and the entity's passive;
  - its three abilities and its ultimate;
  - **its light:** the corps beam, a **construct wheel** and **Forge Ring**;
  - **its rings:** Empower Ring and Living Lantern;
  - its reserves: Deep Reserves (6 000 power) and Wellspring.
- **Beam:** the beam of its corps' ring (Ion: willpower beam, the Butcher: blood vomit...).
- **Constructs:** hold the construct key and pick one: that corps' A New Corps construct weapons, plus the entity's own
  hard-light constructs (Ion's giant fist, Parallax's fear spikes, Ophidian's grasping hand, the Predator's crystal
  prison, the Proselyte's cage, Nekron's grave cage and grave spikes). The Life Entity forms one weapon of each color;
  Nekron the grey Balance weapons. They dissolve when you stop hosting.
- **Forge Ring:** forge a new ring of the entity's color for someone worthy (3 000 power, once every 5 minutes).
- **Empower Ring:** look at a bearer of the entity's color within 24 blocks: +1 000 charge to their ring (400 power).
- **Living Lantern** (toggle): you become a lantern. Bearers of your color within 8 blocks recharge 100 a second, and
  one who **sneaks beside you** recites their oath for a full charge (800 of your power, once every 30 seconds each).

| Entity | Abilities (then the ultimate) | Passive |
|---|---|---|
| Ion | Will Surge, Giant Fist, Unbreakable Will → Willpower Unbound | Indomitable |
| Parallax | Fear Gaze, Spikes of Terror, Terror → Fear Incarnate | Feeds on Fear |
| The Butcher | Roar of Rage, Rampage, Gore Charge → Slaughter | Bloodlust |
| Ophidian | Coil, Hoard, Devour → Serpent's Hoard | Endless Avarice |
| Adara | Wings of Hope, Beacon of Hope, Rekindle → Hope Eternal | Undying Hope |
| The Predator | Crystal Embrace, Heart's Desire, Obsession → Love Unending | Devotion |
| The Proselyte | Empathy, Tendrils, Indigo Phase → Compassion for All | Empathic Link |
| The Life Entity | Life Wave, Regrowth, Breath of Life → Light of Creation | Eternal Life (cheat death every 10 minutes) |
| Nekron | Black Hand, Raise the Dead, Death's Touch → Blackest Night | Deathless |

### Ending it

- **Give it up:** the **Release** slot on its bar, or say *"I release you"*, then confirm. It goes back into the world.
- **Draw it out with a lantern:** another player **sneaks while holding a corps' lantern** and **looks at the host for
  five seconds** from within 6 blocks. The host sees a warning and can get away. Then the entity is sealed: the lantern
  becomes the **Lantern of &lt;entity&gt;**. Right-click it to **release** the entity into the world, or to **host**
  it yourself if you're worthy. A lantern left shut for two hours goes empty: the entity breaks free.

Either way, no entity will choose that host again for an hour.

## Corps leaders

An admin appoints leaders (`/lantern leader <player> <corps>`). A leader can revoke the ring of a member of their own
corps: `/trigger gl_roster` lists online members with their ids, then `/trigger gl_revoke set <id>`. The revoked ring
goes to the leader, unbound, for a new recruit. Leaders can't revoke each other.

## Admin commands

With KubeJS: `/lantern` (operators only). Without it, run the matching function, as the player where it acts on one:

- `/function final_lanterns:admin/help` lists them all.
- `/function final_lanterns:entity/admin/summon/ion` summons Ion in front of you;
  `/execute as Steve run function final_lanterns:entity/admin/host/ion` makes Steve its host.
- `/execute as Steve run function final_lanterns:admin/offer/green` makes the green ring choose Steve now.
- `/scoreboard players set Steve gl_e_will 20000` sets an emotion.

| Command | What it does |
|---|---|
| `/lantern give <player> <corps>` | give a ring already bound to the player |
| `/lantern unbound <player> <corps>` | give an unbound ring |
| `/lantern battery <player> <corps>` | give that corps' lantern |
| `/lantern emotion <player> <emotion> set\|add <n>` | change an emotion (`scoreboard players set <player> gl_e_<emotion> <n>`) |
| `/lantern reroll <player>` | roll their starting emotions again |
| `/lantern offer <player> <corps>` | make that ring choose the player now |
| `/lantern leader\|unleader <player> <corps>` | appoint or remove a corps leader |
| `/lantern remove <player> <corps>` / `removeall <player>` | take rings away (inventory, hands and Curios) |
| `/lantern unbind <player>` | unbind the ring in their main hand |
| `/lantern reset <player>` / `cooldowns <player>` / `show <player>` | reset emotions, clear decline cooldowns, show emotions |
| `/lantern threshold <n>` | change the threshold (`scoreboard players set #threshold gl_cfg <n>`) |
| `/lantern blackfloor <n>` | the Black ring comes when 4+ spectrum emotions are below n (default 11 000) |
| `/lantern enable` / `disable` | turn emotions and ring offers on or off |
| `/lantern entity status\|reset\|on\|off` | where each entity is; free them all; let them appear or not |
| `/lantern entity summon <entity>` | a free entity appears in front of you, and chat says who it chooses (ion, parallax, butcher, ophidian, adara, predator, proselyte, life, nekron) |
| `/lantern entity host <player> <entity>` | make the player its host now, skipping its emotion check and the one-hour wait |
| `/lantern check` | the same as saying *lantern check*: what works, and why no ring has come |

- **Emotion names:** will, fear, rage, greed, hope, love, compassion, death.
- **Corps names:** green, yellow, red, orange, blue, violet, indigo, white, black.
- **The entity cooldown:** `scoreboard players set <player> gl_ehcd 0` lets entities choose a player again now.

## Editing

The jar is built from `src/`, which is generated: don't edit it by hand.

- `base/` is A New Corps, renamed into the `final_lanterns` namespace. `python3 -I tools/import_anc.py <zip>`
  refreshes it from a new A New Corps zip.
- `python3 tools/gen_final.py` copies `base/` into `src/` and adds our systems:
  - `tools/systems.py`: ring binding, recall, offers, leaders, admin and the KubeJS script;
  - `tools/emotions.py`: emotions, the menu and quests;
  - `tools/entities.py`: the entities;
  - `tools/hosts.py`: the host powers and suits;
  - `tools/hardlight.py`: the hard-light constructs;
  - `tools/spectrum.py`: the Spectrum Bond (two rings) and its merged suits;
  - `tools/check.py`: the *lantern check*;
  - `tools/entity_models/`: the entities' models;
  - `tools/common.py`: the nine corps and how they map onto A New Corps' rings.
- `python3 tools/build.py` validates and packages the jar. `tools/lint_commands.py` syntax-checks every command (needs
  the `mecha` package). Both count problems already present in A New Corps separately and fail only on new ones.
