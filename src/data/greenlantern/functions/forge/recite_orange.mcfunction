scoreboard players set #done gl_tmp 1
tellraw @a[distance=..24] [{"selector":"@s","color":"#FA8214"},{"text":": ","color":"gray"},{"translate":"oath.greenlantern.orange.1","color":"#FA8214","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.orange.2","color":"#FA8214","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.orange.3","color":"#FA8214","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.orange.4","color":"#FA8214","italic":true}]
function greenlantern:forge/request_orange
