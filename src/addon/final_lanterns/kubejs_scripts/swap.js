StartupEvents.registry('palladium:abilities', (event) => {
    event.create('finallanterns:swap_pos')
        .icon(palladium.createItemIcon('minecraft:ender_pearl'))
        .addProperty("max_distance", "float", 15.0, "Maximum range to swap")
        .tick((entity, entry, holder, enabled) => {
            // --- CRASH PREVENTION ---
            // 1. Only run for players
            if (!entity.isPlayer()) return;
            // 2. STOP if we are on the Client (This fixes the "obj is null" crash)
            if (entity.level.isClientSide()) return;

            let data = entity.persistentData;

            // --- LOGIC: Only fire once per activation ---
            // If ability is OFF, reset the lock so we can use it again later
            if (!enabled) {
                if (data.getBoolean("swap_has_fired")) {
                    data.remove("swap_has_fired");
                }
                return;
            }

            // If we already swapped successfully this activation, stop.
            if (data.getBoolean("swap_has_fired")) return;

            // --- RAYCAST LOGIC ---
            const range = entry.getPropertyByName("max_distance");
            const level = entity.level;
            
            // Calculate the ray from eye position
            let viewVec = entity.getLookAngle();
            let eyePos = entity.getEyePosition(1.0);
            let endPos = eyePos.add(viewVec.x * range, viewVec.y * range, viewVec.z * range);

            // Create a search area
            let searchBox = entity.boundingBox.expandTowards(viewVec.x * range, viewVec.y * range, viewVec.z * range).inflate(1.0);

            let target = null;
            let closestDistSq = range * range; 

            // Find the entity blocking the ray
            level.getEntitiesWithin(searchBox).forEach(e => {
                if (e === entity || e.isSpectator()) return; 

                // Check for precise hitbox collision
                let hitResult = e.boundingBox.clip(eyePos, endPos);
                
                if (hitResult.isPresent()) {
                    let distSq = eyePos.distanceToSqr(hitResult.get());
                    if (distSq < closestDistSq) {
                        closestDistSq = distSq;
                        target = e;
                    }
                }
            });

            // --- EXECUTE SWAP ---
            if (target) {
                let pPos = entity.position();
                let tPos = target.position();

                // Swap positions
                entity.teleportTo(tPos.x, tPos.y, tPos.z);
                target.teleportTo(pPos.x, pPos.y, pPos.z);

                // Sound & Feedback
                level.playSound(null, entity.blockPosition(), 'minecraft:entity.enderman.teleport', 'players', 1.0, 1.0);
                entity.tell(Text.green("Swapped with ").append(target.name));

                // Lock the ability so it doesn't swap again instantly
                data.putBoolean("swap_has_fired", true);
            }
        });
});