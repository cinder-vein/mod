energybar value subtract @s greenlantern:green_lantern ring_charge 150
scoreboard players set @s gl_cc_cannon 100
tag @s add gl_user
execute anchored eyes positioned ^ ^ ^1.6 run summon palladium:custom_projectile ~ ~ ~ {Tags:["gl_proj_new"],PreventShooterInteraction:1b,Damage:16f,Gravity:0.01f,Size:1.0f,Lifetime:120,DieOnEntityHit:1b,DieOnBlockHit:1b,ExplosionRadius:3.0f,ExplosionCausesFire:0b,ExplosionBlockInteraction:"keep",Appearances:[{Type:"item",Item:{id:"greenlantern:construct_ball",Count:1b,tag:{CustomModelData:1}}},{Type:"particles",ParticleType:"minecraft:end_rod",Spread:0.5f}]}
function greenlantern:construct/aim/1_4
playsound minecraft:entity.generic.explode player @a[distance=..24] ~ ~ ~ 1 1.6
playsound minecraft:entity.firework_rocket.blast player @a[distance=..24] ~ ~ ~ 1 0.6
tag @s remove gl_user
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Cannon","color":"#2EC846"}]
