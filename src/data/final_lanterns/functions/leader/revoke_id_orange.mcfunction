tag @s add gl_revoker
execute as @a if score @s gl_id = #target gl_tmp run function final_lanterns:leader/revoke_target_orange
tag @a remove gl_revoked
tag @s remove gl_revoker
