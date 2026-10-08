ServerEvents.commandRegistry(event => {
  const { commands: Commands } = event;

  // command prompt /mobswap
  event.register(
    Commands.literal('mobswap')
      .requires(source => source.hasPermission(2)) // this makes it so that only op can use the command
      .executes(ctx => swapWithTarget(ctx.source.player))
  );

  function swapWithTarget(player) {
    if (!player) return 0;

    //this determines the swap distance in blocks
    const hitResult = player.rayTrace(32);


    const targetMob = hitResult.entity;

    const pPos = {
      x: player.x,
      y: player.y,
      z: player.z,
      dim: player.level.dimension,
      yaw: player.yaw,
      pitch: player.pitch
    };

    const mPos = {
      x: targetMob.x,
      y: targetMob.y,
      z: targetMob.z,
      dim: targetMob.level.dimension,
      yaw: targetMob.yaw,
      pitch: targetMob.pitch
    };

    
    player.teleportTo(mPos.dim, mPos.x, mPos.y, mPos.z, pPos.yaw, pPos.pitch);

    targetMob.teleportTo(pPos.dim, pPos.x, pPos.y, pPos.z, mPos.yaw, mPos.pitch);

    
    player.playSound("minecraft:entity.enderman.teleport");
    
    return 1;
  }
});