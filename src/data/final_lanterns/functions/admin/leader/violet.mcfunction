tag @s add gl_leader_violet
tag @s add gl_member_violet
function final_lanterns:leader/update_any
tellraw @s [{"text":"You are now a leader of the Star Sapphires. ","color":"#D737DC"},{"text":"Use the Revoke Ring ability, /trigger gl_roster and /trigger gl_revoke set <id>.","color":"gray"}]
