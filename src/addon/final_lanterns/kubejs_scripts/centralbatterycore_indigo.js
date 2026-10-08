StartupEvents.registry('block', event => {
    event.create('kubejs:centralbatterycore_indigo', 'basic') // Use 'basic' to render on all sides
        .displayName('§5Indigo Central Battery Core')
        .soundType('glass')
        .hardness(255.0)
        .resistance(100.0)
        .lightLevel(1.0) // fully bright
        .model('final_lanterns:block/centralbatterycore_indigo') // applies to all sides
        .defaultCutout() // if your texture has transparent/glowing parts
})