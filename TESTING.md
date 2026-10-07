# In-game test checklist (Lantern Corps 9.0)

Use a creative test world with cheats on, plus a second account or a friend for the multiplayer checks.
`/reload` re-runs the datapack after any change.

## 1. Rings, suits, beam
- [ ] `/give @s greenlantern:green_lantern_ring` and hold it. Chat says *"The ring is now bound to you"*, and the tooltip
      shows *Bound to &lt;you&gt;*.
- [ ] In third person (F5), look at your right hand. The ring's logo signet sits on the **outside of the hand, at the
      base of the fingers**, and a thin band crosses the front of the hand. It's on the hand, not the wrist.
- [ ] Wear a second ring (blue in the offhand, or a second Curios slot). It shows on your **left** hand.
- [ ] Hold the beam key: your right arm points forward and the beam leaves the hand.
- [ ] **Suit Up** (bottom slot of the first page): the suit appears and your face stays visible. Suit and mask
      choices are in the accessories menu.

## 2. Lantern (Power Battery) and charge
- [ ] Place a Green Power Battery. It's a small green lantern with a glowing glass chamber (logo inside), glowing side
      lenses, a stepped cap and a white wire handle.
- [ ] Right-click it with an empty hand, or right-click while holding it: the ring charges fully and the oath plays.
- [ ] `/energybar value get @s greenlantern:green_lantern ring_charge` shows the charge. Take the ring off and put it
      back on (or relog): the charge stays the same.

## 3. Constructs
- [ ] Buy **Constructs** in the powers menu. Press **X** to reach page 2: *Construct 1* to *Construct 5*.
- [ ] Construct 1 (Sword) forms a green hard-light sword in your empty hand. Press it again: the sword dissolves.
- [ ] Hold a stack of dirt and press Construct 1: the dirt moves to a free slot and the sword takes its place. Holding
      the ring in your main hand instead puts the sword in your inventory, and the ring stays in your hand.
- [ ] Construct 2 (Blast) fires a bolt where you look. Construct 3 (Tower Shield) appears in the offhand and blocks with
      right-click. Construct 4 gives 64 Construct Blocks you can place. Construct 5 (Scan) on a mob prints its health
      and armor, and the mob glows.
- [ ] **Configure Constructs** (page 4) or `/trigger gl_construct`: click *[Slot 2]*, then *[Defense]*, then
      *[Barrier Wall]*. Slot 2 now shows Barrier Wall. It's locked until you buy *Defense Constructs I*: pressing the slot
      says so.
- [ ] Buy the branches and try each construct:
  - Barrier Wall: a 5×4 wall 3 blocks ahead, gone after 15 s.
  - Dome: a dome around you, gone after 15 s.
  - Bridge: 16 blocks long, gone after 30 s. Hard light only replaces air.
  - Gatling: hold right-click to fire.
  - Missiles and Cannon: they explode without breaking blocks.
  - Scuba Gear: a helmet bubble and tank; you breathe underwater. Press again to remove it.
  - Mining Drill, Mace, Battle Axe, Sword & Shield.
- [ ] The **Construct Wheel** (page 1) lists every construct. Locked ones are grey.
- [ ] Drop a held construct with Q: it vanishes. Take the ring off: held constructs and leftover construct blocks vanish.
- [ ] Let the ring run dry while holding a construct: it dissolves.
- [ ] Signature constructs (after all four branches):
  - Green Train
  - Sinestro Fear Spikes
  - Red Blood Claws (they set mobs on fire)
  - Orange Grasping Hands
  - Blue Sanctuary
  - Violet Crystal Spear
  - Indigo Staff (long reach; nearby players regenerate)
  - White Radiant Aegis
  - Black Hand

## 4. Ring benefits
- [ ] With a charged ring, a villager's prices drop (Hero of the Village).
- [ ] Each corps' gift (shown next to Suit Up in the skill tree):
  - Green: `/effect give @s darkness` is cleared at once.
  - Red: you can stand in lava.
  - Orange: XP orbs fly to you.
  - Blue: you regenerate below 10 hearts.
  - White and Black: you never get hungry.

## 5. Two rings
- [ ] With green and blue worn, Spectrum Fusion is on page 4 of Green's bar. Your hearts don't double, and only one suit
      can be up at a time.

## 6. Ownership
- [ ] A second player picks up your bound ring and holds it: it jumps out of their hand and flies to you, even if you're
      in another dimension. Try the same with their Curios slot: the ring is thrown out within half a second.
- [ ] Log out, then have them hold it again: it lands at their feet, they can't pick it back up, and it doesn't despawn.
      You can pick it up when you're back.
- [ ] `/lantern unbind <you>` while holding your ring: it stays unbound while you hold it, and binds to the next player
      who holds it.

## 7. Ring offers
- [ ] `/lantern emotion <you> will set 20000` in survival. Within a second a ring hovers in front of you and asks.
- [ ] Click **[ACCEPT]**: you get a bound ring **and its Power Battery**. Try it with a full inventory: both drop at your
      feet.
- [ ] Decline (or type *no* with KubeJS): the ring flies away. `/lantern cooldowns <you>` lets it come back.

## 8. Leaders
- [ ] `/lantern leader <you> green`. A member wearing a green ring (in a hand or a Curios slot) stands near you. Use
      **Revoke Ring** (page 4): their ring is gone, and you get it unbound. Holding it doesn't bind it to you; your
      recruit can bind it.
- [ ] `/trigger gl_roster` lists members; `/trigger gl_revoke set <id>` revokes remotely.

## 9. Admin
- [ ] `/lantern` prints the help. Try:
  - `/lantern give <player> red`
  - `battery`
  - `remove` (also clears Curios slots)
  - `removeall`
  - `threshold 5000`
  - `disable` / `enable`

If something fails, open Palladium's **Addon Pack Log** (main menu → Mods → Palladium) and check the game log for
`greenlantern` errors, then send them over.
