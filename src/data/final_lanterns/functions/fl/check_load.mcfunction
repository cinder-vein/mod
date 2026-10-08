scoreboard objectives add gl_cfg dummy
scoreboard objectives add gl_check trigger
scoreboard objectives add gl_spirit dummy
scoreboard objectives add gl_tmp dummy
scoreboard players set #load_ok gl_cfg 0
scoreboard players set #ticks gl_cfg 0
scoreboard players set #seconds gl_cfg 0
execute unless score #kubejs gl_cfg matches 0.. run scoreboard players set #kubejs gl_cfg 0
