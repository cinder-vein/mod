scoreboard players set #second gl_cfg 0
execute if score #enabled gl_cfg matches 1 as @a run function final_lanterns:emotion/feed
execute if score #enabled gl_cfg matches 1 run function final_lanterns:offer/scan
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
execute as @a[tag=gl_offer_any,scores={gl_offer=..0}] at @s run function final_lanterns:offer/timeout
scoreboard players enable @a[tag=gl_offer_any] gl_accept
scoreboard players enable @a[tag=gl_offer_any] gl_decline
scoreboard players enable @a[tag=gl_leader_any] gl_revoke
scoreboard players enable @a[tag=gl_leader_any] gl_roster
scoreboard players enable @a gl_emotions
scoreboard players enable @a gl_recall
scoreboard players remove @a[scores={gl_reser=1..}] gl_reser 1
execute as @a[tag=gl_hasid] run function final_lanterns:id/verify
execute as @a[tag=gl_hasid,tag=!gl_sersaved] run function final_lanterns:ring/save_serials
tag @a[tag=gl_reser,scores={gl_reser=..0}] remove gl_reser
scoreboard players remove @a[scores={gl_rcd=1..}] gl_rcd 1
execute as @a run function final_lanterns:emotion/quests
scoreboard players operation #req85 gl_ent = #threshold gl_cfg
scoreboard players operation #req90 gl_ent = #threshold gl_cfg
scoreboard players operation #req95 gl_ent = #threshold gl_cfg
scoreboard players operation #req100 gl_ent = #threshold gl_cfg
scoreboard players set #pct gl_ent 100
scoreboard players set #p85 gl_ent 85
scoreboard players operation #req85 gl_ent *= #p85 gl_ent
scoreboard players operation #req85 gl_ent /= #pct gl_ent
scoreboard players set #p90 gl_ent 90
scoreboard players operation #req90 gl_ent *= #p90 gl_ent
scoreboard players operation #req90 gl_ent /= #pct gl_ent
scoreboard players set #p95 gl_ent 95
scoreboard players operation #req95 gl_ent *= #p95 gl_ent
scoreboard players operation #req95 gl_ent /= #pct gl_ent
scoreboard players add @a gl_edc_ion 0
scoreboard players add @a gl_edc_parallax 0
scoreboard players add @a gl_edc_butcher 0
scoreboard players add @a gl_edc_ophidian 0
scoreboard players add @a gl_edc_adara 0
scoreboard players add @a gl_edc_predator 0
scoreboard players add @a gl_edc_proselyte 0
scoreboard players add @a gl_edc_life 0
scoreboard players add @a gl_edc_nekron 0
scoreboard players remove @a[scores={gl_edc_ion=1..}] gl_edc_ion 1
scoreboard players remove @a[scores={gl_edc_parallax=1..}] gl_edc_parallax 1
scoreboard players remove @a[scores={gl_edc_butcher=1..}] gl_edc_butcher 1
scoreboard players remove @a[scores={gl_edc_ophidian=1..}] gl_edc_ophidian 1
scoreboard players remove @a[scores={gl_edc_adara=1..}] gl_edc_adara 1
scoreboard players remove @a[scores={gl_edc_predator=1..}] gl_edc_predator 1
scoreboard players remove @a[scores={gl_edc_proselyte=1..}] gl_edc_proselyte 1
scoreboard players remove @a[scores={gl_edc_life=1..}] gl_edc_life 1
scoreboard players remove @a[scores={gl_edc_nekron=1..}] gl_edc_nekron 1
scoreboard players add #seek gl_ent 1
execute if score #seek gl_ent matches 10.. if score #entities gl_cfg matches 1 run function final_lanterns:entity/seek
execute if score #seek gl_ent matches 10.. run scoreboard players set #seek gl_ent 0
scoreboard players add #minute gl_ent 1
execute if score #minute gl_ent matches 60.. run function final_lanterns:entity/minute
execute if score #minute gl_ent matches 60.. run scoreboard players set #minute gl_ent 0
scoreboard players add @a gl_ehcd 0
scoreboard players remove @a[scores={gl_ehcd=1..}] gl_ehcd 1
function final_lanterns:entity/ion/second
function final_lanterns:entity/parallax/second
function final_lanterns:entity/butcher/second
execute if score #state_butcher gl_ent matches 1 as @e[tag=gl_ent_butcher] at @s run function final_lanterns:entity/butcher/special_clock
function final_lanterns:entity/ophidian/second
function final_lanterns:entity/adara/second
function final_lanterns:entity/predator/second
function final_lanterns:entity/proselyte/second
function final_lanterns:entity/life/second
function final_lanterns:entity/nekron/second
execute if score #state_nekron gl_ent matches 1 as @e[tag=gl_ent_nekron] at @s run function final_lanterns:entity/nekron/special_clock
scoreboard players remove @a[scores={gl_eofft=1..}] gl_eofft 1
tag @a[tag=gl_eoffer_ion,scores={gl_eofft=..0}] remove gl_eoffer_ion
tag @a[tag=gl_eoffer_parallax,scores={gl_eofft=..0}] remove gl_eoffer_parallax
tag @a[tag=gl_eoffer_butcher,scores={gl_eofft=..0}] remove gl_eoffer_butcher
tag @a[tag=gl_eoffer_ophidian,scores={gl_eofft=..0}] remove gl_eoffer_ophidian
tag @a[tag=gl_eoffer_adara,scores={gl_eofft=..0}] remove gl_eoffer_adara
tag @a[tag=gl_eoffer_predator,scores={gl_eofft=..0}] remove gl_eoffer_predator
tag @a[tag=gl_eoffer_proselyte,scores={gl_eofft=..0}] remove gl_eoffer_proselyte
tag @a[tag=gl_eoffer_life,scores={gl_eofft=..0}] remove gl_eoffer_life
tag @a[tag=gl_eoffer_nekron,scores={gl_eofft=..0}] remove gl_eoffer_nekron
scoreboard players enable @a gl_entity
scoreboard players remove @a[scores={gl_lifecd=1..}] gl_lifecd 1
tag @a[tag=gl_host_life,scores={gl_lifecd=..0}] add gl_life_ready
scoreboard players add @a[tag=gl_host_life] gl_lifecd 0
execute as @a[tag=gl_living_lantern,tag=gl_host_ion] at @s run function final_lanterns:host/ion/lantern_pulse
execute as @a[tag=gl_living_lantern,tag=gl_host_parallax] at @s run function final_lanterns:host/parallax/lantern_pulse
execute as @a[tag=gl_living_lantern,tag=gl_host_butcher] at @s run function final_lanterns:host/butcher/lantern_pulse
execute as @a[tag=gl_living_lantern,tag=gl_host_ophidian] at @s run function final_lanterns:host/ophidian/lantern_pulse
execute as @a[tag=gl_living_lantern,tag=gl_host_adara] at @s run function final_lanterns:host/adara/lantern_pulse
execute as @a[tag=gl_living_lantern,tag=gl_host_predator] at @s run function final_lanterns:host/predator/lantern_pulse
execute as @a[tag=gl_living_lantern,tag=gl_host_proselyte] at @s run function final_lanterns:host/proselyte/lantern_pulse
execute as @a[tag=gl_living_lantern,tag=gl_host_life] at @s run function final_lanterns:host/life/lantern_pulse
execute as @a[tag=gl_living_lantern,tag=gl_host_nekron] at @s run function final_lanterns:host/nekron/lantern_pulse
scoreboard players add @a gl_lcd 0
scoreboard players remove @a[scores={gl_lcd=1..}] gl_lcd 1
tag @a[tag=gl_living_lantern,tag=!gl_host] remove gl_living_lantern
execute as @a[tag=gl_dual] run superpower add final_lanterns:spectrum_bond @s
execute as @a[tag=!gl_dual] run superpower remove final_lanterns:spectrum_bond @s
execute as @a[tag=gl_dual,tag=gl_dn_shared_light] run function final_lanterns:bond/shared_light
execute as @a[tag=gl_dual,tag=gl_dn_twin_lanterns] run function final_lanterns:bond/twin_lanterns
tag @a remove gl_dn_shared_light
tag @a remove gl_dn_twin_lanterns
tag @a[tag=gl_prism,tag=!gl_dual] remove gl_prism
superpower add final_lanterns:emotional_spectrum @a
