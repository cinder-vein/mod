
NetworkEvents.dataReceived("open_enderchest", (event) => {
    let player = event.player;

    if (!player.isClientSide()) {
    player.openInventoryGUI(player.enderChestInventory, Component.translatable("container.enderchest"));
    }
});
