PlayerEvents.inventoryChanged(event => {
    let player = event.entity;
            if (
                !abilityUtil.hasPower(player, 'final_lanterns:greenlantern') ||
                !abilityUtil.hasPower(player, 'final_lanterns:indigolantern') ||
                !abilityUtil.hasPower(player, 'final_lanterns:whitelantern')
            ) {
                player.runCommandSilent(`clear @s #final_lanterns:willpower_tools`);
            }

            if (
                !abilityUtil.hasPower(player, 'final_lanterns:sorrowlantern')
            ) {
                player.runCommandSilent(`clear @s #final_lanterns:sorrow_tools`);
            }

            if (
                !abilityUtil.hasPower(player, 'final_lanterns:pridelantern')
            ) {
                player.runCommandSilent(`clear @s #final_lanterns:pride_tools`);
            }
    });
