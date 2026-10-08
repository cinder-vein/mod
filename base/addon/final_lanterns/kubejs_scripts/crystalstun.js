StartupEvents.registry('mob_effect', event => {
    event.create('final_lanterns:crystal_stun')
      .effectTick((entity, lvl) => {
              superpowerUtil.addSuperpower(entity, "final_lanterns:crystalstun")
      }) 
      .color(0xed6ef0)
  }) 