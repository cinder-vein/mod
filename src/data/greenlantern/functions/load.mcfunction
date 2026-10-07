scoreboard objectives add gl_life dummy
scoreboard objectives add gl_bkills totalKillCount
scoreboard objectives add gl_k_zombie minecraft.killed:minecraft.zombie
scoreboard objectives add gl_k_husk minecraft.killed:minecraft.husk
scoreboard objectives add gl_k_drowned minecraft.killed:minecraft.drowned
scoreboard objectives add gl_k_skeleton minecraft.killed:minecraft.skeleton
scoreboard objectives add gl_k_stray minecraft.killed:minecraft.stray
scoreboard objectives add gl_k_wither_skeleton minecraft.killed:minecraft.wither_skeleton
scoreboard objectives add gl_k_spider minecraft.killed:minecraft.spider
scoreboard objectives add gl_k_cave_spider minecraft.killed:minecraft.cave_spider
scoreboard objectives add gl_k_enderman minecraft.killed:minecraft.enderman
scoreboard objectives add gl_k_pillager minecraft.killed:minecraft.pillager
scoreboard objectives add gl_k_vindicator minecraft.killed:minecraft.vindicator
scoreboard objectives add gl_k_blaze minecraft.killed:minecraft.blaze
scoreboard objectives add gl_k_zombified_piglin minecraft.killed:minecraft.zombified_piglin
scoreboard objectives add gl_k_piglin_brute minecraft.killed:minecraft.piglin_brute
scoreboard objectives add gl_hoard dummy
team add gl_greed
team modify gl_greed displayName {"text": "Greed Constructs", "color": "gold"}
team modify gl_greed color gold
team modify gl_greed friendlyFire false
scoreboard objectives add gl_s_zombie dummy
scoreboard objectives add gl_s_husk dummy
scoreboard objectives add gl_s_drowned dummy
scoreboard objectives add gl_s_skeleton dummy
scoreboard objectives add gl_s_stray dummy
scoreboard objectives add gl_s_wither_skeleton dummy
scoreboard objectives add gl_s_spider dummy
scoreboard objectives add gl_s_cave_spider dummy
scoreboard objectives add gl_s_enderman dummy
scoreboard objectives add gl_s_pillager dummy
scoreboard objectives add gl_s_vindicator dummy
scoreboard objectives add gl_s_blaze dummy
scoreboard objectives add gl_s_zombified_piglin dummy
scoreboard objectives add gl_s_piglin_brute dummy
scoreboard objectives add gl_dead dummy
team add gl_dead
team modify gl_dead displayName {"text": "Black Lantern Revenants", "color": "dark_gray"}
team modify gl_dead color dark_gray
team modify gl_dead friendlyFire false
scoreboard objectives add gl_d_zombie dummy
scoreboard objectives add gl_d_husk dummy
scoreboard objectives add gl_d_drowned dummy
scoreboard objectives add gl_d_skeleton dummy
scoreboard objectives add gl_d_stray dummy
scoreboard objectives add gl_d_wither_skeleton dummy
scoreboard objectives add gl_d_spider dummy
scoreboard objectives add gl_d_cave_spider dummy
scoreboard objectives add gl_d_enderman dummy
scoreboard objectives add gl_d_pillager dummy
scoreboard objectives add gl_d_vindicator dummy
scoreboard objectives add gl_d_blaze dummy
scoreboard objectives add gl_d_zombified_piglin dummy
scoreboard objectives add gl_d_piglin_brute dummy
scoreboard objectives add gl_ch_green dummy
scoreboard objectives add gl_ch_yellow dummy
scoreboard objectives add gl_ch_red dummy
scoreboard objectives add gl_ch_orange dummy
scoreboard objectives add gl_ch_blue dummy
scoreboard objectives add gl_ch_violet dummy
scoreboard objectives add gl_ch_indigo dummy
scoreboard objectives add gl_ch_white dummy
scoreboard objectives add gl_ch_black dummy
scoreboard objectives add gl_ok dummy
scoreboard objectives add gl_t_green dummy
scoreboard objectives add gl_t_yellow dummy
scoreboard objectives add gl_t_red dummy
scoreboard objectives add gl_t_orange dummy
scoreboard objectives add gl_t_blue dummy
scoreboard objectives add gl_t_violet dummy
scoreboard objectives add gl_t_indigo dummy
scoreboard objectives add gl_t_white dummy
scoreboard objectives add gl_t_black dummy
scoreboard objectives add gl_id dummy
scoreboard objectives add gl_tmp dummy
scoreboard objectives add gl_cfg dummy
scoreboard objectives add gl_offer dummy
scoreboard objectives add gl_accept trigger
scoreboard objectives add gl_decline trigger
scoreboard objectives add gl_revoke trigger
scoreboard objectives add gl_roster trigger
scoreboard objectives add gl_emotions trigger
execute unless score #threshold gl_cfg matches 1.. run scoreboard players set #threshold gl_cfg 20000
execute unless score #enabled gl_cfg matches 0.. run scoreboard players set #enabled gl_cfg 1
execute unless score #second gl_cfg matches 0.. run scoreboard players set #second gl_cfg 0
scoreboard objectives add gl_cd_green dummy
scoreboard objectives add gl_cd_yellow dummy
scoreboard objectives add gl_cd_red dummy
scoreboard objectives add gl_cd_orange dummy
scoreboard objectives add gl_cd_blue dummy
scoreboard objectives add gl_cd_violet dummy
scoreboard objectives add gl_cd_indigo dummy
scoreboard objectives add gl_cd_white dummy
scoreboard objectives add gl_cd_black dummy
scoreboard objectives add gl_e_will dummy
scoreboard objectives add gl_s_will0 minecraft.custom:minecraft.damage_taken
scoreboard objectives add gl_s_will1 minecraft.custom:minecraft.damage_blocked_by_shield
scoreboard players set #w2 gl_cfg 2
scoreboard objectives add gl_s_will2 minecraft.custom:minecraft.damage_absorbed
scoreboard objectives add gl_e_fear dummy
scoreboard objectives add gl_s_fear0 minecraft.custom:minecraft.deaths
scoreboard players set #w600 gl_cfg 600
scoreboard objectives add gl_s_fear1 minecraft.custom:minecraft.sneak_time
scoreboard objectives add gl_e_rage dummy
scoreboard objectives add gl_s_rage0 minecraft.custom:minecraft.damage_dealt
scoreboard objectives add gl_s_rage1 playerKillCount
scoreboard players set #w500 gl_cfg 500
scoreboard objectives add gl_e_greed dummy
scoreboard objectives add gl_s_greed0 minecraft.custom:minecraft.traded_with_villager
scoreboard players set #w100 gl_cfg 100
scoreboard objectives add gl_s_greed1 minecraft.custom:minecraft.open_chest
scoreboard players set #w20 gl_cfg 20
scoreboard objectives add gl_s_greed2 minecraft.custom:minecraft.open_barrel
scoreboard players set #w20 gl_cfg 20
scoreboard objectives add gl_s_greed3 minecraft.mined:minecraft.diamond_ore
scoreboard players set #w300 gl_cfg 300
scoreboard objectives add gl_s_greed4 minecraft.mined:minecraft.deepslate_diamond_ore
scoreboard players set #w300 gl_cfg 300
scoreboard objectives add gl_s_greed5 minecraft.mined:minecraft.emerald_ore
scoreboard players set #w300 gl_cfg 300
scoreboard objectives add gl_s_greed6 minecraft.mined:minecraft.deepslate_emerald_ore
scoreboard players set #w300 gl_cfg 300
scoreboard objectives add gl_s_greed7 minecraft.mined:minecraft.gold_ore
scoreboard players set #w50 gl_cfg 50
scoreboard objectives add gl_s_greed8 minecraft.mined:minecraft.deepslate_gold_ore
scoreboard players set #w50 gl_cfg 50
scoreboard objectives add gl_s_greed9 minecraft.mined:minecraft.ancient_debris
scoreboard players set #w500 gl_cfg 500
scoreboard objectives add gl_e_hope dummy
scoreboard objectives add gl_s_hope0 minecraft.custom:minecraft.raid_win
scoreboard players set #w5000 gl_cfg 5000
scoreboard objectives add gl_s_hope1 minecraft.custom:minecraft.sleep_in_bed
scoreboard players set #w200 gl_cfg 200
scoreboard objectives add gl_s_hope2 minecraft.custom:minecraft.bell_ring
scoreboard players set #w50 gl_cfg 50
scoreboard objectives add gl_s_hope3 minecraft.custom:minecraft.play_time
scoreboard players set #w20 gl_cfg 20
scoreboard objectives add gl_e_love dummy
scoreboard objectives add gl_s_love0 minecraft.custom:minecraft.animals_bred
scoreboard players set #w200 gl_cfg 200
scoreboard objectives add gl_s_love1 minecraft.custom:minecraft.eat_cake_slice
scoreboard players set #w50 gl_cfg 50
scoreboard objectives add gl_e_compassion dummy
scoreboard objectives add gl_s_compassion0 minecraft.custom:minecraft.talked_to_villager
scoreboard players set #w25 gl_cfg 25
scoreboard objectives add gl_s_compassion1 minecraft.custom:minecraft.pot_flower
scoreboard players set #w100 gl_cfg 100
scoreboard objectives add gl_s_compassion2 minecraft.custom:minecraft.fill_cauldron
scoreboard players set #w20 gl_cfg 20
scoreboard objectives add gl_e_death dummy
scoreboard objectives add gl_s_death0 totalKillCount
scoreboard players set #w100 gl_cfg 100
scoreboard objectives add gl_s_death1 minecraft.custom:minecraft.deaths
scoreboard players set #w300 gl_cfg 300
scoreboard players set #2 gl_cfg 2
execute unless score #serial gl_cfg matches 1.. run scoreboard players set #serial gl_cfg 0
scoreboard objectives add gl_ser_green dummy
scoreboard objectives add gl_ser_yellow dummy
scoreboard objectives add gl_ser_red dummy
scoreboard objectives add gl_ser_orange dummy
scoreboard objectives add gl_ser_blue dummy
scoreboard objectives add gl_ser_violet dummy
scoreboard objectives add gl_ser_indigo dummy
scoreboard objectives add gl_ser_white dummy
scoreboard objectives add gl_ser_black dummy
scoreboard objectives add gl_recall trigger
scoreboard objectives add gl_rcd dummy
scoreboard objectives add gl_forge trigger
scoreboard objectives add gl_fcd dummy
execute unless score #forge gl_cfg matches 0.. run scoreboard players set #forge gl_cfg 1
execute unless score #forge_cd gl_cfg matches 0.. run scoreboard players set #forge_cd gl_cfg 300
scoreboard objectives add gl_hurt minecraft.custom:minecraft.damage_taken
scoreboard objectives add gl_construct trigger
scoreboard objectives add gl_slotinit dummy
scoreboard objectives add gl_gat dummy
scoreboard objectives add gl_cfgslot dummy
scoreboard objectives add gl_cfgcat dummy
scoreboard objectives add gl_slot1 dummy
scoreboard objectives add gl_slot2 dummy
scoreboard objectives add gl_slot3 dummy
scoreboard objectives add gl_slot4 dummy
scoreboard objectives add gl_slot5 dummy
scoreboard objectives add gl_cc_sword dummy
scoreboard objectives add gl_cc_sword_shield dummy
scoreboard objectives add gl_cc_mace dummy
scoreboard objectives add gl_cc_axe dummy
scoreboard objectives add gl_cc_fist dummy
scoreboard objectives add gl_cc_slam dummy
scoreboard objectives add gl_cc_blast dummy
scoreboard objectives add gl_cc_gatling dummy
scoreboard objectives add gl_cc_missiles dummy
scoreboard objectives add gl_cc_cannon dummy
scoreboard objectives add gl_cc_shield dummy
scoreboard objectives add gl_cc_barrier dummy
scoreboard objectives add gl_cc_cage dummy
scoreboard objectives add gl_cc_dome dummy
scoreboard objectives add gl_cc_blocks dummy
scoreboard objectives add gl_cc_scuba dummy
scoreboard objectives add gl_cc_drill dummy
scoreboard objectives add gl_cc_bridge dummy
scoreboard objectives add gl_cc_scan dummy
scoreboard objectives add gl_cc_signature dummy
