tag @s add gl_leader_orange
tag @s add gl_member_orange
function final_lanterns:leader/update_any
tellraw @s [{"text":"You are now a leader of the Orange Lanterns. ","color":"#FA8214"},{"text":"Use the Revoke Ring ability, /trigger gl_roster and /trigger gl_revoke set <id>.","color":"gray"}]
