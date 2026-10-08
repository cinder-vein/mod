ServerEvents.tick(event => {
    event.server.entities.forEach(entity => {
        if (entity.type == 'palladium:custom_projectile' && entity.tags.contains('pink')) {
                        let level = entity.level;
            let box = entity.boundingBox.inflate(2);

            level.getEntitiesWithin(box).forEach(mob => {
                if (!mob.isLiving() || mob.isPlayer() || mob.isMonster()) return;

                if (mob.nbt.contains("Age") && mob.nbt.getInt("Age") === 0) {
                    mob.mergeNbt({ InLove: 600 });
                    level.spawnParticles('minecraft:heart', true, mob.x, mob.y + 0.5, mob.z, 0.5, 0.5, 0.5, 5, 0.1);
                }
            });
            entity.kill();
        }
    });
});