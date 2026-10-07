// Lantern Corps: /lantern admin command and chat replies to ring offers.
// Loaded by Palladium's KubeJS integration when KubeJS is installed; without KubeJS the
// same features are available through /function greenlantern:admin/... and /trigger.
const CORPS = ["green", "yellow", "red", "orange", "blue", "violet", "indigo", "white", "black"]
const EMOTIONS = ["will", "fear", "rage", "greed", "hope", "love", "compassion", "death"]

ServerEvents.commandRegistry(event => {
  const { commands: Commands, arguments: Arguments } = event

  const run = (ctx, cmd) => {
    ctx.source.server.runCommandSilent(cmd)
    return 1
  }
  const playerName = (ctx) => Arguments.PLAYER.getResult(ctx, 'player').getGameProfile().getName()
  const corpsArg = (then) => Commands.argument('corps', Arguments.WORD.create(event))
    .suggests((ctx, builder) => { CORPS.forEach(c => builder.suggest(c)); return builder.buildFuture() })
    .executes(then)
  const asPlayer = (ctx, fn) => run(ctx, `execute as ${playerName(ctx)} at @s run function greenlantern:${fn}`)
  const checkCorps = (ctx) => {
    const c = Arguments.WORD.getResult(ctx, 'corps')
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
    .executes(ctx => run(ctx, `execute as ${ctx.source.textName} run function greenlantern:admin/help`))
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
    .then(Commands.literal('enable').executes(ctx => run(ctx, `execute as ${ctx.source.textName} run function greenlantern:admin/enable`)))
    .then(Commands.literal('disable').executes(ctx => run(ctx, `execute as ${ctx.source.textName} run function greenlantern:admin/disable`)))
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
  event.register(Commands.literal('ring')
    .then(Commands.literal('recall')
      .executes(ctx => recall(ctx, null))
      .then(Commands.argument('corps', Arguments.WORD.create(event))
        .suggests((ctx, builder) => { CORPS.forEach(c => builder.suggest(c)); return builder.buildFuture() })
        .executes(ctx => recall(ctx, Arguments.WORD.getResult(ctx, 'corps')))))
  )
})

// Recall runs as the player (by UUID, so any name works).
const callRing = (server, player, corps) => {
  const fn = corps ? `greenlantern:recall/request_${corps}` : 'greenlantern:recall/request'
  server.runCommandSilent(`execute as ${player.getStringUUID()} at @s run function ${fn}`)
}

// Chat phrases that call your ring: "ring", plus a calling word ("ring, come to me", "return to me,
// green ring", "I summon my ring"). Naming a corps or its emotion calls only that ring.
const CALL_WORDS = /\b(come|return|recall|summon|back|answer|to me)\b/
const CORPS_WORDS = {
  green: ['green', 'will', 'willpower'], yellow: ['yellow', 'sinestro', 'fear'], red: ['red', 'rage'],
  orange: ['orange', 'greed', 'avarice'], blue: ['blue', 'hope'], violet: ['violet', 'star sapphire', 'sapphire', 'love'],
  indigo: ['indigo', 'compassion'], white: ['white', 'life'], black: ['black', 'death']
}
const namedCorps = (msg) => {
  let found = null
  CORPS.forEach(c => {
    if (found) return
    const words = CORPS_WORDS[c] || [c]
    words.forEach(w => {
      if (!found && new RegExp('\\b' + w + '\\b').test(msg)) found = c
    })
  })
  return found
}

// Answer a ring's offer by typing yes / no in chat, or call your ring with a phrase.
PlayerEvents.chat(event => {
  const player = event.player
  const server = player.server
  const msg = String(event.message).trim().toLowerCase()
  if (/\bring\b/.test(msg) && CALL_WORDS.test(msg)) {
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
