# In-game test checklist (Final Lanterns 1.4)

Use a creative test world with cheats on, plus a second account or a friend for the multiplayer checks.
`/reload` re-runs the datapack after any change. Install the mods listed in the README first (Palladium, GeckoLib,
GraveCore, Curios, KubeJS), and remove the old Lantern Corps and A New Corps jars.

## 1. Loading
- [ ] Coming from Lantern Corps 10: `lantern_commands.js` and `lantern_keys.js` are gone from the game's
      `kubejs/server_scripts` and `kubejs/client_scripts` folders.
- [ ] Type **`/trigger gl_check`** (works for any player, cheats or not): every line is a ✔ (datapack running, chat
      phrases, KubeJS commands loaded, *Lantern Ring slots: 2*). The corps lines show your emotion against the
      threshold, and each free entity says what brings it and your own number. Saying **lantern check** and
      `/lantern check` (also without op) show the same.
- [ ] Any ✘ names what's wrong (for a function that didn't load, the name to search for in `logs/latest.log`).
- [ ] The game starts with Final Lanterns in the mods list (*"Based on A New Corps"* in its description).
- [ ] `logs/latest.log` has no errors about `final_lanterns` functions failing to load.
- [ ] `logs/kubejs/server.log` says *"[Final Lanterns] KubeJS script loaded"*. If not, copy
      `kubejs/server_scripts/lantern_commands.js` from this repository into the game's `kubejs/server_scripts`.
- [ ] The A New Corps creative tabs are there (*Rings*, *Batteries & Other*).

## 2. Your emotions on joining
- [ ] Join a new world: chat says *"The emotional spectrum stirs in you. [See your emotions]"*.
- [ ] Click it (or say *emotions*): every emotion is between **10 000 and 15 000** (50% to 75%, Lv 5 to 7).
- [ ] Click an emotion: its page shows *Born with: +N*, what raised it, and its quests.
- [ ] `/lantern reroll <you>` rolls them again (the menu shows new numbers).
- [ ] Relog: the numbers don't change (you're only rolled once).

## 3. The Black Lantern ring
- [ ] Set four spectrum emotions low: `/scoreboard players set @s gl_e_will 10000` (same for `gl_e_fear`,
      `gl_e_rage`, `gl_e_greed`). Within a second the **Black Lantern** ring streaks down and offers
      itself (*"a heart gone cold..."*).
- [ ] With only three below 11 000, it doesn't come.
- [ ] `/lantern blackfloor 13000` raises the floor: more players qualify.

## 4. Rings (A New Corps) with our additions
- [ ] Accept a ring offer (`/lantern offer <you> green`): the ring is bound to you (*Bound to &lt;you&gt;*) and its
      lantern comes with it.
- [ ] With the suit **off**, the ring still works: fire the beam, open the construct wheel, fly, and buy skill-tree
      nodes. Toggling the suit only changes your look (suit, mask, transformation, sound).
- [ ] Wear it in the **Lantern Ring** slot: the A New Corps Willpower power appears. Its bar has an **Emotional
      Spectrum** button (second or third page): it opens the menu.
- [ ] Drop the ring and say *"ring, come to me"*: it flies back. Put it in a chest, walk away and call it: a new ring
      forms on you and the one in the chest goes dark when worn.
- [ ] A second player picks up your ring: it flies back to you.

## 5. Entities: one host, one hour
- [ ] `/lantern entity summon ion` (or `/function final_lanterns:entity/admin/summon/ion`): Ion appears 6 blocks in
      front of you and chat says it offers itself to players with 100% willpower, with a **[Make me its host now]**
      button.
- [ ] With willpower at 20 000 (`/lantern emotion <you> will set 20000`), within 10 seconds Ion flies to you and offers
      itself. Accept: you host Ion (suit, aura, the host power).
- [ ] `/lantern entity reset`, summon Parallax: it comes straight at you and possesses you.
- [ ] `/lantern entity host <you> butcher`: you host the Butcher right away.
- [ ] While hosting Ion, summon Adara for yourself (hope 20 000): accepting says *"You already host an entity."*
- [ ] Release Ion (Release slot, or say *"I release you"* and confirm). Then summon Ion again and accept: *"No entity
      will join you yet: you lost one too recently."* The menu says how many minutes are left (60).
- [ ] `/scoreboard players set @s gl_ehcd 0`: now you can host again.
- [ ] A second player draws your entity out with a lantern (sneak, hold a corps' lantern, look at you for 5 s). You
      lose it and the one-hour wait starts for you.

## 6. Hosting: the new powers
Buy the nodes in the host's skill tree (`/xp add @s 300 levels`).
- [ ] **Passive recharge:** spend power, then watch the bar refill on its own at about 60 a second (faster with
      Wellspring), even while flying or fighting.
- [ ] **Beam** (first slot): Ion fires the green willpower beam, the Butcher blood vomit, and so on.
- [ ] **Constructs** (second slot, hold the key): Ion's wheel shows the green construct weapons and Giant Fist. Picking
      a weapon puts it in your hand; the shield goes in your offhand. Release the entity: the construct weapons
      vanish from your inventory.
- [ ] **Forge Ring** (page 2): a ring of the entity's color forms in front of you (green for Ion, black for Nekron).
- [ ] **Empower Ring** (page 2): with a second player wearing a green ring in front of you, use it: their ring gains
      1 000 charge and they see *"Ion's light fills your ring."* With nobody in sight: *"Look at a Green Lantern ring
      bearer..."*.
- [ ] **Living Lantern** (page 2, toggle): the green bearer within 8 blocks recharges; when they sneak beside you,
      they recite the oath and their ring fills (once every 30 s).
- [ ] **Suit:** each host wears its entity's suit (Ion galaxy, Parallax with cape, Atrocitus, Larfleeze, Saint Walker,
      Carol Ferris, Indigo-1, White Lantern, Black Lantern). **Mortal Form** (page 3) hides it.
- [ ] **A free entity near your ring:** with Ion out in the world (summoned, not hosted), a green bearer within 24
      blocks sees *"Ion is near: your ring drinks its light."* and recharges.

## 6b. Skill trees (1.4)
- [ ] Host Ion (`/lantern entity host <you> ion`): its tab in the powers menu is the Willpower tree (lime background,
      green bar), with *Ion's Power* on the right and *Ion's Light* on the left. Every node opens and can be bought.
- [ ] Toggle the Ion node: Ion's suit and aura appear; toggle again: they go.
- [ ] Wear two rings: the Spectrum Bond tab has the same layout, a spectrum bar and a prismatic background; the
      second ring is on your left hand.

## 7. Two rings: the Spectrum Bond
- [ ] The Lantern Ring slot (Curios) has **two** slots, and `/trigger gl_check` says *Lantern Ring slots: 2*.
- [ ] Put an unbound ring from the creative menu straight into the slot: it pops out with *"A ring has to bind to you
      before you can wear it..."*, lands back in your inventory and binds; put it on again.
- [ ] With both rings on, `/trigger gl_check` lists both as *worn, its power is on* and *Spectrum Bond: on*.
- [ ] Wear a green and a yellow ring: the actionbar says *Spectrum Bond: Willpower + Fear* and a **Spectrum Bond**
      bar and skill tree appear (each ring keeps its own). Take one off: *"The Spectrum Bond fades."*
- [ ] Buy the nodes (`/xp add @s 300 levels`). **Twin Beam** (hold): a green beam from the right hand and a yellow one
      from the left; both rings' charge drops.
- [ ] **Twin Constructs**: the wheel shows green and yellow construct weapons. Take a ring off: the bond's
      construct weapons vanish.
- [ ] **Spectrum Fusion**: the title *Will Over Fear*, both colors, and both rings lose 125 charge.
- [ ] **Prismatic Shield**: Resistance II and particles in both colors while it's on.
- [ ] **Spectrum Overload**: everything around flies up; you get Strength, Resistance and Speed.
- [ ] **Shared Light**: drain one ring (beam) and watch charge flow into it from the other. **Twin Lanterns**:
      recharge the green ring at its lantern: the yellow fills too.
- [ ] Turn a ring's suit on: the merged **Split Light** suit shows (green right half, yellow left half). In the
      accessories menu, **Spectrum Suit** lists Split Light, Above and Below (and reversed) and **Own Suits**, which
      brings each ring's own suit back.

## 8. Parallax by sacrifice (A New Corps)
- [ ] As a Sinestro Corps bearer, sacrifice ten rings at the yellow lantern: the counter shows *Rings Sacrificed n/10*.
      At ten, if Parallax is free and you host nothing, **our** Parallax takes you (the host power, its suit). If
      Parallax is taken: *"Parallax does not answer your sacrifice..."*

## 9. Admin
- [ ] `/lantern` lists the commands. `/lantern entity status` shows where each entity is.
- [ ] Without KubeJS: `execute as <you> run function final_lanterns:admin/help` works the same.
