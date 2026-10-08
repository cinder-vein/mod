tag @s add gl_leader_yellow
tag @s add gl_member_yellow
function final_lanterns:leader/update_any
tellraw @s [{"text":"You are now a leader of the Sinestro Corps. ","color":"#F5CD1E"},{"text":"Use the Revoke Ring ability, /trigger gl_roster and /trigger gl_revoke set <id>.","color":"gray"}]
