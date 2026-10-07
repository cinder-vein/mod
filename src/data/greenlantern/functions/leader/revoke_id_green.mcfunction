tag @s add gl_revoker
execute as @a if score @s gl_id = #target gl_tmp run function greenlantern:leader/revoke_target_green
tag @a remove gl_revoked
tag @s remove gl_revoker
