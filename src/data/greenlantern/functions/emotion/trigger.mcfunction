scoreboard players operation #v gl_tmp = @s gl_emotions
scoreboard players set @s gl_emotions 0
scoreboard players enable @s gl_emotions
execute unless score #v gl_tmp matches 11..18 run function greenlantern:emotion/menu
execute if score #v gl_tmp matches 11 run function greenlantern:emotion/page/will
execute if score #v gl_tmp matches 12 run function greenlantern:emotion/page/fear
execute if score #v gl_tmp matches 13 run function greenlantern:emotion/page/rage
execute if score #v gl_tmp matches 14 run function greenlantern:emotion/page/greed
execute if score #v gl_tmp matches 15 run function greenlantern:emotion/page/hope
execute if score #v gl_tmp matches 16 run function greenlantern:emotion/page/love
execute if score #v gl_tmp matches 17 run function greenlantern:emotion/page/compassion
execute if score #v gl_tmp matches 18 run function greenlantern:emotion/page/death
