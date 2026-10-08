// Final Lanterns: the /lantern admin command, /ring recall, /emotions, and looser chat wordings for calling your
// ring. Loaded by Palladium's KubeJS integration when KubeJS is installed (or copy it into kubejs/server_scripts).
// Without KubeJS the exact phrases still work through Palladium, and the rest is available through /trigger and
// /function final_lanterns:admin/...
const CORPS = ["green", "yellow", "red", "orange", "blue", "violet", "indigo", "white", "black"]
const EMOTIONS = ["will", "fear", "rage", "greed", "hope", "love", "compassion", "death"]
// answered by Palladium itself (exact messages), so the script leaves them alone
const PALLADIUM_PHRASES = ["accept", "black ring come to me", "black ring come to me!", "black ring, come to me", "black ring, come to me!", "blue ring come to me", "blue ring come to me!", "blue ring, come to me", "blue ring, come to me!", "come to me ring", "come to me ring!", "come to me, black ring", "come to me, black ring!", "come to me, blue ring", "come to me, blue ring!", "come to me, green ring", "come to me, green ring!", "come to me, indigo ring", "come to me, indigo ring!", "come to me, orange ring", "come to me, orange ring!", "come to me, red ring", "come to me, red ring!", "come to me, ring", "come to me, ring!", "come to me, sinestro ring", "come to me, sinestro ring!", "come to me, star sapphire ring", "come to me, star sapphire ring!", "come to me, violet ring", "come to me, violet ring!", "come to me, white ring", "come to me, white ring!", "come to me, yellow ring", "come to me, yellow ring!", "decline", "emotional spectrum", "emotions", "final lanterns check", "green ring come to me", "green ring come to me!", "green ring, come to me", "green ring, come to me!", "i accept", "i call my ring", "i call my ring!", "i decline", "i summon my ring", "i summon my ring!", "indigo ring come to me", "indigo ring come to me!", "indigo ring, come to me", "indigo ring, come to me!", "lantern check", "lanterns check", "my emotions", "n", "no", "orange ring come to me", "orange ring come to me!", "orange ring, come to me", "orange ring, come to me!", "red ring come to me", "red ring come to me!", "red ring, come to me", "red ring, come to me!", "return to me, black ring", "return to me, black ring!", "return to me, blue ring", "return to me, blue ring!", "return to me, green ring", "return to me, green ring!", "return to me, indigo ring", "return to me, indigo ring!", "return to me, orange ring", "return to me, orange ring!", "return to me, red ring", "return to me, red ring!", "return to me, ring", "return to me, ring!", "return to me, sinestro ring", "return to me, sinestro ring!", "return to me, star sapphire ring", "return to me, star sapphire ring!", "return to me, violet ring", "return to me, violet ring!", "return to me, white ring", "return to me, white ring!", "return to me, yellow ring", "return to me, yellow ring!", "ring come back", "ring come back!", "ring come to me", "ring come to me!", "ring return to me", "ring return to me!", "ring, come back", "ring, come back!", "ring, come to me", "ring, come to me!", "ring, return to me", "ring, return to me!", "ring, to me", "ring, to me!", "show my emotions", "sinestro ring come to me", "sinestro ring come to me!", "sinestro ring, come to me", "sinestro ring, come to me!", "star sapphire ring come to me", "star sapphire ring come to me!", "star sapphire ring, come to me", "star sapphire ring, come to me!", "violet ring come to me", "violet ring come to me!", "violet ring, come to me", "violet ring, come to me!", "white ring come to me", "white ring come to me!", "white ring, come to me", "white ring, come to me!", "y", "yellow ring come to me", "yellow ring come to me!", "yellow ring, come to me", "yellow ring, come to me!", "yes"]
const ENTITY_KEYS = ["ion", "parallax", "butcher", "ophidian", "adara", "predator", "proselyte", "life", "nekron"]
console.info('[Final Lanterns] KubeJS script loaded: /lantern, /ring and /emotions')

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
  const asPlayer = (ctx, fn) => run(ctx, `execute as ${playerName(ctx)} at @s run function final_lanterns:${fn}`)
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
    .executes(ctx => runSelf(ctx, 'final_lanterns:admin/help'))
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
    .then(Commands.literal('blackfloor').then(Commands.argument('amount', Arguments.INTEGER.create(event)).executes(ctx =>
      run(ctx, `scoreboard players set #black_floor gl_cfg ${Math.max(1, Arguments.INTEGER.getResult(ctx, 'amount'))}`))))
    .then(perPlayer('reroll', 'emotion/reroll'))
    .then(Commands.literal('entity')
      .then(Commands.literal('status').executes(ctx => runSelf(ctx, 'final_lanterns:entity/admin/status')))
      .then(Commands.literal('reset').executes(ctx => runSelf(ctx, 'final_lanterns:entity/admin/reset')))
      .then(Commands.literal('on').executes(ctx => runSelf(ctx, 'final_lanterns:entity/admin/on')))
      .then(Commands.literal('off').executes(ctx => runSelf(ctx, 'final_lanterns:entity/admin/off')))
      .then(Commands.literal('host').then(Commands.argument('player', Arguments.PLAYER.create(event))
        .then(Commands.argument('entity', Arguments.WORD.create(event))
          .suggests((ctx, builder) => { ENTITY_KEYS.forEach(e => builder.suggest(e)); return builder.buildFuture() })
          .executes(ctx => {
            const key = String(Arguments.WORD.getResult(ctx, 'entity')).toLowerCase()
            if (ENTITY_KEYS.indexOf(key) < 0) {
              ctx.source.sendFailure(Text.of(`Unknown entity '${key}'. Use one of: ${ENTITY_KEYS.join(', ')}`))
              return 0
            }
            return asPlayer(ctx, `entity/admin/host/${key}`)
          }))))
      .then(Commands.literal('summon').then(Commands.argument('entity', Arguments.WORD.create(event))
        .suggests((ctx, builder) => { ENTITY_KEYS.forEach(e => builder.suggest(e)); return builder.buildFuture() })
        .executes(ctx => {
          const key = String(Arguments.WORD.getResult(ctx, 'entity')).toLowerCase()
          if (ENTITY_KEYS.indexOf(key) < 0) {
            ctx.source.sendFailure(Text.of(`Unknown entity '${key}'. Use one of: ${ENTITY_KEYS.join(', ')}`))
            return 0
          }
          return runSelf(ctx, `final_lanterns:entity/admin/summon/${key}`)
        }))))
    .then(Commands.literal('check').executes(ctx => runSelf(ctx, 'final_lanterns:check')))
    .then(Commands.literal('enable').executes(ctx => runSelf(ctx, 'final_lanterns:admin/enable')))
    .then(Commands.literal('disable').executes(ctx => runSelf(ctx, 'final_lanterns:admin/disable')))
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
  const corpsArgument = (then) => Commands.argument('corps', Arguments.WORD.create(event))
    .suggests((ctx, builder) => suggestCorps(builder))
    .executes(then)
  event.register(Commands.literal('emotions').executes(ctx => runSelf(ctx, 'final_lanterns:emotion/menu')))
  event.register(Commands.literal('ring')
    .then(Commands.literal('recall')
      .executes(ctx => recall(ctx, null))
      .then(corpsArgument(ctx => recall(ctx, String(Arguments.WORD.getResult(ctx, 'corps')).toLowerCase()))))
  )
})

// Lets the datapack's check ("lantern check") see that this script is loaded.
PlayerEvents.loggedIn(event => {
  event.server.runCommandSilent('scoreboard players set #kubejs gl_cfg 1')
})

// Recall runs as the player (by UUID, so any name works).
const callRing = (server, player, corps) => {
  const fn = corps ? `final_lanterns:recall/request_${corps}` : 'final_lanterns:recall/request'
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

// Call your ring with a phrase. (Typing yes / no to a ring's offer, and the exact phrases, are answered by
// Palladium.)
PlayerEvents.chat(event => {
  const player = event.player
  const server = player.server
  const msg = String(event.message).trim().toLowerCase()
  if (PALLADIUM_PHRASES.indexOf(msg) >= 0) return
  if (isCall(msg)) {
    callRing(server, player, namedCorps(msg))  // the words still show in chat
  }
})
