tag @s add gl_revoker
execute as @p[tag=gl_indigo,tag=!gl_revoker,distance=..8] run function greenlantern:leader/revoke_target_indigo
execute unless entity @p[tag=gl_revoked,distance=..8] run tellraw @s [{"text":"No member of your corps is close enough.","color":"gray"}]
tag @a remove gl_revoked
tag @s remove gl_revoker
