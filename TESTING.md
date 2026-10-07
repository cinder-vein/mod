# In-game test checklist (Lantern Corps 10.0)

Use a creative test world with cheats on, plus a second account or a friend for the multiplayer checks.
`/reload` re-runs the datapack after any change.

## 1. Rings, suits, beam
- [ ] `/give @s greenlantern:green_lantern_ring`. Within half a second chat says *"The ring binds itself to you"*, and
      the tooltip shows *Bound to &lt;you&gt;*.
- [ ] Hold the ring in your hand: no ability bar, no hearts. Put it in a **Curios ring slot**: the bar and the
      hearts appear. Rings only work from a ring slot.
- [ ] Put a fresh ring straight into the ring slot from the creative menu (never carried): it pops out with a message.
      Pick it up, wait a moment, wear it: it works.
- [ ] In third person (F5), look at your right hand. The ring's logo signet sits on the **outside of the hand, at the
      base of the fingers**, and a thin band crosses the front of the hand. It's on the hand, not the wrist.
- [ ] Wear a second ring (blue, in the second ring slot). It shows on your **left** hand.
- [ ] Hold the beam key: your right arm points forward and the beam leaves the hand.
- [ ] **Suit Up** (bottom slot of the first page): the suit appears and your face stays visible. Suit and mask
      choices are in the accessories menu.
- [ ] Every slot on the bar has its own pixel-art icon in the ring's colors (no vanilla item icons).
- [ ] **Modes** (KubeJS on client and server): hold **Ctrl**. The first slot turns into *Switch Mode*. Press the first
      ability key (V): the actionbar says *Blast mode*. Release Ctrl: the first two slots are now **Energy Blast** and
      **Scan**.
  - Energy Blast fires a bolt (40 charge). Scan on a mob prints its health and armor, and it glows.
  - Ctrl + V again: back to *Beam mode* (Beam and Construct Wheel).
  - Without KubeJS: sneak instead of Ctrl. With KubeJS, sneaking doesn't change the first slot.

## 2. Lantern (Power Battery) and charge
- [ ] Place a Green Power Battery. It's a small green lantern with a glowing glass chamber (logo inside), glowing side
      lenses, a stepped cap and a white wire handle.
- [ ] Right-click it with an empty hand, or right-click while holding it: the ring charges fully and the oath plays.
- [ ] `/energybar value get @s greenlantern:green_lantern ring_charge` shows the charge. Take the ring off and put it
      back on (or relog): the charge stays the same.
- [ ] Spend some charge and wait: the ring does **not** recharge on its own.
- [ ] Buy **Passive Recharge I** (60 levels, `/xp add @s 300 levels`): it regains 2 charge a second. Tier IV gives 16
      a second. Each tier needs the one before.

## 3. Constructs
- [ ] Buy **Constructs** in the powers menu. There's no construct page any more: the **Construct Wheel** (second slot
      of the first page) holds every construct, and locked ones are grey.
- [ ] Pick Sword on the wheel: a green hard-light sword forms in your empty hand. Pick it again: the sword dissolves.
- [ ] Hold a stack of dirt and pick Sword: the dirt moves to a free slot and the sword takes its place. Holding the ring
      in your main hand instead puts the sword in your inventory, and the ring stays in your hand.
- [ ] Tower Shield appears in the offhand and blocks with right-click. Construct Blocks gives 64 blocks you can place.
- [ ] Buy the branches and try each construct:
  - Barrier Wall: a 5×4 wall 3 blocks ahead, gone after 15 s.
  - Dome: a dome around you, gone after 15 s.
  - Bridge: 16 blocks long, gone after 30 s. Hard light only replaces air.
  - Gatling: hold right-click to fire. With two rings worn it fires at the same rate.
  - Missiles and Cannon: they explode without breaking blocks.
  - Scuba Gear: a helmet bubble and tank; you breathe underwater. Pick it again to remove it.
  - Mining Drill, Mace, Battle Axe, Sword & Shield, Giant Fist, Hammer Slam, Cage.
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
- [ ] Each corps' gift (shown beside the root of the skill tree):
  - Green: `/effect give @s darkness` is cleared at once.
  - Red: you can stand in lava.
  - Orange: XP orbs fly to you.
  - Blue: you regenerate below 10 hearts.
  - White and Black: you never get hungry.

## 5. Two rings: the Spectrum Bond
- [ ] Wear green (hand or Curios) and blue. Within a moment the actionbar says *Spectrum Bond: Willpower + Hope*, and the
      first time a chat message explains the bond.
- [ ] Press **X** through the pages:
  - The Spectrum Bond's bar: Spectrum Beam, Construct Wheel, Force Field, Ring Light, Suit Up.
  - Green's specials page and Blue's specials page.
  - Neither ring's own first page shows.
- [ ] Hold the beam key: a green beam from your right hand and a blue beam from your left. Each ring's charge drops.
- [ ] The Spectrum Charge bar shows both charges added together (2000 when both are full).
- [ ] Construct Wheel: a construct only Blue has unlocked forms in blue and costs Blue's charge. One Green has forms in
      green.
- [ ] Ctrl + V: **Twin Blast** fires a green and a blue bolt. Scan works.
- [ ] Open the powers menu: a **Spectrum Bond** tree. Buy *Spectrum Fusion* (8 levels): page 2 of the bond's bar has it.
      Using it shows *Hope Ignites Will*.
- [ ] Try *Shared Light* (one ring nearly empty: they even out), *Twin Batteries* (recharge one ring at its battery: both
      fill), *Prismatic Shield* (force field gives Resistance II and shimmers in both colors), *Twin Signatures*
      (second ring's signature on the wheel) and *Spectrum Overload*.
- [ ] Accessories menu: **Spectrum Suit** and **Spectrum Mask** slots. *Split Light* is green on your right side and
      blue on your left. Try the other designs with Suit Up on.
- [ ] Take the blue ring off: the bond's bar goes, Green's own first page comes back, and the merged suit comes off.
      Put it back on: the bond's skills are still bought.
- [ ] Your hearts don't double with two rings.

## 6. Ownership
- [ ] A second player picks up your bound ring and holds it: it jumps out of their hand and flies to you, even if you're
      in another dimension. Try the same with their Curios slot: the ring is thrown out within half a second.
- [ ] Log out, then have them hold it again: it lands at their feet, they can't pick it back up, and it doesn't despawn.
      You can pick it up when you're back.
- [ ] `/lantern unbind <you>` while holding your ring: it stays unbound while you hold it, and binds to the next player
      who holds it.

## 6b. Calling your ring
- [ ] Drop your bound ring, walk away (or go to the Nether), then run `/trigger gl_recall`. The ring flies to you.
- [ ] Put the ring in a chest, close it and `/trigger gl_recall`. A new ring forms on you. Take the old one out of the
      chest and wear it: it crumbles ("This ring has gone dark").
- [ ] **Without KubeJS** (or with it): say *"ring, come to me"* in chat: the ring flies back. *"Return to me, blue ring"*
      calls only the blue ring. If the ring is already on you, it says so.
- [ ] With KubeJS: `/ring recall green` works, and so does a looser wording like *"come back blue ring"*.
      `logs/kubejs/server.log` shows *"[Lantern Corps] KubeJS script loaded"*. If `/ring` is unknown, copy the repo's
      `kubejs/server_scripts` files into the game's `kubejs/server_scripts` and restart.
- [ ] Put the ring in your ender chest and call it: it comes out at your feet (no new ring).
- [ ] A member whose ring was revoked runs `/trigger gl_recall`: *"No ring has chosen you yet."*
- [ ] Craft a second green ring while wearing yours and hold it: it drops at your feet ("you already bear a ring of
      this corps"). Your own ring keeps working. A friend can pick it up and bind it.

## 6c. Forging a ring by oath
- [ ] Wear a charged green ring and type the Green Lantern oath in chat (works without KubeJS, word for word):
  *In brightest day, in blackest night, no evil shall escape my sight. Let those who worship evil's might, beware my
  power... Green Lantern's light!*
  - A title says *"A new Green Lantern ring is forged"*, 500 charge is spent, and you get an unbound ring.
  - Nearby players see the oath and the announcement.
- [ ] Carry the forged ring: it doesn't bind to you. Drop it (Q); a second player picks it up: it binds to them. Your
      own ring keeps working.
- [ ] Forge again right away: it says to wait (5 minutes). `/lantern forgecooldown 0` removes the wait.
- [ ] Without the ring on, the oath says *"no ring answers"*. Type only half the oath: nothing happens.
- [ ] `/trigger gl_forge` (and `/ring forge green` with KubeJS) recites the oath for you and forges.
- [ ] `/lantern forging off`: forging is refused.

## 7. Ring offers
- [ ] `/lantern emotion <you> will set 20000` in survival. Within a second a ring hovers in front of you and asks.
- [ ] Click **[ACCEPT]**: you get a bound ring **and its Power Battery**. Try it with a full inventory: both drop at your
      feet.
- [ ] Decline (or type *no* in chat; *yes* accepts): the ring flies away. `/lantern cooldowns <you>` lets it come back.

## 7b. Emotional Spectrum menu and quests
- [ ] Say *"emotions"* in chat (or `/trigger gl_emotions`, or the *Emotional Spectrum* button on the last page of a
      ring's bar). The menu lists all eight emotions with a bar, a percentage, a level and the amount.
- [ ] `/lantern emotion <you> will set 10000`: Willpower shows 50% and Lv 5.
- [ ] Click *Willpower*: its page lists what raised it (taking damage, blocking, absorbing) with the points from each,
      and its three quests. The first is active: *Stand Your Ground*, block 25 hearts with a shield.
- [ ] Block damage with a shield and reopen the page: the progress goes up. Finish it: a title and chat message show the
      reward (+1,500 Willpower), the quest gets a tick, and the next one starts.
- [ ] Sneak for a while: Fear's page shows the sneaking points growing.

## 7c. Flight and the force field
- [ ] Buy Flight and fly: you glow with an outline in your ring's color (no trail).
- [ ] Turn on Force Field: a bubble of hexagonal hard light surrounds you, turning and crouching with you. With two
      rings, the bubble takes your first ring's color; Prismatic Shield layers both colors.

## 7d. The emotional spectrum entities
- [ ] `/lantern entity status`: all nine are free.
- [ ] `/lantern emotion <you> will set 20000`, stand outside in the sky's view, then `/lantern entity summon ion`. A title
      says Ion is here; a huge green leviathan floats toward you. Within 8 blocks it offers itself: click **[ACCEPT]**.
  - The announcement goes out, Ion's model disappears, and you get the Ion host bar (Will Surge, Giant Fist,
    Unbreakable Will, Willpower Unbound, Release) and the Ion tree in the powers menu. Your bar's power is full.
  - Buy Will Surge (5 levels): it dashes you forward. Buy Flight: you fly with a green glow.
- [ ] Second player: hold a Power Battery, **sneak and look at you** from a few blocks for 5 seconds: the actionbar
      counts up, then the battery becomes **Lantern of Ion** and your host bar is gone.
  - They right-click the lantern: **[HOST IT]** (needs 100% willpower) or **[RELEASE IT]** (Ion is free again).
- [ ] Host again, then say *"I release you"* and click **[RELEASE IT]**: Ion leaves you.
- [ ] `/lantern emotion <you> fear set 12000` then `/lantern entity summon parallax`: it appears behind you and flies
      at you. When it reaches you, you're possessed. Within a few minutes it takes control (darkness, nausea).
- [ ] In the Nether with 25%+ rage: `/lantern entity summon butcher`. A boss bar appears; the Butcher fights. Bring it
      to 15%: with 50% rage you become its host, without it the Butcher vanishes.
- [ ] Ophidian (100% avarice, below y 30): it asks for gold. Throw it a block of gold: then it offers itself.

## 8. Leaders
- [ ] `/lantern leader <you> green`. A member wearing a green ring stands near you. Use
      **Revoke Ring** (last page): their ring is gone, and you get it unbound. Holding it doesn't bind it to you; drop it
      and your recruit can pick it up and bind it. The revoked member can't wield it.
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
