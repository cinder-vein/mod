ServerEvents.commandRegistry(event => {
  const { commands: Commands, arguments: Arguments } = event;
  const SPEED_WARP_DIM = "final_lanterns:djinndesert";

  event.register(
    Commands.literal('djinnwarp')
      .requires(source => source.hasPermission(2))
      .then(
        Commands.literal('in')
          .executes(ctx => warpIn(ctx.source.player))
      )
      .then(
        Commands.literal('out')
          .executes(ctx => warpOut(ctx.source.player))
      )
  );

  function warpIn(player) {
    if (player.level.dimension.toString() === SPEED_WARP_DIM) return 0;

    const pData = player.persistentData;
    pData.putString("sw_return_dim", player.level.dimension.toString());

    const targetX = Math.floor(player.x);
    const targetZ = Math.floor(player.z);
    const targetY = 1;

    teleport(player, SPEED_WARP_DIM, targetX, targetY, targetZ);
    return 1;
  }

  function warpOut(player) {
    if (player.level.dimension.toString() !== SPEED_WARP_DIM) return 0;

    const pData = player.persistentData;
    if (!pData.contains("sw_return_dim")) return 0;

    const returnDim = pData.getString("sw_return_dim");
    const currentX = Math.floor(player.x);
    const currentZ = Math.floor(player.z);

    const safeY = findSafeY(player, returnDim, currentX, currentZ);

    teleport(player, returnDim, currentX, safeY, currentZ);
    
    pData.remove("sw_return_dim");
    return 1;
  }

  function findSafeY(player, dimId, x, z) {
    const server = player.server;
    const targetLevel = server.getLevel(dimId);

    if (!targetLevel) return 100;

    for (let y = 320; y > -64; y--) {
        let block = targetLevel.getBlock(x, y, z);
        let id = block.id.toString();
        
        if (id !== "minecraft:air" && id !== "minecraft:void_air" && id !== "minecraft:cave_air") {
            return y + 1; 
        }
    }
    return 64; 
  }

  function teleport(player, dim, x, y, z) {
    player.server.runCommandSilent(
      `execute in ${dim} run tp ${player.uuid} ${x} ${y} ${z}`
    );
  }
});