scoreboard players set #second gl_cfg 0
execute if score #enabled gl_cfg matches 1 as @a run function greenlantern:emotion/feed
execute as @a at @s if data entity @s ForgeCaps."curios:inventory" run function #greenlantern:curios_check
execute if score #enabled gl_cfg matches 1 run function greenlantern:offer/scan
scoreboard players remove @a[scores={gl_cd_green=1..}] gl_cd_green 1
scoreboard players remove @a[scores={gl_cd_yellow=1..}] gl_cd_yellow 1
scoreboard players remove @a[scores={gl_cd_red=1..}] gl_cd_red 1
scoreboard players remove @a[scores={gl_cd_orange=1..}] gl_cd_orange 1
scoreboard players remove @a[scores={gl_cd_blue=1..}] gl_cd_blue 1
scoreboard players remove @a[scores={gl_cd_violet=1..}] gl_cd_violet 1
scoreboard players remove @a[scores={gl_cd_indigo=1..}] gl_cd_indigo 1
scoreboard players remove @a[scores={gl_cd_white=1..}] gl_cd_white 1
scoreboard players remove @a[scores={gl_cd_black=1..}] gl_cd_black 1
scoreboard players remove @a[tag=gl_offer_any] gl_offer 1
execute as @a[tag=gl_offer_any,scores={gl_offer=..0}] at @s run function greenlantern:offer/timeout
scoreboard players enable @a[tag=gl_offer_any] gl_accept
scoreboard players enable @a[tag=gl_offer_any] gl_decline
scoreboard players enable @a[tag=gl_leader_any] gl_revoke
scoreboard players enable @a[tag=gl_leader_any] gl_roster
scoreboard players enable @a gl_emotions
function greenlantern:charge/save
