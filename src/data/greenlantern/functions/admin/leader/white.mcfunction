tag @s add gl_leader_white
tag @s add gl_member_white
function greenlantern:leader/update_any
tellraw @s [{"text":"You are now a leader of the White Lantern Corps. ","color":"#EBF2FA"},{"text":"Use the Revoke Ring ability, /trigger gl_roster and /trigger gl_revoke set <id>.","color":"gray"}]
