import sys
import os
import ui
import name_generator

game_title = name_generator.gen_name()

limit_number_lenght=6
# start
os.system('clear')
ui.main_menu(game_title)



#adversary.append()

##for preview
#player.hp-=60
#player.sp=int(player.sp/2)
#player.max_mp+=50
#player.mp=int(player.max_mp/3)
#enemy2.max_hp=enemy2.max_hp*2
#enemy2.max_hp=enemy2.max_hp-25
#enemy1.max_hp=999999
#enemy1.hp=enemy1.max_hp
#enemy1.max_sp=999999
#enemy1.sp=int(enemy1.max_sp/2)

#battle.battle(player,[enemy1,enemy2],False)