const POWER_ID = 'final_lanterns:parallax';
const SACRIFICE_ABILITY_ID = 'sacrifice';
const RECOVERY_EFFECT = 'final_lanterns:parallax';
EntityEvents.death(event => {
    const { entity, server } = event;
    if (!entity.isPlayer()) return;
    if (palladium.abilities.hasPower(entity, POWER_ID)) {
        entity.setHealth(1);
        server.runCommandSilent(`effect give ${entity.username} ${RECOVERY_EFFECT} 5 1 true`);
        event.cancel();
    }
});
EntityEvents.hurt(event => {
    const { entity } = event;
    if (!entity.isPlayer()) return;
    if (palladium.abilities.isEnabled(entity, POWER_ID, SACRIFICE_ABILITY_ID)) {
        // If sacrifice is active, cancel all incoming damage.
        event.cancel();
    }
});