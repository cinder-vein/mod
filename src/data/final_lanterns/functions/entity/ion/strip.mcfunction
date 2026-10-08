superpower remove final_lanterns:host_ion @s
tag @s remove gl_host_ion
tag @s remove gl_host
scoreboard players set @s gl_ehcd 3600
clear @s #final_lanterns:host_constructs{fl_host:1b}
function final_lanterns:host/ion/release_clear
tag @s remove gl_living_lantern
