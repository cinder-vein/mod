scoreboard players set #done gl_tmp 1
tellraw @a[distance=..24] [{"selector":"@s","color":"#2EC846"},{"text":": ","color":"gray"},{"translate":"oath.greenlantern.green.1","color":"#2EC846","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.green.2","color":"#2EC846","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.green.3","color":"#2EC846","italic":true}]
tellraw @a[distance=..24] [{"text":"   "},{"translate":"oath.greenlantern.green.4","color":"#2EC846","italic":true}]
function greenlantern:forge/request_green
