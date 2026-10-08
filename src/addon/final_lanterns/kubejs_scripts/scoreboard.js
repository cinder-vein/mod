//Made by Bosatron04
StartupEvents.registry('palladium:abilities', (event) => {
    event.create('finallanterns:scoreboard_ability')
        .icon(palladium.createItemIcon('minecraft:blaze_rod'))
        .addProperty('score', 'string', 'example_score', 'Name of the scoreboard to modify')
        .addProperty('adjustment_type', 'string', 'add', 'add, subtract or set')
        .addProperty('adjustment_amount', 'integer', 1, 'The amount you want to adjust the score by')
        .addProperty('max_score', 'integer', 10, 'Maximum score allowed (When using ADD mode)')
        .addProperty('min_score', 'integer', 0, 'Minimum score allowed (When using SUBTRACT mode)')

        .tick((entity, entry, holder, enabled) => {
            if (enabled && entity.isPlayer()) {
                let scoreName = entry.getPropertyByName('score');
                let adjustmentType = entry.getPropertyByName('adjustment_type');
                let adjustmentAmount = entry.getPropertyByName('adjustment_amount');
                let max = entry.getPropertyByName('max_score');
                let min = entry.getPropertyByName('min_score');
                if (adjustmentType === 'add' && palladium.scoreboard.getScore(entity, scoreName) + adjustmentAmount <= max) {
                    palladium.scoreboard.addScore(entity, scoreName, adjustmentAmount);
                } 
                else if (adjustmentType === 'subtract' && palladium.scoreboard.getScore(entity, scoreName) - adjustmentAmount >= min) {
                    palladium.scoreboard.subtractScore(entity, scoreName, adjustmentAmount);
                } 
                else if (adjustmentType === 'set') {
                    palladium.scoreboard.setScore(entity, scoreName, adjustmentAmount);
                }
            }
        });
});