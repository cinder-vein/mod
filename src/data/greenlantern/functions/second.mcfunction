scoreboard players set #second gl_cfg 0
execute if score #enabled gl_cfg matches 1 as @a run function greenlantern:emotion/feed
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
scoreboard players enable @a gl_recall
scoreboard players enable @a gl_forge
scoreboard players remove @a[scores={gl_fcd=1..}] gl_fcd 1
scoreboard players remove @a[scores={gl_reser=1..}] gl_reser 1
execute as @a[tag=gl_hasid] run function greenlantern:id/verify
tag @a[tag=gl_reser,scores={gl_reser=..0}] remove gl_reser
scoreboard players remove @a[scores={gl_rcd=1..}] gl_rcd 1
function greenlantern:charge/save
execute at @a[tag=gl_yellow] run effect give @e[type=#greenlantern:greed_prey,distance=..8] minecraft:weakness 2 0 true
execute as @a[tag=gl_green,tag=gl_cr_green] if predicate greenlantern:construct_held/green_mainhand run function greenlantern:construct/green/upkeep
execute as @a[tag=gl_green,tag=gl_cr_green] if predicate greenlantern:construct_held/green_offhand run function greenlantern:construct/green/upkeep
execute as @a[tag=gl_green,tag=gl_cr_green,tag=gl_scuba_green] run function greenlantern:construct/green/upkeep
execute as @a[tag=gl_yellow,tag=gl_cr_yellow] if predicate greenlantern:construct_held/yellow_mainhand run function greenlantern:construct/yellow/upkeep
execute as @a[tag=gl_yellow,tag=gl_cr_yellow] if predicate greenlantern:construct_held/yellow_offhand run function greenlantern:construct/yellow/upkeep
execute as @a[tag=gl_yellow,tag=gl_cr_yellow,tag=gl_scuba_yellow] run function greenlantern:construct/yellow/upkeep
execute as @a[tag=gl_red,tag=gl_cr_red] if predicate greenlantern:construct_held/red_mainhand run function greenlantern:construct/red/upkeep
execute as @a[tag=gl_red,tag=gl_cr_red] if predicate greenlantern:construct_held/red_offhand run function greenlantern:construct/red/upkeep
execute as @a[tag=gl_red,tag=gl_cr_red,tag=gl_scuba_red] run function greenlantern:construct/red/upkeep
execute as @a[tag=gl_orange,tag=gl_cr_orange] if predicate greenlantern:construct_held/orange_mainhand run function greenlantern:construct/orange/upkeep
execute as @a[tag=gl_orange,tag=gl_cr_orange] if predicate greenlantern:construct_held/orange_offhand run function greenlantern:construct/orange/upkeep
execute as @a[tag=gl_orange,tag=gl_cr_orange,tag=gl_scuba_orange] run function greenlantern:construct/orange/upkeep
execute as @a[tag=gl_blue,tag=gl_cr_blue] if predicate greenlantern:construct_held/blue_mainhand run function greenlantern:construct/blue/upkeep
execute as @a[tag=gl_blue,tag=gl_cr_blue] if predicate greenlantern:construct_held/blue_offhand run function greenlantern:construct/blue/upkeep
execute as @a[tag=gl_blue,tag=gl_cr_blue,tag=gl_scuba_blue] run function greenlantern:construct/blue/upkeep
execute as @a[tag=gl_violet,tag=gl_cr_violet] if predicate greenlantern:construct_held/violet_mainhand run function greenlantern:construct/violet/upkeep
execute as @a[tag=gl_violet,tag=gl_cr_violet] if predicate greenlantern:construct_held/violet_offhand run function greenlantern:construct/violet/upkeep
execute as @a[tag=gl_violet,tag=gl_cr_violet,tag=gl_scuba_violet] run function greenlantern:construct/violet/upkeep
execute as @a[tag=gl_indigo,tag=gl_cr_indigo] if predicate greenlantern:construct_held/indigo_mainhand run function greenlantern:construct/indigo/upkeep
execute as @a[tag=gl_indigo,tag=gl_cr_indigo] if predicate greenlantern:construct_held/indigo_offhand run function greenlantern:construct/indigo/upkeep
execute as @a[tag=gl_indigo,tag=gl_cr_indigo,tag=gl_scuba_indigo] run function greenlantern:construct/indigo/upkeep
execute as @a[tag=gl_white,tag=gl_cr_white] if predicate greenlantern:construct_held/white_mainhand run function greenlantern:construct/white/upkeep
execute as @a[tag=gl_white,tag=gl_cr_white] if predicate greenlantern:construct_held/white_offhand run function greenlantern:construct/white/upkeep
execute as @a[tag=gl_white,tag=gl_cr_white,tag=gl_scuba_white] run function greenlantern:construct/white/upkeep
execute as @a[tag=gl_black,tag=gl_cr_black] if predicate greenlantern:construct_held/black_mainhand run function greenlantern:construct/black/upkeep
execute as @a[tag=gl_black,tag=gl_cr_black] if predicate greenlantern:construct_held/black_offhand run function greenlantern:construct/black/upkeep
execute as @a[tag=gl_black,tag=gl_cr_black,tag=gl_scuba_black] run function greenlantern:construct/black/upkeep
tag @a remove gl_carry
tag @a[tag=gl_ring] add gl_carry
execute as @a[tag=!gl_carry] store result score @s gl_tmp run clear @s #greenlantern:lantern_rings 0
tag @a[tag=!gl_carry,scores={gl_tmp=1..}] add gl_carry
clear @a[tag=!gl_carry] #greenlantern:constructs
kill @e[type=minecraft:item,nbt={Item:{tag:{gl_construct:1b}}}]
tag @a[tag=gl_scuba_green,tag=!gl_green] remove gl_scuba_green
tag @a[tag=gl_scuba_yellow,tag=!gl_yellow] remove gl_scuba_yellow
tag @a[tag=gl_scuba_red,tag=!gl_red] remove gl_scuba_red
tag @a[tag=gl_scuba_orange,tag=!gl_orange] remove gl_scuba_orange
tag @a[tag=gl_scuba_blue,tag=!gl_blue] remove gl_scuba_blue
tag @a[tag=gl_scuba_violet,tag=!gl_violet] remove gl_scuba_violet
tag @a[tag=gl_scuba_indigo,tag=!gl_indigo] remove gl_scuba_indigo
tag @a[tag=gl_scuba_white,tag=!gl_white] remove gl_scuba_white
tag @a[tag=gl_scuba_black,tag=!gl_black] remove gl_scuba_black
scoreboard players enable @a gl_construct
