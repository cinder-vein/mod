StartupEvents.registry('block', event => {
    event.create('yellowlanternbattery') // Create a new block
      .displayName('§eFear Lantern Battery') // Set a custom name
      .soundType('small_amethyst_bud') // Set a material (affects the sounds and some properties)
      .hardness(1.0) // Set hardness (affects mining time)
      .resistance(1.0) // Set resistance (to explosions, etc)
      .requiresTool(false) // Requires a tool or it won't drop (see tags below)
      .tagBlock('minecraft:mineable/axe') //can be mined faster with an axe
      .tagBlock('minecraft:mineable/pickaxe') // or a pickaxe
      .tagBlock('minecraft:needs_iron_tool') // the tool tier must be at least iron
      .lightLevel(0.4)
      .model('final_lanterns:block/yellowlanternbattery')
      .box(4, 0, 5, 12, 14, 11, true)
      .defaultCutout()
  })