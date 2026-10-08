BlockEvents.broken(event => {
    // Check if the block broken is "final_lanterns:egg"
    if (event.block.id === 'final_lanterns:eggoflife') {
        // Get the player who broke the block
        let player = event.player;

        // Run the commands as the player who broke the block
        event.server.runCommandSilent(`execute as ${player.uuid} at ${player.uuid} run function final_lanterns:white_ritual/rune_summon`)
    }
});
