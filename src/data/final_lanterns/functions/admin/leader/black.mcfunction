tag @s add gl_leader_black
tag @s add gl_member_black
function final_lanterns:leader/update_any
tellraw @s [{"text":"You are now a leader of the Black Lantern Corps. ","color":"#AAAFBE"},{"text":"Use the Revoke Ring ability, /trigger gl_roster and /trigger gl_revoke set <id>.","color":"gray"}]
