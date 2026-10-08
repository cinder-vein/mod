StartupEvents.registry('palladium:abilities', (event) => {
    event.create('finallanterns:toughlungs')
        .icon(palladium.createItemIcon('palladium:vibranium_circuit'))

        .tick((entity, entry, holder, enabled) => {
            if (enabled) {
                // Prevents the player from accumulating freezing ticks
                entity.setTicksFrozen(0);
                if (entity.airSupply < 300) {
                    entity.airSupply = 300;
                }
            }
        });

});
