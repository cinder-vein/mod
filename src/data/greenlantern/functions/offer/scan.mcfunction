scoreboard players add @a gl_cd_green 0
scoreboard players add @a gl_cd_yellow 0
scoreboard players add @a gl_cd_red 0
scoreboard players add @a gl_cd_orange 0
scoreboard players add @a gl_cd_blue 0
scoreboard players add @a gl_cd_violet 0
scoreboard players add @a gl_cd_indigo 0
scoreboard players add @a gl_cd_white 0
scoreboard players add @a gl_cd_black 0
execute as @a[gamemode=survival,tag=!gl_offer_any,tag=!gl_member_green,scores={gl_cd_green=..0}] if score @s gl_e_will >= #threshold gl_cfg run function greenlantern:offer/start_green
execute as @a[gamemode=survival,tag=!gl_offer_any,tag=!gl_member_yellow,scores={gl_cd_yellow=..0}] if score @s gl_e_fear >= #threshold gl_cfg run function greenlantern:offer/start_yellow
execute as @a[gamemode=survival,tag=!gl_offer_any,tag=!gl_member_red,scores={gl_cd_red=..0}] if score @s gl_e_rage >= #threshold gl_cfg run function greenlantern:offer/start_red
execute as @a[gamemode=survival,tag=!gl_offer_any,tag=!gl_member_orange,scores={gl_cd_orange=..0}] if score @s gl_e_greed >= #threshold gl_cfg run function greenlantern:offer/start_orange
execute as @a[gamemode=survival,tag=!gl_offer_any,tag=!gl_member_blue,scores={gl_cd_blue=..0}] if score @s gl_e_hope >= #threshold gl_cfg run function greenlantern:offer/start_blue
execute as @a[gamemode=survival,tag=!gl_offer_any,tag=!gl_member_violet,scores={gl_cd_violet=..0}] if score @s gl_e_love >= #threshold gl_cfg run function greenlantern:offer/start_violet
execute as @a[gamemode=survival,tag=!gl_offer_any,tag=!gl_member_indigo,scores={gl_cd_indigo=..0}] if score @s gl_e_compassion >= #threshold gl_cfg run function greenlantern:offer/start_indigo
execute as @a[gamemode=survival,tag=!gl_offer_any,tag=!gl_member_white,scores={gl_cd_white=..0}] if score @s gl_e_will >= #threshold gl_cfg if score @s gl_e_fear >= #threshold gl_cfg if score @s gl_e_rage >= #threshold gl_cfg if score @s gl_e_greed >= #threshold gl_cfg if score @s gl_e_hope >= #threshold gl_cfg if score @s gl_e_love >= #threshold gl_cfg if score @s gl_e_compassion >= #threshold gl_cfg run function greenlantern:offer/start_white
execute as @a[gamemode=survival,tag=!gl_offer_any,tag=!gl_member_black,scores={gl_cd_black=..0}] if score @s gl_e_death >= #threshold gl_cfg run function greenlantern:offer/start_black
