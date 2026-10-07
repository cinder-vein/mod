tag @s add gl_leader_red
tag @s add gl_member_red
function greenlantern:leader/update_any
tellraw @s [{"text":"You are now a leader of the Red Lantern Corps. ","color":"#DC1E23"},{"text":"Use the Revoke Ring ability, /trigger gl_roster and /trigger gl_revoke set <id>.","color":"gray"}]
