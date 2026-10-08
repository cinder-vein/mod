StartupEvents.registry("palladium:abilities", event => {    
    
    event.create("foi1y:ender_chest")
    // Preset icon, can also be changed individually in the power json
        .icon(palladium.createItemIcon('minecraft:ender_chest'))
    // Documentation description
        .documentationDescription('(Made by Fsang18) Ability to create a GUI for opening / closing an ender chest.')
    // Adding a configurable property for the condition that can be changed in the power json
    .tick((entity, entry, holder, enabled) => {
        if (enabled && entity.isPlayer()) {
            // Directly open the ender chest GUI for the player
            entity.openInventoryGUI(entity.enderChestInventory, Component.translatable("container.enderchest"));
        }
    });
    });