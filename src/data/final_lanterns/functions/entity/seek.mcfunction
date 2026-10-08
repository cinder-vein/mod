tag @a remove gl_ecand_ion
execute if score #state_ion gl_ent matches 0 as @a[tag=!gl_host,scores={gl_edc_ion=..0,gl_ehcd=..0},gamemode=!spectator] if score @s gl_e_will >= #req100 gl_ent run tag @s add gl_ecand_ion
execute if score #state_ion gl_ent matches 0 as @r[tag=gl_ecand_ion] at @s run function final_lanterns:entity/ion/manifest
tag @a remove gl_ecand_ion
tag @a remove gl_ecand_parallax
execute if score #state_parallax gl_ent matches 0 as @a[tag=!gl_host,scores={gl_edc_parallax=..0,gl_ehcd=..0},gamemode=!spectator] if score @s gl_e_fear >= #req85 gl_ent run tag @s add gl_ecand_parallax
execute if score #state_parallax gl_ent matches 0 as @r[tag=gl_ecand_parallax] at @s run function final_lanterns:entity/parallax/manifest
tag @a remove gl_ecand_parallax
tag @a remove gl_ecand_butcher
execute if score #state_butcher gl_ent matches 0 as @a[tag=!gl_host,scores={gl_edc_butcher=..0,gl_ehcd=..0},gamemode=!spectator] if score @s gl_e_rage >= #req90 gl_ent run tag @s add gl_ecand_butcher
execute if score #state_butcher gl_ent matches 0 as @r[tag=gl_ecand_butcher] at @s run function final_lanterns:entity/butcher/manifest
tag @a remove gl_ecand_butcher
tag @a remove gl_ecand_ophidian
execute if score #state_ophidian gl_ent matches 0 as @a[tag=!gl_host,scores={gl_edc_ophidian=..0,gl_ehcd=..0},gamemode=!spectator] if score @s gl_e_greed >= #req100 gl_ent run tag @s add gl_ecand_ophidian
execute if score #state_ophidian gl_ent matches 0 as @r[tag=gl_ecand_ophidian] at @s run function final_lanterns:entity/ophidian/manifest
tag @a remove gl_ecand_ophidian
tag @a remove gl_ecand_adara
execute if score #state_adara gl_ent matches 0 as @a[tag=!gl_host,scores={gl_edc_adara=..0,gl_ehcd=..0},gamemode=!spectator] if score @s gl_e_hope >= #req100 gl_ent run tag @s add gl_ecand_adara
execute if score #state_adara gl_ent matches 0 as @r[tag=gl_ecand_adara] at @s run function final_lanterns:entity/adara/manifest
tag @a remove gl_ecand_adara
tag @a remove gl_ecand_predator
execute if score #state_predator gl_ent matches 0 as @a[tag=!gl_host,scores={gl_edc_predator=..0,gl_ehcd=..0},gamemode=!spectator] if score @s gl_e_love >= #req85 gl_ent run tag @s add gl_ecand_predator
execute if score #state_predator gl_ent matches 0 as @r[tag=gl_ecand_predator] at @s run function final_lanterns:entity/predator/manifest
tag @a remove gl_ecand_predator
tag @a remove gl_ecand_proselyte
execute if score #state_proselyte gl_ent matches 0 as @a[tag=!gl_host,scores={gl_edc_proselyte=..0,gl_ehcd=..0},gamemode=!spectator] if score @s gl_e_compassion >= #req100 gl_ent run tag @s add gl_ecand_proselyte
execute if score #state_proselyte gl_ent matches 0 as @r[tag=gl_ecand_proselyte] at @s run function final_lanterns:entity/proselyte/manifest
tag @a remove gl_ecand_proselyte
tag @a remove gl_ecand_life
execute if score #state_life gl_ent matches 0 as @a[tag=!gl_host,scores={gl_edc_life=..0,gl_ehcd=..0},gamemode=!spectator] if score @s gl_e_will >= #req100 gl_ent if score @s gl_e_fear >= #req100 gl_ent if score @s gl_e_rage >= #req100 gl_ent if score @s gl_e_greed >= #req100 gl_ent if score @s gl_e_hope >= #req100 gl_ent if score @s gl_e_love >= #req100 gl_ent if score @s gl_e_compassion >= #req100 gl_ent run tag @s add gl_ecand_life
execute if score #state_life gl_ent matches 0 as @r[tag=gl_ecand_life] at @s run function final_lanterns:entity/life/manifest
tag @a remove gl_ecand_life
tag @a remove gl_ecand_nekron
execute if score #state_nekron gl_ent matches 0 as @a[tag=!gl_host,scores={gl_edc_nekron=..0,gl_ehcd=..0},gamemode=!spectator] if score @s gl_e_death >= #req90 gl_ent run tag @s add gl_ecand_nekron
execute if score #state_nekron gl_ent matches 0 as @r[tag=gl_ecand_nekron] at @s run function final_lanterns:entity/nekron/manifest
tag @a remove gl_ecand_nekron
