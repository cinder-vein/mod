energybar value subtract @s greenlantern:yellow_lantern ring_charge 120
scoreboard players set @s gl_cc_missiles 80
tag @s add gl_user
execute anchored eyes positioned ^-0.7 ^0 ^1.2 run summon palladium:custom_projectile ~ ~ ~ {Tags:["gl_proj_new"],PreventShooterInteraction:1b,Damage:6f,Gravity:0.0f,Size:0.4f,Lifetime:80,DieOnEntityHit:1b,DieOnBlockHit:1b,Appearances:[{Type:"laser",Thickness:0.25f,Color:"#F5CD1E"},{Type:"particles",ParticleType:"minecraft:smoke",Spread:0.2f}],ExplosionRadius:1.5f,ExplosionCausesFire:0b,ExplosionBlockInteraction:"keep"}
function greenlantern:construct/aim/1_6
execute anchored eyes positioned ^0 ^0.5 ^1.2 run summon palladium:custom_projectile ~ ~ ~ {Tags:["gl_proj_new"],PreventShooterInteraction:1b,Damage:6f,Gravity:0.0f,Size:0.4f,Lifetime:80,DieOnEntityHit:1b,DieOnBlockHit:1b,Appearances:[{Type:"laser",Thickness:0.25f,Color:"#F5CD1E"},{Type:"particles",ParticleType:"minecraft:smoke",Spread:0.2f}],ExplosionRadius:1.5f,ExplosionCausesFire:0b,ExplosionBlockInteraction:"keep"}
function greenlantern:construct/aim/1_6
execute anchored eyes positioned ^0.7 ^0 ^1.2 run summon palladium:custom_projectile ~ ~ ~ {Tags:["gl_proj_new"],PreventShooterInteraction:1b,Damage:6f,Gravity:0.0f,Size:0.4f,Lifetime:80,DieOnEntityHit:1b,DieOnBlockHit:1b,Appearances:[{Type:"laser",Thickness:0.25f,Color:"#F5CD1E"},{Type:"particles",ParticleType:"minecraft:smoke",Spread:0.2f}],ExplosionRadius:1.5f,ExplosionCausesFire:0b,ExplosionBlockInteraction:"keep"}
function greenlantern:construct/aim/1_6
playsound minecraft:entity.firework_rocket.launch player @a[distance=..24] ~ ~ ~ 1 0.9
playsound minecraft:entity.firework_rocket.launch player @a[distance=..24] ~ ~ ~ 1 1.2
tag @s remove gl_user
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Missile Barrage","color":"#F5CD1E"}]
