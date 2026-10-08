execute unless entity @s[tag=gl_eoffer_parallax] run tellraw @s ["",{"text":"Parallax hasn't offered itself to you.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_parallax] unless score #state_parallax gl_ent matches 1 run tellraw @s ["",{"text":"Parallax is gone.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_parallax,tag=gl_host] run tellraw @s ["",{"text":"You already host an entity.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_parallax,tag=!gl_host,scores={gl_ehcd=1..}] run tellraw @s ["",{"text":"No entity will join you yet: you lost one too recently. ","color":"gray"},{"text":"(see your Emotional Spectrum menu)","color":"dark_gray"}]
execute if entity @s[tag=gl_eoffer_parallax,tag=!gl_host,scores={gl_ehcd=..0}] if score #state_parallax gl_ent matches 1 at @s run function final_lanterns:entity/parallax/host
tag @s remove gl_eoffer_parallax
