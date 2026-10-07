energybar value subtract @s greenlantern:green_lantern ring_charge 40
tag @s add gl_user
execute anchored eyes positioned ^ ^ ^1.2 run summon palladium:custom_projectile ~ ~ ~ {Tags:["gl_proj_new"],PreventShooterInteraction:1b,Damage:8f,Gravity:0.0f,Size:0.4f,Lifetime:100,DieOnEntityHit:1b,DieOnBlockHit:1b,Appearances:[{Type:"laser",Thickness:0.15f,Color:"#2EC846"},{Type:"particles",ParticleType:"minecraft:end_rod",Spread:0.2f}]}
function greenlantern:construct/aim/2_5
playsound minecraft:entity.firework_rocket.blast player @a[distance=..24] ~ ~ ~ 1 1.5
tag @s remove gl_user
