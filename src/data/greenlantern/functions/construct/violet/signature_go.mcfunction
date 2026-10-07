energybar value subtract @s greenlantern:violet_lantern ring_charge 120
scoreboard players set @s gl_cc_signature 60
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Crystal Spear","color":"#D737DC"}]
tag @s add gl_user
execute anchored eyes positioned ^ ^ ^1.2 run summon palladium:custom_projectile ~ ~ ~ {Tags:["gl_proj_new"],PreventShooterInteraction:1b,Damage:10f,Gravity:0.0f,Size:0.4f,Lifetime:80,DieOnEntityHit:1b,DieOnBlockHit:1b,Appearances:[{Type:"laser",Thickness:0.2f,Color:"#D737DC"},{Type:"particles",ParticleType:"minecraft:end_rod",Spread:0.2f}],CommandOnEntityHit:"effect give @e[distance=..2.5,type=!minecraft:item,type=!minecraft:marker] minecraft:slowness 5 255 true"}
function greenlantern:construct/aim/2_2
playsound minecraft:block.amethyst_cluster.break player @a[distance=..24] ~ ~ ~ 1 0.8
playsound minecraft:entity.arrow.shoot player @a[distance=..24] ~ ~ ~ 1 0.6
tag @s remove gl_user
