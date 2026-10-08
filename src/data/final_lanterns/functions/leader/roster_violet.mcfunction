tag @s add gl_viewer
tellraw @s [{"text":"Star Sapphires roster (online)","color":"#D737DC","bold":true}]
execute as @a[tag=gl_member_violet] run tellraw @a[tag=gl_viewer] [{"text":"  "},{"selector":"@s"},{"text":"  id ","color":"gray"},{"score":{"name":"@s","objective":"gl_id"},"color":"yellow"}]
tellraw @s [{"text":"Revoke with ","color":"gray"},{"text":"/trigger gl_revoke set <id>","color":"yellow"}]
tag @s remove gl_viewer
