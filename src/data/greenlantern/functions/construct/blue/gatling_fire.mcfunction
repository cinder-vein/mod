energybar value subtract @s greenlantern:blue_lantern ring_charge 3
execute anchored eyes positioned ^-0.3 ^-0.2 ^1.2 run summon palladium:custom_projectile ~ ~ ~ {Tags:["gl_proj_new"],PreventShooterInteraction:1b,Damage:3f,Gravity:0.0f,Size:0.25f,Lifetime:40,DieOnEntityHit:1b,DieOnBlockHit:1b,Appearances:[{Type:"laser",Thickness:0.08f,Color:"#2882FF"}]}
function greenlantern:construct/aim/3_0
playsound minecraft:block.note_block.snare player @a[distance=..16] ~ ~ ~ 0.6 1.8
