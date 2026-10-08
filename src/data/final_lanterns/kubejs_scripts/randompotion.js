ServerEvents.commandRegistry(event => {
  const { commands: Commands } = event;

  event.register(
    Commands.literal('randomeffect')
      .requires(source => source.hasPermission(2))
      .executes(ctx => applyChaosRaycast(ctx.source.player))
  );

  function applyChaosRaycast(player) {
    if (!player) return 0;

    const pData = player.persistentData;
    const currentTime = Date.now();
    const cooldownMs = 500;

    if (pData.contains("re_cooldown")) {
      const lastUse = pData.getLong("re_cooldown");
      if (currentTime - lastUse < cooldownMs) {
        const timeLeft = Math.ceil((cooldownMs - (currentTime - lastUse)) / 1000);
        return 0;
      }
    }

    const hitResult = player.rayTrace(32);



    const target = hitResult.entity;

    const possibleEffects = [
      "minecraft:speed", "minecraft:slowness", "minecraft:haste", "minecraft:mining_fatigue",
      "minecraft:strength", "minecraft:weakness", "minecraft:poison", "minecraft:regeneration",
      "minecraft:invisibility", "minecraft:blindness", "minecraft:night_vision", "minecraft:hunger",
      "minecraft:nausea", "minecraft:levitation", "minecraft:slow_falling", "minecraft:glowing",
      "minecraft:wither", "minecraft:instant_damage", "minecraft:instant_health",
      "final_lanterns:after_effects", "final_lanterns:berserker", "final_lanterns:corruptedimmortality",
      "final_lanterns:fear", "final_lanterns:hope_enpowerment"
    ];

    const randomEffectId = possibleEffects[Math.floor(Math.random() * possibleEffects.length)];
    const duration = 100 + Math.floor(Math.random() * 300);
    const amplifier = Math.floor(Math.random() * 4);

    target.potionEffects.add(randomEffectId, duration, amplifier, false, true);
    
    pData.putLong("re_cooldown", currentTime);

    player.level.playSound(null, target.x, target.y, target.z, "minecraft:entity.witch.throw", player.soundSource, 1, 1);
    

    return 1;
  }
});