scoreboard players operation #target gl_tmp = @s gl_revoke
execute if entity @s[tag=gl_leader_green] run function greenlantern:leader/revoke_id_green
execute if entity @s[tag=gl_leader_yellow] run function greenlantern:leader/revoke_id_yellow
execute if entity @s[tag=gl_leader_red] run function greenlantern:leader/revoke_id_red
execute if entity @s[tag=gl_leader_orange] run function greenlantern:leader/revoke_id_orange
execute if entity @s[tag=gl_leader_blue] run function greenlantern:leader/revoke_id_blue
execute if entity @s[tag=gl_leader_violet] run function greenlantern:leader/revoke_id_violet
execute if entity @s[tag=gl_leader_indigo] run function greenlantern:leader/revoke_id_indigo
execute if entity @s[tag=gl_leader_white] run function greenlantern:leader/revoke_id_white
execute if entity @s[tag=gl_leader_black] run function greenlantern:leader/revoke_id_black
scoreboard players set @s gl_revoke 0
