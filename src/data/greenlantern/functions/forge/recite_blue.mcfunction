scoreboard players set #done gl_tmp 1
tellraw @a[distance=..24] [{"selector":"@s","color":"#2882FF"},{"text":": ","color":"gray"},{"translate":"oath.greenlantern.blue.1","color":"#2882FF","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.blue.2","color":"#2882FF","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.blue.3","color":"#2882FF","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.blue.4","color":"#2882FF","italic":true}]
function greenlantern:forge/request_blue
