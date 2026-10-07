scoreboard players set #done gl_tmp 1
tellraw @a[distance=..24] [{"selector":"@s","color":"#DC1E23"},{"text":": ","color":"gray"},{"translate":"oath.greenlantern.red.1","color":"#DC1E23","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.red.2","color":"#DC1E23","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.red.3","color":"#DC1E23","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.red.4","color":"#DC1E23","italic":true}]
function greenlantern:forge/request_red
