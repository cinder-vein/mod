scoreboard players set #done gl_tmp 1
tellraw @a[distance=..24] [{"selector":"@s","color":"#D737DC"},{"text":": ","color":"gray"},{"translate":"oath.greenlantern.violet.1","color":"#D737DC","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.violet.2","color":"#D737DC","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.violet.3","color":"#D737DC","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.violet.4","color":"#D737DC","italic":true}]
function greenlantern:forge/request_violet
