scoreboard objectives add gl_life dummy
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
scoreboard objectives add gl_reser dummy
scoreboard objectives add gl_recall trigger
scoreboard objectives add gl_rcd dummy
execute unless score #black_floor gl_cfg matches 1.. run scoreboard players set #black_floor gl_cfg 11000
scoreboard objectives add gl_qc0 minecraft.custom:minecraft.animals_bred
scoreboard objectives add gl_qc1 minecraft.custom:minecraft.bell_ring
scoreboard objectives add gl_qc2 minecraft.custom:minecraft.damage_blocked_by_shield
scoreboard objectives add gl_qc3 minecraft.custom:minecraft.damage_dealt
scoreboard objectives add gl_qc4 minecraft.custom:minecraft.damage_taken
scoreboard objectives add gl_qc5 minecraft.custom:minecraft.eat_cake_slice
scoreboard objectives add gl_qc6 minecraft.custom:minecraft.interact_with_brewingstand
scoreboard objectives add gl_qc7 minecraft.custom:minecraft.mob_kills
scoreboard objectives add gl_qc8 minecraft.custom:minecraft.pot_flower
scoreboard objectives add gl_qc9 minecraft.custom:minecraft.raid_win
scoreboard objectives add gl_qc10 minecraft.custom:minecraft.sleep_in_bed
scoreboard objectives add gl_qc11 minecraft.custom:minecraft.sneak_time
scoreboard objectives add gl_qc12 minecraft.custom:minecraft.talked_to_villager
scoreboard objectives add gl_qc13 minecraft.custom:minecraft.traded_with_villager
scoreboard objectives add gl_qc14 minecraft.killed:minecraft.ender_dragon
scoreboard objectives add gl_qc15 minecraft.killed:minecraft.phantom
scoreboard objectives add gl_qc16 minecraft.killed:minecraft.ravager
scoreboard objectives add gl_qc17 minecraft.killed:minecraft.skeleton
scoreboard objectives add gl_qc18 minecraft.killed:minecraft.warden
scoreboard objectives add gl_qc19 minecraft.killed:minecraft.wither
scoreboard objectives add gl_qc20 minecraft.killed:minecraft.zombie
scoreboard objectives add gl_qc21 minecraft.mined:minecraft.ancient_debris
scoreboard objectives add gl_qc22 minecraft.mined:minecraft.deepslate_diamond_ore
scoreboard objectives add gl_qc23 minecraft.mined:minecraft.diamond_ore
scoreboard players set #100 gl_cfg 100
scoreboard players set #10 gl_cfg 10
scoreboard players set #d20 gl_cfg 20
scoreboard players set #d1200 gl_cfg 1200
scoreboard objectives add gl_qn_will dummy
scoreboard objectives add gl_qs_will dummy
scoreboard objectives add gl_qp_will dummy
scoreboard objectives add gl_qd_will dummy
scoreboard objectives add gl_ep_will dummy
scoreboard objectives add gl_el_will dummy
scoreboard objectives add gl_tr_will0 dummy
scoreboard objectives add gl_tr_will1 dummy
scoreboard objectives add gl_tr_will2 dummy
scoreboard objectives add gl_tr_will_quests dummy
scoreboard objectives add gl_tr_will_start dummy
scoreboard objectives add gl_qn_fear dummy
scoreboard objectives add gl_qs_fear dummy
scoreboard objectives add gl_qp_fear dummy
scoreboard objectives add gl_qd_fear dummy
scoreboard objectives add gl_ep_fear dummy
scoreboard objectives add gl_el_fear dummy
scoreboard objectives add gl_tr_fear0 dummy
scoreboard objectives add gl_tr_fear1 dummy
scoreboard objectives add gl_tr_fear_quests dummy
scoreboard objectives add gl_tr_fear_start dummy
scoreboard objectives add gl_qn_rage dummy
scoreboard objectives add gl_qs_rage dummy
scoreboard objectives add gl_qp_rage dummy
scoreboard objectives add gl_qd_rage dummy
scoreboard objectives add gl_ep_rage dummy
scoreboard objectives add gl_el_rage dummy
scoreboard objectives add gl_tr_rage0 dummy
scoreboard objectives add gl_tr_rage1 dummy
scoreboard objectives add gl_tr_rage_quests dummy
scoreboard objectives add gl_tr_rage_start dummy
scoreboard objectives add gl_qn_greed dummy
scoreboard objectives add gl_qs_greed dummy
scoreboard objectives add gl_qp_greed dummy
scoreboard objectives add gl_qd_greed dummy
scoreboard objectives add gl_ep_greed dummy
scoreboard objectives add gl_el_greed dummy
scoreboard objectives add gl_tr_greed0 dummy
scoreboard objectives add gl_tr_greed1 dummy
scoreboard objectives add gl_tr_greed2 dummy
scoreboard objectives add gl_tr_greed3 dummy
scoreboard objectives add gl_tr_greed4 dummy
scoreboard objectives add gl_tr_greed5 dummy
scoreboard objectives add gl_tr_greed6 dummy
scoreboard objectives add gl_tr_greed7 dummy
scoreboard objectives add gl_tr_greed8 dummy
scoreboard objectives add gl_tr_greed9 dummy
scoreboard objectives add gl_tr_greed_quests dummy
scoreboard objectives add gl_tr_greed_start dummy
scoreboard objectives add gl_qn_hope dummy
scoreboard objectives add gl_qs_hope dummy
scoreboard objectives add gl_qp_hope dummy
scoreboard objectives add gl_qd_hope dummy
scoreboard objectives add gl_ep_hope dummy
scoreboard objectives add gl_el_hope dummy
scoreboard objectives add gl_tr_hope0 dummy
scoreboard objectives add gl_tr_hope1 dummy
scoreboard objectives add gl_tr_hope2 dummy
scoreboard objectives add gl_tr_hope3 dummy
scoreboard objectives add gl_tr_hope_quests dummy
scoreboard objectives add gl_tr_hope_start dummy
scoreboard objectives add gl_qn_love dummy
scoreboard objectives add gl_qs_love dummy
scoreboard objectives add gl_qp_love dummy
scoreboard objectives add gl_qd_love dummy
scoreboard objectives add gl_ep_love dummy
scoreboard objectives add gl_el_love dummy
scoreboard objectives add gl_tr_love0 dummy
scoreboard objectives add gl_tr_love1 dummy
scoreboard objectives add gl_tr_love_quests dummy
scoreboard objectives add gl_tr_love_start dummy
scoreboard objectives add gl_qn_compassion dummy
scoreboard objectives add gl_qs_compassion dummy
scoreboard objectives add gl_qp_compassion dummy
scoreboard objectives add gl_qd_compassion dummy
scoreboard objectives add gl_ep_compassion dummy
scoreboard objectives add gl_el_compassion dummy
scoreboard objectives add gl_tr_compassion0 dummy
scoreboard objectives add gl_tr_compassion1 dummy
scoreboard objectives add gl_tr_compassion2 dummy
scoreboard objectives add gl_tr_compassion_quests dummy
scoreboard objectives add gl_tr_compassion_start dummy
scoreboard objectives add gl_qn_death dummy
scoreboard objectives add gl_qs_death dummy
scoreboard objectives add gl_qp_death dummy
scoreboard objectives add gl_qd_death dummy
scoreboard objectives add gl_ep_death dummy
scoreboard objectives add gl_el_death dummy
scoreboard objectives add gl_tr_death0 dummy
scoreboard objectives add gl_tr_death1 dummy
scoreboard objectives add gl_tr_death_quests dummy
scoreboard objectives add gl_tr_death_start dummy
scoreboard players set #span gl_cfg 5001
scoreboard players set #bits gl_cfg 8192
scoreboard players set #60 gl_cfg 60
scoreboard objectives add gl_ent dummy
scoreboard objectives add gl_eser dummy
scoreboard objectives add gl_exo dummy
scoreboard objectives add gl_entity trigger
scoreboard objectives add gl_eofft dummy
scoreboard objectives add gl_lifecd dummy
scoreboard objectives add gl_takeover dummy
scoreboard objectives add gl_ehcd dummy
execute unless score #entities gl_cfg matches 0.. run scoreboard players set #entities gl_cfg 1
scoreboard players add #state_ion gl_ent 0
scoreboard players add #host_ion gl_ent 0
scoreboard players add #ser_ion gl_ent 0
scoreboard players add #seal_ion gl_ent 0
scoreboard objectives add gl_edc_ion dummy
scoreboard players add #state_parallax gl_ent 0
scoreboard players add #host_parallax gl_ent 0
scoreboard players add #ser_parallax gl_ent 0
scoreboard players add #seal_parallax gl_ent 0
scoreboard objectives add gl_edc_parallax dummy
scoreboard players add #state_butcher gl_ent 0
scoreboard players add #host_butcher gl_ent 0
scoreboard players add #ser_butcher gl_ent 0
scoreboard players add #seal_butcher gl_ent 0
scoreboard objectives add gl_edc_butcher dummy
bossbar add final_lanterns:butcher {"text": "The Butcher", "color": "#DC1E23"}
bossbar set final_lanterns:butcher color red
bossbar set final_lanterns:butcher max 400
bossbar set final_lanterns:butcher style notched_10
scoreboard players add #state_ophidian gl_ent 0
scoreboard players add #host_ophidian gl_ent 0
scoreboard players add #ser_ophidian gl_ent 0
scoreboard players add #seal_ophidian gl_ent 0
scoreboard objectives add gl_edc_ophidian dummy
scoreboard players add #state_adara gl_ent 0
scoreboard players add #host_adara gl_ent 0
scoreboard players add #ser_adara gl_ent 0
scoreboard players add #seal_adara gl_ent 0
scoreboard objectives add gl_edc_adara dummy
scoreboard players add #state_predator gl_ent 0
scoreboard players add #host_predator gl_ent 0
scoreboard players add #ser_predator gl_ent 0
scoreboard players add #seal_predator gl_ent 0
scoreboard objectives add gl_edc_predator dummy
scoreboard players add #state_proselyte gl_ent 0
scoreboard players add #host_proselyte gl_ent 0
scoreboard players add #ser_proselyte gl_ent 0
scoreboard players add #seal_proselyte gl_ent 0
scoreboard objectives add gl_edc_proselyte dummy
scoreboard players add #state_life gl_ent 0
scoreboard players add #host_life gl_ent 0
scoreboard players add #ser_life gl_ent 0
scoreboard players add #seal_life gl_ent 0
scoreboard objectives add gl_edc_life dummy
scoreboard players add #state_nekron gl_ent 0
scoreboard players add #host_nekron gl_ent 0
scoreboard players add #ser_nekron gl_ent 0
scoreboard players add #seal_nekron gl_ent 0
scoreboard objectives add gl_edc_nekron dummy
bossbar add final_lanterns:nekron {"text": "Nekron", "color": "#969BAA"}
bossbar set final_lanterns:nekron color white
bossbar set final_lanterns:nekron max 320
bossbar set final_lanterns:nekron style notched_10
scoreboard objectives add gl_lcd dummy
scoreboard objectives add gl_rings dummy
scoreboard objectives add gl_dc1 dummy
scoreboard objectives add gl_dc2 dummy
scoreboard players set #load_ok gl_cfg 1
