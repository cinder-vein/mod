// Lantern Corps: /lantern admin command and chat replies to ring offers.
// Loaded by Palladium's KubeJS integration when KubeJS is installed; without KubeJS the
// same features are available through /function greenlantern:admin/... and /trigger.
const CORPS = ["green", "yellow", "red", "orange", "blue", "violet", "indigo", "white", "black"]
const EMOTIONS = ["will", "fear", "rage", "greed", "hope", "love", "compassion", "death"]
const OATHS = {
  "green": "In brightest day, in blackest night, No evil shall escape my sight. Let those who worship evil's might, Beware my power... Green Lantern's light!",
  "yellow": "In blackest day, in brightest night, Beware your fears made into light. Let those who try to stop what's right, Burn like my power... Sinestro's might!",
  "red": "With blood and rage of crimson red, Ripped from a corpse so freshly dead, Together with our hellish hate, We'll burn you all... that is your fate!",
  "orange": "What's mine is mine, and mine, and mine... and mine! And not yours!",
  "blue": "In fearful day, in raging night, With strong hearts full, our souls ignite, When all seems lost in the War of Light, Look to the stars... for hope burns bright!",
  "violet": "For hearts long lost and full of fright, For those alone in blackest night, Accept our ring and join our fight, Love conquers all... with violet light!",
  "indigo": "Tor lowar lan, Abin Sur, Ak wo tauva, Ihla wo nauva, Natromo faan, Dur ak naja, Ono ot vauva, Abin Sur.",
  "white": "From the light of creation, every color of the spectrum, all life, as one, ...shines White!",
  "black": "The Blackest Night falls from the skies, The darkness grows as all light dies, We crave your hearts and your demise, By my black hand, the dead shall rise!"
}

ServerEvents.commandRegistry(event => {
  const { commands: Commands, arguments: Arguments } = event

  const run = (ctx, cmd) => {
    ctx.source.server.runCommandSilent(cmd)
    return 1
  }
  // run a function as the player who typed the command (by UUID), or directly from the console
  const runSelf = (ctx, fn) => {
    const player = ctx.source.player
    return run(ctx, player ? `execute as ${player.getStringUUID()} at @s run function ${fn}` : `function ${fn}`)
  }
  // corps names, filtered by what has been typed
  const suggestCorps = (builder) => {
    const typed = String(builder.getRemaining()).toLowerCase()
    CORPS.forEach(c => { if (c.indexOf(typed) === 0) builder.suggest(c) })
    return builder.buildFuture()
  }
  const playerName = (ctx) => Arguments.PLAYER.getResult(ctx, 'player').getGameProfile().getName()
  const corpsArg = (then) => Commands.argument('corps', Arguments.WORD.create(event))
    .suggests((ctx, builder) => suggestCorps(builder))
    .executes(then)
  const asPlayer = (ctx, fn) => run(ctx, `execute as ${playerName(ctx)} at @s run function greenlantern:${fn}`)
  const checkCorps = (ctx) => {
    const c = String(Arguments.WORD.getResult(ctx, 'corps')).toLowerCase()
    if (CORPS.indexOf(c) < 0) {
      ctx.source.sendFailure(Text.of(`Unknown corps '${c}'. Use one of: ${CORPS.join(', ')}`))
      return null
    }
    return c
  }
  const perCorps = (name, fn) => Commands.literal(name).then(
    Commands.argument('player', Arguments.PLAYER.create(event)).then(corpsArg(ctx => {
      const c = checkCorps(ctx)
      return c ? asPlayer(ctx, `${fn}/${c}`) : 0
    })))
  const perPlayer = (name, fn) => Commands.literal(name).then(
    Commands.argument('player', Arguments.PLAYER.create(event)).executes(ctx => asPlayer(ctx, fn)))

  event.register(Commands.literal('lantern')
    .requires(src => src.hasPermission(2))
    .executes(ctx => runSelf(ctx, 'greenlantern:admin/help'))
    .then(perCorps('give', 'admin/give'))
    .then(perCorps('unbound', 'admin/give_unbound'))
    .then(perCorps('battery', 'admin/battery'))
    .then(perCorps('leader', 'admin/leader'))
    .then(perCorps('unleader', 'admin/unleader'))
    .then(perCorps('remove', 'admin/remove'))
    .then(perCorps('offer', 'admin/offer'))
    .then(perPlayer('removeall', 'admin/remove_all'))
    .then(perPlayer('unbind', 'admin/unbind'))
    .then(perPlayer('reset', 'admin/reset_emotions'))
    .then(perPlayer('cooldowns', 'admin/reset_cooldowns'))
    .then(perPlayer('show', 'admin/show'))
    .then(Commands.literal('emotion').then(Commands.argument('player', Arguments.PLAYER.create(event))
      .then(Commands.argument('emotion', Arguments.WORD.create(event))
        .suggests((ctx, builder) => { EMOTIONS.forEach(e => builder.suggest(e)); return builder.buildFuture() })
        .then(Commands.literal('set').then(Commands.argument('amount', Arguments.INTEGER.create(event)).executes(ctx =>
          run(ctx, `scoreboard players set ${playerName(ctx)} gl_e_${Arguments.WORD.getResult(ctx, 'emotion')} ${Arguments.INTEGER.getResult(ctx, 'amount')}`))))
        .then(Commands.literal('add').then(Commands.argument('amount', Arguments.INTEGER.create(event)).executes(ctx =>
          run(ctx, `scoreboard players add ${playerName(ctx)} gl_e_${Arguments.WORD.getResult(ctx, 'emotion')} ${Arguments.INTEGER.getResult(ctx, 'amount')}`)))))))
    .then(Commands.literal('threshold').then(Commands.argument('amount', Arguments.INTEGER.create(event)).executes(ctx =>
      run(ctx, `scoreboard players set #threshold gl_cfg ${Arguments.INTEGER.getResult(ctx, 'amount')}`))))
    .then(Commands.literal('forging')
      .then(Commands.literal('on').executes(ctx => runSelf(ctx, 'greenlantern:admin/forging_on')))
      .then(Commands.literal('off').executes(ctx => runSelf(ctx, 'greenlantern:admin/forging_off'))))
    .then(Commands.literal('forgecooldown').then(Commands.argument('seconds', Arguments.INTEGER.create(event)).executes(ctx =>
      run(ctx, `scoreboard players set #forge_cd gl_cfg ${Math.max(0, Arguments.INTEGER.getResult(ctx, 'seconds'))}`))))
    .then(Commands.literal('enable').executes(ctx => runSelf(ctx, 'greenlantern:admin/enable')))
    .then(Commands.literal('disable').executes(ctx => runSelf(ctx, 'greenlantern:admin/disable')))
  )

  // /ring recall [corps]: anyone can call their own rings back (no permission needed)
  const recall = (ctx, corps) => {
    const player = ctx.source.player
    if (!player) {
      ctx.source.sendFailure(Text.of('Only players can call their rings.'))
      return 0
    }
    if (corps && CORPS.indexOf(corps) < 0) {
      ctx.source.sendFailure(Text.of(`Unknown corps '${corps}'. Use one of: ${CORPS.join(', ')}`))
      return 0
    }
    callRing(ctx.source.server, player, corps)
    return 1
  }
  // /ring forge [corps]: recite your corps' oath and forge a new ring for a recruit
  const forge = (ctx, corps) => {
    const player = ctx.source.player
    if (!player) {
      ctx.source.sendFailure(Text.of('Only players can forge rings.'))
      return 0
    }
    if (corps && CORPS.indexOf(corps) < 0) {
      ctx.source.sendFailure(Text.of(`Unknown corps '${corps}'. Use one of: ${CORPS.join(', ')}`))
      return 0
    }
    const fn = corps ? `greenlantern:forge/recite_${corps}` : 'greenlantern:forge/recite_any'
    ctx.source.server.runCommandSilent(`execute as ${player.getStringUUID()} at @s run function ${fn}`)
    return 1
  }
  const corpsArgument = (then) => Commands.argument('corps', Arguments.WORD.create(event))
    .suggests((ctx, builder) => suggestCorps(builder))
    .executes(then)
  event.register(Commands.literal('ring')
    .then(Commands.literal('recall')
      .executes(ctx => recall(ctx, null))
      .then(corpsArgument(ctx => recall(ctx, String(Arguments.WORD.getResult(ctx, 'corps')).toLowerCase()))))
    .then(Commands.literal('forge')
      .executes(ctx => forge(ctx, null))
      .then(corpsArgument(ctx => forge(ctx, String(Arguments.WORD.getResult(ctx, 'corps')).toLowerCase()))))
  )
})

// Recall runs as the player (by UUID, so any name works).
const callRing = (server, player, corps) => {
  const fn = corps ? `greenlantern:recall/request_${corps}` : 'greenlantern:recall/request'
  server.runCommandSilent(`execute as ${player.getStringUUID()} at @s run function ${fn}`)
}

// Chat phrases that call your ring. The whole message must be a call (punctuation ignored), so
// ordinary talk about rings never triggers it:
//   "ring, come to me" / "green ring, come back" / "my star sapphire ring, return"
//   "return to me, green ring" / "come back, blue ring"
//   "I summon my ring" / "I call my red ring"      "ring, to me"
// Naming a corps (or, failing that, its emotion) calls only that ring.
const CALLS = [
  /^(?:(?:my|the|o)\s+)?(?:\w+\s+){0,2}ring\s+(?:come|return)(?:\s+back)?(?:\s+(?:to\s+me|here))?(?:\s+now)?$/,
  /^(?:come\s+back|come|return)(?:\s+to\s+me)?\s+(?:(?:my|the)\s+)?(?:\w+\s+){0,2}ring$/,
  /^i\s+(?:summon|call)\s+(?:(?:my|the)\s+)?(?:\w+\s+){0,2}ring(?:\s+to\s+me)?$/,
  /^(?:(?:my|the)\s+)?(?:\w+\s+){0,2}ring\s+to\s+me$/
]
const normalized = (text) => String(text).toLowerCase().replace(/[^a-z ]+/g, ' ').replace(/\s+/g, ' ').trim()
const isCall = (text) => {
  const t = normalized(text)
  return CALLS.some(re => re.test(t))
}
const CORPS_NAMES = {
  green: ['green'], yellow: ['yellow', 'sinestro'], red: ['red'], orange: ['orange'], blue: ['blue'],
  violet: ['violet', 'star sapphire', 'sapphire'], indigo: ['indigo'], white: ['white'], black: ['black']
}
const EMOTION_NAMES = {
  green: ['will', 'willpower'], yellow: ['fear'], red: ['rage'], orange: ['greed', 'avarice'], blue: ['hope'],
  violet: ['love'], indigo: ['compassion'], white: ['life'], black: ['death']
}
const namedIn = (t, names) => {
  let found = null
  CORPS.forEach(c => {
    (names[c] || []).forEach(w => {
      if (!found && (' ' + t + ' ').indexOf(' ' + w + ' ') >= 0) found = c
    })
  })
  return found
}
const namedCorps = (text) => {
  const t = normalized(text)
  return namedIn(t, CORPS_NAMES) || namedIn(t, EMOTION_NAMES)
}

// Speaking your corps' oath forges a new ring. Small slips are fine: the words must match at least
// OATH_MATCH of the oath, in order (punctuation and capitals don't matter).
const OATH_MATCH = 0.8
const oathWords = (text) => String(text).toLowerCase().replace(/[^a-z ]+/g, ' ').split(' ').filter(w => w.length > 0)
const OATH_WORDS = {}
CORPS.forEach(c => { OATH_WORDS[c] = oathWords(OATHS[c]) })
const inOrder = (a, b) => {  // longest common subsequence of two word lists
  let prev = []
  for (let j = 0; j <= b.length; j++) prev.push(0)
  for (let i = 1; i <= a.length; i++) {
    let cur = [0]  // not const: the KubeJS Rhino fork keeps a loop-body const's first value
    for (let j = 1; j <= b.length; j++) {
      cur.push(a[i - 1] === b[j - 1] ? prev[j - 1] + 1 : Math.max(prev[j], cur[j - 1]))
    }
    prev = cur
  }
  return prev[b.length]
}
const spokenOath = (msg) => {
  const words = oathWords(msg)
  let best = null
  let bestScore = 0
  CORPS.forEach(c => {
    const oath = OATH_WORDS[c]
    if (words.length < oath.length * OATH_MATCH) return
    const score = inOrder(words, oath) / oath.length
    if (score > bestScore) { bestScore = score; best = c }
  })
  return bestScore >= OATH_MATCH ? best : null
}

// Answer a ring's offer by typing yes / no in chat, call your ring with a phrase, or forge a ring
// by speaking your oath.
PlayerEvents.chat(event => {
  const player = event.player
  const server = player.server
  const msg = String(event.message).trim().toLowerCase()
  const oath = spokenOath(msg)
  if (oath) {  // the oath stays in chat for everyone to hear
    server.runCommandSilent(`execute as ${player.getStringUUID()} at @s run function greenlantern:forge/request_${oath}`)
    return
  }
  if (isCall(msg)) {
    callRing(server, player, namedCorps(msg))  // the words still show in chat
    return
  }
  if (!player.tags.contains('gl_offer_any')) return
  const name = event.username
  if (['yes', 'y', 'accept', 'i accept'].indexOf(msg) >= 0) {
    server.runCommandSilent(`execute as ${name} at @s run function greenlantern:offer/accept_chat`)
    event.cancel()
  } else if (['no', 'n', 'decline', 'i decline'].indexOf(msg) >= 0) {
    server.runCommandSilent(`execute as ${name} at @s run function greenlantern:offer/decline_chat`)
    event.cancel()
  }
})
