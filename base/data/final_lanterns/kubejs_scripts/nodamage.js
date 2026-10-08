EntityEvents.hurt("minecraft:player", event => {
    if (!event.entity.isPlayer()) return;

    let player = event.entity;

    // Change `minecraft:resistance` to the effect you want
    if (!player.hasEffect("final_lanterns:corruptedimmortality")) return;

    let damage = Math.floor(event.damage);
    let health = player.health;

    if (damage) {
        player.server.runCommandSilent(`execute as ${player.username} at ${player.username} run particle minecraft:enchant ~ ~ ~ 0.5 1.5 0.5 0 50 normal ${player.username}`);
        event.cancel();
    }
});