scoreboard players set #done gl_tmp 1
tellraw @a[distance=..24] [{"selector":"@s","color":"#EBF2FA"},{"text":": ","color":"gray"},{"translate":"oath.greenlantern.white.1","color":"#EBF2FA","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.white.2","color":"#EBF2FA","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.white.3","color":"#EBF2FA","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.white.4","color":"#EBF2FA","italic":true}]
function greenlantern:forge/request_white
