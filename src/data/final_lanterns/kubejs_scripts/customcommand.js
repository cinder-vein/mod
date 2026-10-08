// Fsang made this Script & Gave me permission to use it.

ServerEvents.commandRegistry(event => {
    const { commands: Commands, arguments: Arguments } = event

    event.register(
        Commands.literal("wormhole_teleport_primary")
            .requires(src => src.hasPermission(2))
            .executes(ctx => {

                let player = ctx.source.player;
                let username = player.getGameProfile().getName();
                let server = ctx.source.getServer();
                let dimension = ctx.source.getLevel().getDimension();
                let x_value = Utils.server.scoreboard.getOrCreatePlayerScore(username, Utils.server.scoreboard.getObjective("Foi1y.Waypoint.A.X")).getScore();
                let y_value = Utils.server.scoreboard.getOrCreatePlayerScore(username, Utils.server.scoreboard.getObjective("Foi1y.Waypoint.A.Y")).getScore();
                let z_value = Utils.server.scoreboard.getOrCreatePlayerScore(username, Utils.server.scoreboard.getObjective("Foi1y.Waypoint.A.Z")).getScore();


                server.runCommandSilent(`execute in ${dimension} as ${username} at @s run tp ${x_value} ${y_value} ${z_value}`);

                return 1;
            })
    );
    event.register(
        Commands.literal("wormhole_teleport_secondary")
            .requires(src => src.hasPermission(2))
            .executes(ctx => {

                let player = ctx.source.player;
                let username = player.getGameProfile().getName();
                let server = ctx.source.getServer();
                let dimension = ctx.source.getLevel().getDimension();
                let x_value = Utils.server.scoreboard.getOrCreatePlayerScore(username, Utils.server.scoreboard.getObjective("Foi1y.Waypoint.B.X")).getScore();
                let y_value = Utils.server.scoreboard.getOrCreatePlayerScore(username, Utils.server.scoreboard.getObjective("Foi1y.Waypoint.B.Y")).getScore();
                let z_value = Utils.server.scoreboard.getOrCreatePlayerScore(username, Utils.server.scoreboard.getObjective("Foi1y.Waypoint.B.Z")).getScore();


                server.runCommandSilent(`execute in ${dimension} as ${username} at @s run tp ${x_value} ${y_value} ${z_value}`);

                return 1;
            })
    );
    })