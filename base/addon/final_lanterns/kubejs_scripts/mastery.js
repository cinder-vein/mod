StartupEvents.registry('palladium:abilities', (event) => {
    event.create('finallanterns:mastery')
        .addProperty('element', 'string', 'lantern.Level', 'The name of the lanterns mastery LEVEL scoreboard')
        .addProperty('mastery', 'string', 'lantern.Mastery', 'The name of the lanterns mastery SCORE scoreboard')
        .addProperty('masteryMax', 'string', 'lantern.MasteryMax', 'The name of the lanterns mastery MAX SCORE scoreboard')
        .addProperty('base_value', 'integer', 500, 'The base value of this mastery')
        .addProperty('modifier', 'integer', 200, 'Modifier for how much the experience cap increases per level')
        .addProperty('max_level', 'integer', 100, 'The maximum level this mastery can reach')
        .firstTick((entity, entry, holder, enabled) => {
            let base = entry.getPropertyByName('base_value')
            let element = entry.getPropertyByName('element')
            let max = entry.getPropertyByName('masteryMax')
            if (enabled) {
                if (palladium.scoreboard.getScore(entity, max) === 0 && element === 0) {
                    palladium.scoreboard.setScore(entity, max, base)
                }
            }
        })
        .tick((entity, entry, holder, enabled) => {
            let element = entry.getPropertyByName('element')
            let modifier = entry.getPropertyByName('modifier')
            let base = entry.getPropertyByName('base_value')
            let mastery = entry.getPropertyByName('mastery')
            let max = entry.getPropertyByName('masteryMax')
            let max_level = entry.getPropertyByName('max_level')
            let current_level = palladium.scoreboard.getScore(entity, element)
            let prevmax = Math.floor((current_level - 1) * modifier + base)
            let newlevelsubtract = Math.floor(palladium.scoreboard.getScore(entity, mastery) - prevmax)
            let newMax = Math.floor(current_level * modifier + base)
            if (enabled) {
                if (current_level === max_level) return

                else if (palladium.scoreboard.getScore(entity, mastery) > palladium.scoreboard.getScore(entity, max)) {
                    palladium.scoreboard.setScore(entity, mastery, newlevelsubtract)
                    palladium.scoreboard.addScore(entity, element, 1)
                    palladium.scoreboard.setScore(entity, max, newMax)
                }
            }
        })
})