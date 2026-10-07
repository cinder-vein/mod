scoreboard players add @s gl_e_will 0
scoreboard players add @s gl_e_fear 0
scoreboard players add @s gl_e_rage 0
scoreboard players add @s gl_e_greed 0
scoreboard players add @s gl_e_hope 0
scoreboard players add @s gl_e_love 0
scoreboard players add @s gl_e_compassion 0
scoreboard players add @s gl_e_death 0
scoreboard players operation @s gl_e_will += @s gl_s_will0
scoreboard players operation @s gl_tr_will0 += @s gl_s_will0
scoreboard players set @s gl_s_will0 0
scoreboard players operation @s gl_tmp = @s gl_s_will1
scoreboard players operation @s gl_tmp *= #w2 gl_cfg
scoreboard players operation @s gl_e_will += @s gl_tmp
scoreboard players operation @s gl_tr_will1 += @s gl_tmp
scoreboard players set @s gl_s_will1 0
scoreboard players operation @s gl_e_will += @s gl_s_will2
scoreboard players operation @s gl_tr_will2 += @s gl_s_will2
scoreboard players set @s gl_s_will2 0
scoreboard players operation @s gl_tmp = @s gl_s_fear0
scoreboard players operation @s gl_tmp *= #w600 gl_cfg
scoreboard players operation @s gl_e_fear += @s gl_tmp
scoreboard players operation @s gl_tr_fear0 += @s gl_tmp
scoreboard players set @s gl_s_fear0 0
scoreboard players operation @s gl_e_fear += @s gl_s_fear1
scoreboard players operation @s gl_tr_fear1 += @s gl_s_fear1
scoreboard players set @s gl_s_fear1 0
scoreboard players operation @s gl_e_rage += @s gl_s_rage0
scoreboard players operation @s gl_tr_rage0 += @s gl_s_rage0
scoreboard players set @s gl_s_rage0 0
scoreboard players operation @s gl_tmp = @s gl_s_rage1
scoreboard players operation @s gl_tmp *= #w500 gl_cfg
scoreboard players operation @s gl_e_rage += @s gl_tmp
scoreboard players operation @s gl_tr_rage1 += @s gl_tmp
scoreboard players set @s gl_s_rage1 0
scoreboard players operation @s gl_tmp = @s gl_s_greed0
scoreboard players operation @s gl_tmp *= #w100 gl_cfg
scoreboard players operation @s gl_e_greed += @s gl_tmp
scoreboard players operation @s gl_tr_greed0 += @s gl_tmp
scoreboard players set @s gl_s_greed0 0
scoreboard players operation @s gl_tmp = @s gl_s_greed1
scoreboard players operation @s gl_tmp *= #w20 gl_cfg
scoreboard players operation @s gl_e_greed += @s gl_tmp
scoreboard players operation @s gl_tr_greed1 += @s gl_tmp
scoreboard players set @s gl_s_greed1 0
scoreboard players operation @s gl_tmp = @s gl_s_greed2
scoreboard players operation @s gl_tmp *= #w20 gl_cfg
scoreboard players operation @s gl_e_greed += @s gl_tmp
scoreboard players operation @s gl_tr_greed2 += @s gl_tmp
scoreboard players set @s gl_s_greed2 0
scoreboard players operation @s gl_tmp = @s gl_s_greed3
scoreboard players operation @s gl_tmp *= #w300 gl_cfg
scoreboard players operation @s gl_e_greed += @s gl_tmp
scoreboard players operation @s gl_tr_greed3 += @s gl_tmp
scoreboard players set @s gl_s_greed3 0
scoreboard players operation @s gl_tmp = @s gl_s_greed4
scoreboard players operation @s gl_tmp *= #w300 gl_cfg
scoreboard players operation @s gl_e_greed += @s gl_tmp
scoreboard players operation @s gl_tr_greed4 += @s gl_tmp
scoreboard players set @s gl_s_greed4 0
scoreboard players operation @s gl_tmp = @s gl_s_greed5
scoreboard players operation @s gl_tmp *= #w300 gl_cfg
scoreboard players operation @s gl_e_greed += @s gl_tmp
scoreboard players operation @s gl_tr_greed5 += @s gl_tmp
scoreboard players set @s gl_s_greed5 0
scoreboard players operation @s gl_tmp = @s gl_s_greed6
scoreboard players operation @s gl_tmp *= #w300 gl_cfg
scoreboard players operation @s gl_e_greed += @s gl_tmp
scoreboard players operation @s gl_tr_greed6 += @s gl_tmp
scoreboard players set @s gl_s_greed6 0
scoreboard players operation @s gl_tmp = @s gl_s_greed7
scoreboard players operation @s gl_tmp *= #w50 gl_cfg
scoreboard players operation @s gl_e_greed += @s gl_tmp
scoreboard players operation @s gl_tr_greed7 += @s gl_tmp
scoreboard players set @s gl_s_greed7 0
scoreboard players operation @s gl_tmp = @s gl_s_greed8
scoreboard players operation @s gl_tmp *= #w50 gl_cfg
scoreboard players operation @s gl_e_greed += @s gl_tmp
scoreboard players operation @s gl_tr_greed8 += @s gl_tmp
scoreboard players set @s gl_s_greed8 0
scoreboard players operation @s gl_tmp = @s gl_s_greed9
scoreboard players operation @s gl_tmp *= #w500 gl_cfg
scoreboard players operation @s gl_e_greed += @s gl_tmp
scoreboard players operation @s gl_tr_greed9 += @s gl_tmp
scoreboard players set @s gl_s_greed9 0
scoreboard players operation @s gl_tmp = @s gl_s_hope0
scoreboard players operation @s gl_tmp *= #w5000 gl_cfg
scoreboard players operation @s gl_e_hope += @s gl_tmp
scoreboard players operation @s gl_tr_hope0 += @s gl_tmp
scoreboard players set @s gl_s_hope0 0
scoreboard players operation @s gl_tmp = @s gl_s_hope1
scoreboard players operation @s gl_tmp *= #w200 gl_cfg
scoreboard players operation @s gl_e_hope += @s gl_tmp
scoreboard players operation @s gl_tr_hope1 += @s gl_tmp
scoreboard players set @s gl_s_hope1 0
scoreboard players operation @s gl_tmp = @s gl_s_hope2
scoreboard players operation @s gl_tmp *= #w50 gl_cfg
scoreboard players operation @s gl_e_hope += @s gl_tmp
scoreboard players operation @s gl_tr_hope2 += @s gl_tmp
scoreboard players set @s gl_s_hope2 0
scoreboard players operation @s gl_tmp = @s gl_s_hope3
scoreboard players operation @s gl_tmp /= #w20 gl_cfg
scoreboard players operation @s gl_e_hope += @s gl_tmp
scoreboard players operation @s gl_tr_hope3 += @s gl_tmp
scoreboard players operation @s gl_s_hope3 %= #w20 gl_cfg
scoreboard players operation @s gl_tmp = @s gl_s_love0
scoreboard players operation @s gl_tmp *= #w200 gl_cfg
scoreboard players operation @s gl_e_love += @s gl_tmp
scoreboard players operation @s gl_tr_love0 += @s gl_tmp
scoreboard players set @s gl_s_love0 0
scoreboard players operation @s gl_tmp = @s gl_s_love1
scoreboard players operation @s gl_tmp *= #w50 gl_cfg
scoreboard players operation @s gl_e_love += @s gl_tmp
scoreboard players operation @s gl_tr_love1 += @s gl_tmp
scoreboard players set @s gl_s_love1 0
scoreboard players operation @s gl_tmp = @s gl_s_compassion0
scoreboard players operation @s gl_tmp *= #w25 gl_cfg
scoreboard players operation @s gl_e_compassion += @s gl_tmp
scoreboard players operation @s gl_tr_compassion0 += @s gl_tmp
scoreboard players set @s gl_s_compassion0 0
scoreboard players operation @s gl_tmp = @s gl_s_compassion1
scoreboard players operation @s gl_tmp *= #w100 gl_cfg
scoreboard players operation @s gl_e_compassion += @s gl_tmp
scoreboard players operation @s gl_tr_compassion1 += @s gl_tmp
scoreboard players set @s gl_s_compassion1 0
scoreboard players operation @s gl_tmp = @s gl_s_compassion2
scoreboard players operation @s gl_tmp *= #w20 gl_cfg
scoreboard players operation @s gl_e_compassion += @s gl_tmp
scoreboard players operation @s gl_tr_compassion2 += @s gl_tmp
scoreboard players set @s gl_s_compassion2 0
scoreboard players operation @s gl_tmp = @s gl_s_death0
scoreboard players operation @s gl_tmp *= #w100 gl_cfg
scoreboard players operation @s gl_e_death += @s gl_tmp
scoreboard players operation @s gl_tr_death0 += @s gl_tmp
scoreboard players set @s gl_s_death0 0
scoreboard players operation @s gl_tmp = @s gl_s_death1
scoreboard players operation @s gl_tmp *= #w300 gl_cfg
scoreboard players operation @s gl_e_death += @s gl_tmp
scoreboard players operation @s gl_tr_death1 += @s gl_tmp
scoreboard players set @s gl_s_death1 0
