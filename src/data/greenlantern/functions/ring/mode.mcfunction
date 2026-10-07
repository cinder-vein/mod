execute store success score #m gl_tmp if entity @s[tag=gl_mode]
execute if score #m gl_tmp matches 1 run tag @s remove gl_mode
execute if score #m gl_tmp matches 0 run tag @s add gl_mode
execute if score #m gl_tmp matches 0 run title @s actionbar [{"text":"Blast mode: ","color":"aqua"},{"text":"Energy Blast and Scan","color":"white"}]
execute if score #m gl_tmp matches 1 run title @s actionbar [{"text":"Beam mode: ","color":"aqua"},{"text":"Beam and Construct Wheel","color":"white"}]
playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 0.5 1.8
