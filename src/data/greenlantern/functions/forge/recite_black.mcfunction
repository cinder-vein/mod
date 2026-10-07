scoreboard players set #done gl_tmp 1
tellraw @a[distance=..24] [{"selector":"@s","color":"#AAAFBE"},{"text":": ","color":"gray"},{"translate":"oath.greenlantern.black.1","color":"#AAAFBE","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.black.2","color":"#AAAFBE","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.black.3","color":"#AAAFBE","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.black.4","color":"#AAAFBE","italic":true}]
function greenlantern:forge/request_black
