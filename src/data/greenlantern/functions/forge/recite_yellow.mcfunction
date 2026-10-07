scoreboard players set #done gl_tmp 1
tellraw @a[distance=..24] [{"selector":"@s","color":"#F5CD1E"},{"text":": ","color":"gray"},{"translate":"oath.greenlantern.yellow.1","color":"#F5CD1E","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.yellow.2","color":"#F5CD1E","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.yellow.3","color":"#F5CD1E","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.yellow.4","color":"#F5CD1E","italic":true}]
function greenlantern:forge/request_yellow
