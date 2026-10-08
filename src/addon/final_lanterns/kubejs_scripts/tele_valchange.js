StartupEvents.registry("palladium:abilities", (event) => {
	event.create("finallanterns:tele_valchange")
		.icon(palladium.createItemIcon("minecraft:stick"))

		.documentationDescription("Let's you change the values of the telekinesis ability. (Does nothing on it's own)")

		.addProperty("property", "string", "both", "What property you want to change. (Values: range, strength, both, reset)")
		.addProperty("max_range", "integer", 10, "The maximum distance away from the player for this ability to work.")
		.addProperty("max_strength", "float", 1, "The maximum strength for this ability.")
		.addProperty("min_range", "integer", 3, "The minimum distance away from the player for this ability to work.")
		.addProperty("min_strength", "float", 0.3, "The minimum strength for this ability.")
		.addProperty("range", "integer", 1, "The value to change by every time this ability is activated.")
		.addProperty("strength", "float", -0.1, "The value to change by every time this ability is activated.")
		.addProperty("power", "string", null, "ID of the power where the desired ability is located, leave null for current power.")
		.addProperty("ability", "string", "null", "ID of the desired ability")

		.firstTick((entity, entry, holder, enabled) => {
			if (enabled) {
				const power = entry.getPropertyByName(`power`) ?? holder.power.id;
				const ability = entry.getPropertyByName(`ability`);
				const telekinesis = palladium.abilities.getEntry(entity, power, ability);
				const value = entry.getPropertyByName(`property`) == `range` ? entry.getPropertyByName(`range`) : entry.getPropertyByName(`strength`);
				const curRange = telekinesis.getPropertyByName(`cur_range`);
				const curStrength = telekinesis.getPropertyByName(`cur_strength`);
				const curValue = entry.getPropertyByName(`property`) == `range` ? curRange : curStrength;
				const increment_range = entry.getPropertyByName(`range`) > 0 ? curRange < entry.getPropertyByName(`max_range`) : curRange > entry.getPropertyByName(`min_range`);
				const increment_strength = entry.getPropertyByName(`strength`) > 0 ? curStrength < entry.getPropertyByName(`max_strength`) : curStrength > entry.getPropertyByName(`min_strength`);
				const increment_either = entry.getPropertyByName(`property`) == `range` ? increment_range : increment_strength;

				if (entry.getPropertyByName(`property`) == `reset`) {
					telekinesis.setUniquePropertyByName(`cur_range`, telekinesis.getPropertyByName(`range`));
					telekinesis.setUniquePropertyByName(`cur_strength`, telekinesis.getPropertyByName(`strength`));

					return;
				}

				if (entry.getPropertyByName(`property`) == `both`) {
					if (increment_range) {
						telekinesis.setUniquePropertyByName(`cur_range`, curRange + entry.getPropertyByName(`range`));
					}
					if (increment_strength) {
						telekinesis.setUniquePropertyByName(`cur_strength`, curStrength + entry.getPropertyByName(`strength`));
					}
				} else if (increment_either) {
					telekinesis.setUniquePropertyByName(entry.getPropertyByName(`property`), curValue + value);
				}
			}
		});
});