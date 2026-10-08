StartupEvents.registry('block', event => {
    event.create('final_lanterns:templealtar', 'basic') // Use 'basic' to render on all sides
        .displayName('§fAltar')
        .soundType('ancient_debris')
        .hardness(255.0)
        .resistance(100.0)
        .lightLevel(1.0) // fully bright
        .model('final_lanterns:block/altar') // applies to all sides
        .defaultCutout() //     if your texture has transparent/glowing parts
        .box(2, 0, 2, 14, 10, 14, true)
})