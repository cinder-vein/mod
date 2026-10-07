scoreboard players set #done gl_tmp 1
tellraw @a[distance=..24] [{"selector":"@s","color":"#693CE6"},{"text":": ","color":"gray"},{"translate":"oath.greenlantern.indigo.1","color":"#693CE6","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.indigo.2","color":"#693CE6","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.indigo.3","color":"#693CE6","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.indigo.4","color":"#693CE6","italic":true}]
function greenlantern:forge/request_indigo
