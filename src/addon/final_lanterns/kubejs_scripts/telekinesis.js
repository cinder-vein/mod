let $Util = Java.loadClass("net.minecraft.Util");

StartupEvents.registry("palladium:abilities", event => {
    event.create("finallanterns:telekinesis")
        .icon(palladium.createItemIcon("minecraft:player_head"))

        .documentationDescription("Telekinesis: grab blocks and entities and float them in front of you.")

        .addProperty("scrollable", "boolean", false, "For if you intend to use the tele_valchange ability to make this scrollable.")
        .addProperty("damage", "float", 2, "The damage to apply when hitting an entity with a block via telekinesis.")
        .addProperty("range", "integer", 8, "The default range of the ability.")
        .addProperty("strength", "float", 0.8, "The default strength/speed of the telekinesis.")
        .addProperty("particle", "string", "minecraft:enchant", "The ID of the particle you want to summon around the entity.")
        .addProperty("dust", "boolean", true, "Whether or not you'd like to have dust particles around the grabbed entity.")
        .addProperty("other_rgbs", "string", "null", "The rgbs values for the other particle if it is colorable. Values are: red, green, blue, size. (Leave null if not colorable)")
        .addProperty("other_count", "integer", 1, "The number of particles to spawn.")
        .addProperty("other_speed", "integer", 1, "The speed of the particles.")
        .addProperty("dust_rgbs", "string", "1 1 1 1", "The rgbs values for the dust particle if enabled. Values are: red, green, blue, size")
        .addProperty("dust_count", "integer", 1, "The number of particles to spawn.")
        .addProperty("dust_speed", "integer", 1, "The speed of the particles.")
        .addProperty("reset", "boolean", false, "Whether to reset after the ability is disabled.")

        .addUniqueProperty("held_entity", "uuid", $Util.NIL_UUID)
        .addUniqueProperty("cur_range", "integer", 8)
        .addUniqueProperty("cur_strength", "float", 0.8)

        .firstTick((entity, entry, holder, enabled) => {
            const range = entry.getPropertyByName(`scrollable`) == false ? `range` : `cur_range`;

            if (enabled) {
                let rayTrace = entity.rayTrace(entry.getPropertyByName(range), false);

                if (rayTrace.entity != null) {
                    entry.setUniquePropertyByName(`held_entity`, rayTrace.entity.uuid);
                } else if (rayTrace.block != null) {
                    entry.setUniquePropertyByName(`held_entity`, spawnFallingBlock(rayTrace.block).uuid);
                }
            }
        })

        .tick((entity, entry, holder, enabled) => {
            const range = entry.getPropertyByName(`scrollable`) == false ? `range` : `cur_range`;
            const strength = entry.getPropertyByName(`scrollable`) == false ? `strength` : `cur_strength`;
            const rgbs = entry.getPropertyByName(`dust_rgbs`);
            const particle = entry.getPropertyByName(`other_rgbs`) == "null" ? entry.getPropertyByName(`particle`) : entry.getPropertyByName(`particle`) + " " + entry.getPropertyByName(`other_rgbs`)
            let heldEntity = getHeldEntity(entity.level, entry);
            if (heldEntity == null) return;
            let targetPos = entity.getEyePosition().add(entity.getLookAngle().scale(entry.getPropertyByName(range)));
            let boundingBox = entity.getBoundingBox();
            const posX = heldEntity.type == `minecraft:block_display` ? heldEntity.x + 0.5 : heldEntity.x;
            const posY = heldEntity.type == `minecraft:block_display` ? heldEntity.y + 0.5 : heldEntity.y + 1;
            const posZ = heldEntity.type == `minecraft:block_display` ? heldEntity.z + 0.5 : heldEntity.z;

            if (enabled) {
                if (heldEntity.type == `minecraft:block_display`) {
                    boundingBox = AABB.ofSize(heldEntity.position(), 1, 1, 1);
                    targetPos = entity.rayTrace(entry.getPropertyByName(range)).hit ?? targetPos; // absolutely awesome operator
                    heldEntity.setPosition(targetPos.x() - 0.5, targetPos.y() - 0.5, targetPos.z() - 0.5);

                    entity.level.getEntities(heldEntity, boundingBox).forEach(collidedEntity => {
                        if (collidedEntity.living) collidedEntity.attack(entry.getPropertyByName(`damage`));
                    })
                } else {
                    heldEntity.setDeltaMovement(targetPos.subtract(heldEntity.getEyePosition()).scale(entry.getPropertyByName(strength)));
                    heldEntity.resetFallDistance()
                }
                entity.level.sendParticles(
                    particle,
                    posX, posY, posZ,
                    entry.getPropertyByName(`other_count`),
                    boundingBox.getXsize() * 0.65, boundingBox.getYsize() * 0.5, boundingBox.getZsize() * 0.65,
                    entry.getPropertyByName(`other_speed`)
                );

                if (entry.getPropertyByName(`dust`) == true) {
                    entity.level.sendParticles(
                        `minecraft:dust ${rgbs}`,
                        posX, posY, posZ,
                        entry.getPropertyByName(`dust_count`),
                        boundingBox.getXsize() * 0.65, boundingBox.getYsize() * 0.5, boundingBox.getZsize() * 0.65,
                        entry.getPropertyByName(`dust_speed`)
                    );
                }
            }
        })

        .lastTick((entity, entry, holder, enabled) => {
            let heldEntity = getHeldEntity(entity.level, entry);
            if (heldEntity == null) return;

            if (heldEntity.type == `minecraft:block_display`) blockDisplayToBlock(heldEntity);

            entry.setUniquePropertyByName(`held_entity`, $Util.NIL_UUID);
            if (entry.getPropertyByName(`reset`)) {
                entry.setUniquePropertyByName(`cur_range`, entry.getPropertyByName(`range`));
                entry.setUniquePropertyByName(`cur_strength`, entry.getPropertyByName(`strength`));
            }
        });
});

function getHeldEntity(level, entry) {
    let uuid = entry.getPropertyByName(`held_entity`);
    if (uuid == $Util.NIL_UUID) return;
    return getEntity(level, uuid);
}
function getEntity(level, uuid) {
    if (uuid == null || uuid == $Util.NIL_UUID) return null;
    let entities = level.getEntities();
    for (let i = 0; i < entities.size(); i++) {
        if (entities.get(i).uuid.equals(uuid)) {
            return entities.get(i);
        }
    }
}

function spawnFallingBlock(block) {
    let entity = block.level.createEntity(`minecraft:block_display`);
    entity.setPosition(block);
    entity.mergeNbt({ block_state: { Name: block.id, Properties: block.properties } })
    block.set('air');
    entity.spawn();
    return entity;
}
function blockDisplayToBlock(entity) {
    if (entity.type != `minecraft:block_display`) return;
    let block = entity.block;

    if (block.id == `minecraft:bedrock`) block = block.up;
    block.level.destroyBlock(block.pos, true);

    let props = {};
    if (entity.nbt.block_state.Properties != null) for (let [key, value] of Object.entries(entity.nbt.block_state.Properties)) {
        props[key] = value;
    }

    block.set(entity.nbt.block_state.Name, props);
    block.level.markAndNotifyBlock(
        block.pos,
        block.level.getChunk(block.pos),
        block.blockState,
        block.blockState,
        3, // flags: notify neighbors and client
        512 // this includes block update + re-render
    )
    entity.discard();
}