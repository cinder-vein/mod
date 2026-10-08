StartupEvents.registry('block', event => {
    event.create('kubejs:egg_of_life', 'basic') // Use 'basic' to render on all sides
        .displayName('§fEgg of Life')
        .soundType('ancient_debris')
        .hardness(0.0)
        .resistance(100.0)
        .lightLevel(1.0) // fully bright
        .model('final_lanterns:block/eggoflife') // applies to all sides
        .defaultCutout() //     if your texture has transparent/glowing parts
        .box(2, 0, 2, 14, 10, 14, true)
})