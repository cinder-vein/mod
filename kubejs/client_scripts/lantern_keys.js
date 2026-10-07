// Lantern Corps: hold Ctrl and press the first ability key to switch your ring between beam mode
// (Beam, Construct Wheel) and blast mode (Energy Blast, Scan). Palladium can't see Ctrl, so this client
// script tells the server while it's held; the first ability slot then shows Switch Mode.
// Loaded by Palladium's KubeJS integration when KubeJS is installed (without it, sneak instead of Ctrl).
let glCtrlDown = false
let glCtrlBeat = 0
let glScreenClass = null
try {
  glScreenClass = Java.loadClass('net.minecraft.client.gui.screens.Screen')
} catch (e) {
  glScreenClass = null
}

ClientEvents.tick(event => {
  const mc = Client
  if (!mc.player) return
  let down = false
  if (mc.screen == null) { // in game only: Ctrl in a menu or chat doesn't count
    try {
      down = glScreenClass ? !!glScreenClass.hasControlDown() : !!mc.options.keySprint.isDown()
    } catch (e) {
      down = false
    }
  }
  glCtrlBeat++
  if (down !== glCtrlDown || glCtrlBeat >= 20) { // on change, and once a second so the server knows we're here
    glCtrlDown = down
    glCtrlBeat = 0
    mc.player.sendData('greenlantern_keys', { ctrl: down })
  }
})
