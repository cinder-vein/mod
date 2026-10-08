scoreboard players remove @a[scores={gl_spirit=1..}] gl_spirit 1
scoreboard players enable @a gl_check
execute as @a[scores={gl_check=1..}] at @s run function final_lanterns:fl/check_trigger
scoreboard players set @a[scores={gl_check=..-1}] gl_check 0
