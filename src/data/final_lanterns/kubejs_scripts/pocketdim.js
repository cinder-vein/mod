ServerEvents.commandRegistry(event => {
  const { commands: Commands } = event;

  event.register(
    Commands.literal('pocket')
      .requires(s => s.hasPermission(2))
      .then(Commands.literal('save').executes(ctx => saveArmor(ctx.source.player)))
      .then(Commands.literal('load').executes(ctx => loadArmor(ctx.source.player)))
  );

  function saveArmor(player) {
    let pData = player.persistentData;

    let armorSlots = [36, 37, 38, 39]; 
    let savedArmor = [];
    let inventory = player.inventory;
    let hasItems = false;

    armorSlots.forEach(slotIndex => {
      let item = inventory.getItem(slotIndex);
      if (!item.isEmpty()) {
        hasItems = true;
        savedArmor.push({
          slot: slotIndex,
          id: item.id,
          count: item.count,
          nbt: item.nbt
        });
        
        inventory.setItem(slotIndex, Item.of("minecraft:air"));
      }
    });
    
    pData.put("pocket_inv_armor", savedArmor);

    player.playSound("minecraft:item.armor.equip_diamond");
    return 1;
  }

  function loadArmor(player) {
    let pData = player.persistentData;

    let savedArmor = pData.get("pocket_inv_armor");
    let inventory = player.inventory;

    savedArmor.forEach(savedItem => {
        let itemStack = Item.of(savedItem.id, savedItem.count, savedItem.nbt);
        inventory.setItem(savedItem.slot, itemStack);
    });
    
    pData.remove("pocket_inv_armor");

    player.playSound("minecraft:item.armor.equip_generic");
    return 1;
  }
});