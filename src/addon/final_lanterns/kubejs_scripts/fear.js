/** Register effects */
StartupEvents.registry('mob_effect', event => {
    // Register radiation effect
    event.create('final_lanterns:fear')
    .displayName("Yellow Fear")
        // Set a tick event to apply the action
        .effectTick((entity, lvl) => {
            if (!entity.server) return
            entity.server.runCommandSilent(`execute as ${entity.uuid} at @s run superpower add final_lanterns:effects/fear @s`);
        }) 
        .color(Color.BLACK)
        .harmful();
})