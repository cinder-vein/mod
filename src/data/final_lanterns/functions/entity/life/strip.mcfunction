superpower remove final_lanterns:host_life @s
tag @s remove gl_host_life
tag @s remove gl_host
scoreboard players set @s gl_ehcd 3600
clear @s #final_lanterns:host_constructs{fl_host:1b}
function final_lanterns:host/life/release_clear
tag @s remove gl_living_lantern
