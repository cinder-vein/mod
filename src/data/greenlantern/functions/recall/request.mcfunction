execute if score @s gl_rcd matches 1.. run tellraw @s [{"text":"Your ring is still answering your last call. Try again in ","color":"gray"},{"score":{"name":"@s","objective":"gl_rcd"},"color":"white"},{"text":" s.","color":"gray"}]
execute unless score @s gl_rcd matches 1.. run function greenlantern:recall/all
