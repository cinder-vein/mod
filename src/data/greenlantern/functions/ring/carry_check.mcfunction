execute store result score #all gl_tmp run clear @s #greenlantern:lantern_rings 0
execute store result score #bound gl_tmp run clear @s #greenlantern:lantern_rings{gl_bound:1b} 0
execute if score #all gl_tmp > #bound gl_tmp run function greenlantern:ring/carry_scan
