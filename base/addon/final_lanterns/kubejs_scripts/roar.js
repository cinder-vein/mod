StartupEvents.registry('palladium:abilities', (event) => {
    event.create('finallanterns:roar')
        .addProperty('distance', 'integer', 10, 'the distance affected')
        .addProperty('speed', 'float', 1, 'the speed. positive values pull, negative values push')
        .firstTick((entity, entry, holder, enabled) => {
            let distance = entry.getPropertyByName('distance')
            let speed = entry.getPropertyByName('speed')
            if (enabled && speed < 0) {
                let targets = entity.level.getEntities(entity, entity.boundingBox.inflate(distance))
                for (let target of targets) {
                    if (target !== entity) {
                        let direction = entity.position().subtract(target.position())
                        let motion = direction.normalize().scale(speed)
                        target.setDeltaMovement(motion)
                        if (target.isPlayer()) {
                            let ClientboundSetEntityMotionPacket = Java.loadClass('net.minecraft.network.protocol.game.ClientboundSetEntityMotionPacket');
                            target.connection.send(new ClientboundSetEntityMotionPacket(target));
                        }
                    }
                }
            }
        })
        .tick((entity, entry, holder, enabled) => {
            let distance = entry.getPropertyByName('distance')
            let speed = entry.getPropertyByName('speed')
            if (enabled && speed > 0) {
                let targets = entity.level.getEntities(entity, entity.boundingBox.inflate(distance))
                for (let target of targets) {
                    if (target !== entity) {
                        let direction = entity.position().subtract(target.position())
                        let motion = direction.normalize().scale(speed)
                        target.setDeltaMovement(motion)
                        if (target.isPlayer()) {
                            let ClientboundSetEntityMotionPacket = Java.loadClass('net.minecraft.network.protocol.game.ClientboundSetEntityMotionPacket');
                            target.connection.send(new ClientboundSetEntityMotionPacket(target));
                        }
                    }
                }
            }
        })
})
//Made by ShadowLegacy557