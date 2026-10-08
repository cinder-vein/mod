StartupEvents.registry('mob_effect', event => {
    event.create('final_lanterns:willpower_overdrive')
      .effectTick((entity, lvl) => {
              entity.potionEffects.add("minecraft:regeneration",5,lvl,false, false)
              entity.potionEffects.add("minecraft:strength",5,lvl,false, false)
              entity.potionEffects.add("minecraft:haste",5,lvl,false, false)
              entity.potionEffects.add("minecraft:speed",5,lvl,false, false)
      }) 
      .color(0x4CBB17)
  }) 