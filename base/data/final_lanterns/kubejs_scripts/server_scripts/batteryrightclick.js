BlockEvents.rightClicked('kubejs:greenlanternbattery', event => {

    if (!event.server) return; // Ensure only server-side execution
    if (event.hand.name() !== 'MAIN_HAND') return; // Ensures only main-hand execution


    const player = event.player;

    if (abilityUtil.hasPower(player, 'final_lanterns:greenlantern')) {
        player.runCommandSilent('function final_lanterns:greenlanternoath');
        event.cancel();
    }
});

BlockEvents.rightClicked('kubejs:corruptedfatebattery', event => {

    if (!event.server) return; // Ensure only server-side execution
    if (event.hand.name() !== 'MAIN_HAND') return; // Ensures only main-hand execution


    const player = event.player;

    if (abilityUtil.hasPower(player, 'final_lanterns:corruptedfate')) {
        player.runCommandSilent('function final_lanterns:corruptedfateoath');
        event.cancel();
    }
});

BlockEvents.rightClicked('kubejs:yellowlanternbattery', event => {

    if (!event.server) return; // Ensure only server-side execution
    if (event.hand.name() !== 'MAIN_HAND') return; // Ensures only main-hand execution


    const player = event.player;

    if (abilityUtil.hasPower(player, 'final_lanterns:yellowlantern')) {
        player.runCommandSilent('function final_lanterns:yellowlanternoath');
        event.cancel();
    }
});

BlockEvents.rightClicked('kubejs:bluelanternbattery', event => {

    if (!event.server) return; // Ensure only server-side execution
    if (event.hand.name() !== 'MAIN_HAND') return; // Ensures only main-hand execution


    const player = event.player;

    if (abilityUtil.hasPower(player, 'final_lanterns:bluelantern')) {
        player.runCommandSilent('function final_lanterns:bluelanternoath');
        event.cancel();
    }
});

BlockEvents.rightClicked('kubejs:redlanternbattery', event => {

    if (!event.server) return; // Ensure only server-side execution
    if (event.hand.name() !== 'MAIN_HAND') return; // Ensures only main-hand execution


    const player = event.player;

    if (abilityUtil.hasPower(player, 'final_lanterns:redlantern')) {
        player.runCommandSilent('function final_lanterns:redlanternoath');
        event.cancel();
    }
});

BlockEvents.rightClicked('kubejs:orangelanternbattery', event => {

    if (!event.server) return; // Ensure only server-side execution
    if (event.hand.name() !== 'MAIN_HAND') return; // Ensures only main-hand execution


    const player = event.player;

    if (abilityUtil.hasPower(player, 'final_lanterns:orangelantern')) {
        player.runCommandSilent('function final_lanterns:orangelanternoath');
        event.cancel();
    }
});

BlockEvents.rightClicked('kubejs:pinklanternbattery', event => {

    if (!event.server) return; // Ensure only server-side execution
    if (event.hand.name() !== 'MAIN_HAND') return; // Ensures only main-hand execution


    const player = event.player;

    if (abilityUtil.hasPower(player, 'final_lanterns:pinklantern')) {
        player.runCommandSilent('function final_lanterns:pinklanternoath');
        event.cancel();
    }
});

BlockEvents.rightClicked('kubejs:goldlanternbattery', event => {

    if (!event.server) return; // Ensure only server-side execution
    if (event.hand.name() !== 'MAIN_HAND') return; // Ensures only main-hand execution


    const player = event.player;

    if (abilityUtil.hasPower(player, 'final_lanterns:goldlantern')) {
        player.runCommandSilent('function final_lanterns:goldlanternoath');
        event.cancel();
    }
});

BlockEvents.rightClicked('kubejs:graylanternbattery', event => {

    if (!event.server) return; // Ensure only server-side execution
    if (event.hand.name() !== 'MAIN_HAND') return; // Ensures only main-hand execution


    const player = event.player;

    if (abilityUtil.hasPower(player, 'final_lanterns:sorrowlantern')) {
        player.runCommandSilent('function final_lanterns:sorrowlanternoath')
        event.cancel();
    }
});

BlockEvents.rightClicked('kubejs:whitelanternbattery', event => {

    if (!event.server) return; // Ensure only server-side execution
    if (event.hand.name() !== 'MAIN_HAND') return; // Ensures only main-hand execution


    const player = event.player;

    if (abilityUtil.hasPower(player, 'final_lanterns:whitelantern')) {
        player.runCommandSilent('function final_lanterns:whitelanternoath');
        event.cancel();
    }
});

BlockEvents.rightClicked('kubejs:greenlanternbattery', event => {

    if (!event.server) return; // Ensure only server-side execution
    if (event.hand.name() !== 'MAIN_HAND') return; // Ensures only main-hand execution


    const player = event.player;

    if (abilityUtil.hasPower(player, 'final_lanterns:starheart')) {
        player.runCommandSilent('function final_lanterns:starheartoath');
        event.cancel();
    }
});