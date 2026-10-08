StartupEvents.registry('block', event => {
    event.create('kubejs:centralbatterycore_yellow', 'basic') // Use 'basic' to render on all sides
        .displayName('§eYellow Central Battery Core')
        .soundType('glass')
        .hardness(255.0)
        .resistance(100.0)
        .lightLevel(1.0) // fully bright
        .model('final_lanterns:block/centralbatterycore_yellow') // applies to all sides
        .defaultCutout() // if your texture has transparent/glowing parts
})