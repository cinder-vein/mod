tag @s add gl_leader_green
tag @s add gl_member_green
function greenlantern:leader/update_any
tellraw @s [{"text":"You are now a leader of the Green Lantern Corps. ","color":"#2EC846"},{"text":"Use the Revoke Ring ability, /trigger gl_roster and /trigger gl_revoke set <id>.","color":"gray"}]
