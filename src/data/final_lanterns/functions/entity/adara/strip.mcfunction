superpower remove final_lanterns:host_adara @s
tag @s remove gl_host_adara
tag @s remove gl_host
scoreboard players set @s gl_ehcd 3600
clear @s #final_lanterns:host_constructs{fl_host:1b}
function final_lanterns:host/adara/release_clear
tag @s remove gl_living_lantern
