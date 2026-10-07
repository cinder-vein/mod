// Ctrl state from the client script (assets/greenlantern/kubejs_scripts/lantern_keys.js)
NetworkEvents.dataReceived('greenlantern_keys', event => {
  const player = event.player
  if (!player) return
  const data = event.data
  const down = data != null && data.getBoolean('ctrl')
  player.server.runCommandSilent(`execute as ${player.getStringUUID()} run function greenlantern:keys/${down ? 'ctrl_on' : 'ctrl_off'}`)
})
