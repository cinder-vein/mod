execute store result score #all gl_tmp run clear @s #final_lanterns:lantern_rings 0
execute store result score #bound gl_tmp run clear @s #final_lanterns:lantern_rings{gl_bound:1b} 0
execute if score #all gl_tmp > #bound gl_tmp run function final_lanterns:ring/carry_scan
