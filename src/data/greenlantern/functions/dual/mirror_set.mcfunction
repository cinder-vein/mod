scoreboard players operation #bits gl_tmp = #sum gl_tmp
execute store success score #set gl_tmp run energybar value set @s greenlantern:spectrum_lantern spectrum_charge 0
execute if score #bits gl_tmp matches 2048.. run energybar value add @s greenlantern:spectrum_lantern spectrum_charge 2048
execute if score #bits gl_tmp matches 2048.. run scoreboard players remove #bits gl_tmp 2048
execute if score #bits gl_tmp matches 1024.. run energybar value add @s greenlantern:spectrum_lantern spectrum_charge 1024
execute if score #bits gl_tmp matches 1024.. run scoreboard players remove #bits gl_tmp 1024
execute if score #bits gl_tmp matches 512.. run energybar value add @s greenlantern:spectrum_lantern spectrum_charge 512
execute if score #bits gl_tmp matches 512.. run scoreboard players remove #bits gl_tmp 512
execute if score #bits gl_tmp matches 256.. run energybar value add @s greenlantern:spectrum_lantern spectrum_charge 256
execute if score #bits gl_tmp matches 256.. run scoreboard players remove #bits gl_tmp 256
execute if score #bits gl_tmp matches 128.. run energybar value add @s greenlantern:spectrum_lantern spectrum_charge 128
execute if score #bits gl_tmp matches 128.. run scoreboard players remove #bits gl_tmp 128
execute if score #bits gl_tmp matches 64.. run energybar value add @s greenlantern:spectrum_lantern spectrum_charge 64
execute if score #bits gl_tmp matches 64.. run scoreboard players remove #bits gl_tmp 64
execute if score #bits gl_tmp matches 32.. run energybar value add @s greenlantern:spectrum_lantern spectrum_charge 32
execute if score #bits gl_tmp matches 32.. run scoreboard players remove #bits gl_tmp 32
execute if score #bits gl_tmp matches 16.. run energybar value add @s greenlantern:spectrum_lantern spectrum_charge 16
execute if score #bits gl_tmp matches 16.. run scoreboard players remove #bits gl_tmp 16
execute if score #bits gl_tmp matches 8.. run energybar value add @s greenlantern:spectrum_lantern spectrum_charge 8
execute if score #bits gl_tmp matches 8.. run scoreboard players remove #bits gl_tmp 8
execute if score #bits gl_tmp matches 4.. run energybar value add @s greenlantern:spectrum_lantern spectrum_charge 4
execute if score #bits gl_tmp matches 4.. run scoreboard players remove #bits gl_tmp 4
execute if score #bits gl_tmp matches 2.. run energybar value add @s greenlantern:spectrum_lantern spectrum_charge 2
execute if score #bits gl_tmp matches 2.. run scoreboard players remove #bits gl_tmp 2
execute if score #bits gl_tmp matches 1.. run energybar value add @s greenlantern:spectrum_lantern spectrum_charge 1
execute if score #bits gl_tmp matches 1.. run scoreboard players remove #bits gl_tmp 1
execute if score #set gl_tmp matches 1 run scoreboard players operation @s gl_dlast = #sum gl_tmp
