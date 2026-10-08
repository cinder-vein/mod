tag @s add gl_revoker
execute as @p[tag=gl_green,tag=!gl_revoker,tag=!gl_leader_green,distance=..8] run function final_lanterns:leader/revoke_target_green
execute unless entity @p[tag=gl_revoked,distance=..8] run tellraw @s [{"text":"No member of your corps is close enough.","color":"gray"}]
tag @a remove gl_revoked
tag @s remove gl_revoker
