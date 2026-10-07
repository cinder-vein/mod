tag @s add gl_leader_indigo
tag @s add gl_member_indigo
function greenlantern:leader/update_any
tellraw @s [{"text":"You are now a leader of the Indigo Tribe. ","color":"#693CE6"},{"text":"Use the Revoke Ring ability, /trigger gl_roster and /trigger gl_revoke set <id>.","color":"gray"}]
