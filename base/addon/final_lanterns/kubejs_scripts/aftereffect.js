StartupEvents.registry('mob_effect', event => {
    event.create('final_lanterns:after_effects')
      .effectTick((entity, lvl) => {
              entity.potionEffects.add("minecraft:nausea",5,lvl,false, false)
              entity.potionEffects.add("minecraft:weakness",5,lvl,false, false)
              entity.potionEffects.add("minecraft:slowness",2,lvl,false, false)
              entity.potionEffects.add("minecraft:hunger",1,lvl,false, false)
      }) 
      .color(0x4CBB17)
  }) 