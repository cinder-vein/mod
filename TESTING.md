# In-game test checklist (Lantern Corps 8.0)

Use a creative test world with cheats on, plus a second account or a friend for the multiplayer checks.
`/reload` re-runs the datapack after any change.

## 1. Rings, suits, beam
- [ ] `/give @s greenlantern:green_lantern_ring` and hold it. Chat says *"The ring is now bound to you"*, and the tooltip
      shows *Bound to &lt;you&gt;*.
- [ ] A small logo plate sits on the **front of your right hand**, not the wrist. Check in third person (F5).
- [ ] Hold the beam key: your right arm points forward and the beam leaves the hand.
- [ ] **Suit Up** (bottom slot of the first page): the suit appears and your face stays visible.
- [ ] In the accessories menu, the *Green Lantern Suit* slot offers Corps Uniform, Shadow and Classic, and the
      *Mask* slot includes **No Mask**.
- [ ] With a slim (Alex) skin, the sleeves line up with your arms.

## 2. Charge
- [ ] `/energybar value get @s greenlantern:green_lantern ring_charge` shows a value. Fly or use powers so it drops.
- [ ] Right-click with a Green Power Battery in your main hand: the charge goes to full and the oath plays.
- [ ] Place the battery, empty your hand, right-click it: it charges.
- [ ] Note the charge, put the ring in a chest, take it back out: the charge is the same (within a second's worth).
      Same after relogging.

## 3. Two rings
- [ ] Hold green in the main hand and blue in the offhand. Press **X** to switch bars; Spectrum Fusion shows on
      Green's third page. Using it shows *"Hope Ignites Will"*.
- [ ] Your hearts don't double. Only one suit can be up at a time.
- [ ] With Curios: two ring slots are available, and both rings work there.

## 4. Ownership
- [ ] A second player picks up your bound ring and holds it: it leaves their hand and lands at your feet (or drops if
      you're offline). Try the same with their Curios slot.

## 5. Ring offers
- [ ] `/lantern emotion <you> will set 20000` (or `scoreboard players set <you> gl_e_will 20000`). In survival,
      within a second a green ring hovers in front of you and the question appears in chat.
- [ ] Click **[ACCEPT]**: you get a bound ring, a title and a server-wide announcement.
- [ ] Repeat with fear and click **[DECLINE]** (or type *no* with KubeJS): the ring rises and vanishes.
      `/lantern cooldowns <you>` lets it come back.
- [ ] Wait 60 s without answering: it leaves on its own.
- [ ] `/trigger gl_emotions` lists your emotions.

## 6. Leaders
- [ ] `/lantern leader <you> green`. The second player is a Green member wearing a ring.
- [ ] Stand within 8 blocks and use **Revoke Ring**: their ring is removed and you get an unbound one.
- [ ] `/trigger gl_roster` lists online members with ids; `/trigger gl_revoke set <id>` revokes remotely.

## 7. Admin
- [ ] `/lantern` (no arguments) prints the help.
- [ ] `/lantern give <player> red`, `battery`, `remove`, `removeall`, `unbind`, `threshold 5000`, `disable` / `enable`.

## 8. Corps checks
- [ ] Orange: kill a zombie with the ring on (*"Your hoard claims the Zombie!"*), then use Greed Construct Arrival.
- [ ] Black: kills add charge; Raise the Dead; Undying.
- [ ] Red: Rage tints the screen. Sinestro: Nightmare shows *"Don't you hear him?"* to players.

If something fails, open Palladium's **Addon Pack Log** (main menu → Mods → Palladium) and check the game log for
`greenlantern` errors, then send them over.
