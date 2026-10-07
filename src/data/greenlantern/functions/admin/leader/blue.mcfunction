tag @s add gl_leader_blue
tag @s add gl_member_blue
function greenlantern:leader/update_any
tellraw @s [{"text":"You are now a leader of the Blue Lantern Corps. ","color":"#2882FF"},{"text":"Use the Revoke Ring ability, /trigger gl_roster and /trigger gl_revoke set <id>.","color":"gray"}]
