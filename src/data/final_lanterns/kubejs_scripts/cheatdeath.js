EntityEvents.hurt("minecraft:player",event =>{
    if (event.entity.isPlayer() && abilityUtil.hasPower(event.player, 'final_lanterns:blacklantern')) {
        let damage = event.damage
        let entity = event.entity;
        let entry = event.entity.entry
        let server = event.server;
        let health = entity.health;
        let username = entity.getGameProfile().getName();
        
        let scoreboard = Utils.server.scoreboard;
        let scoreboard_obj = scoreboard.getObjective("Blacklantern.Death.Amount");
        let score = scoreboard.getOrCreatePlayerScore(username, scoreboard_obj);
        let value = score.getScore();
        
        let scoreboard_2 = Utils.server.scoreboard;
        let scoreboard_obj_2 = scoreboard_2.getObjective("Blacklantern.Death.Amount.Max");
        let score_2 = scoreboard.getOrCreatePlayerScore(username, scoreboard_obj_2);
        let value_2 = score_2.getScore();
        
        if (value < value_2) {
        if (damage >= health) {
        server.runCommandSilent(`scoreboard players add ${username} Blacklantern.Death.Amount 1`);
        event.cancel()
        }
        }
    }
})