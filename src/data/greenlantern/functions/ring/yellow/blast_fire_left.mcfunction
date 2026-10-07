execute anchored eyes positioned ^0.35 ^-0.3 ^1.2 run summon palladium:custom_projectile ~ ~ ~ {Tags:["gl_proj_new"],PreventShooterInteraction:1b,Damage:8f,Gravity:0.0f,Size:0.4f,Lifetime:100,DieOnEntityHit:1b,DieOnBlockHit:1b,Appearances:[{Type:"laser",Thickness:0.15f,Color:"#F5CD1E"},{Type:"particles",ParticleType:"minecraft:end_rod",Spread:0.2f}]}
function greenlantern:construct/aim/2_5
playsound minecraft:entity.firework_rocket.blast player @a[distance=..24] ~ ~ ~ 1 1.5
