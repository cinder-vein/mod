# Only trigger if holding the custom item
execute if data entity @s {SelectedItem:{id:"final_lanterns:red_trident"}} run function final_lanterns:shoot
