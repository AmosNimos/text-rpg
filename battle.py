import ui
from termcolor import colored, cprint
from random import *

line = ui.gen_line("+","-")
def battle(player,opponents,turn):
	battle_menu(player,opponents)

def battle_menu(player,opponents):
	ui.clear()
	print("Select your opponent")
	print(line)
	names=[]
	for x in opponents:
		if x.hp>0:
			names.append(str(x.name))
		else:
			names.append(str(x.name)+" corps")
	print(ui.gen_options(names))
	print(line)
	entry = int(input(">"))
	if opponents[entry].hp>0:
		skills_menu(player,opponents[entry],opponents)
	else:
		print(opponents[entry].name+" is already dead...")

def field(player,opponent):
		ui.clear()
		print(str(randint(0,200)))
		print(line)
		ui.stats(opponent)
		print("")
		print("")
		ui.stats(player)
		print(line)

def skills_menu(player,opponent,opponents):
	turn=0
	field(player,opponent)
	while opponent.hp>0 and player.hp>0:
		if turn == 0:
			print(ui.skills_options(player))
			print(line)
			turn = playermove(player,opponent)
		else:
			entry = opponent.skills[round(randrange(len(opponent.skills)))]
			opponent.use_skill(entry,player,player,opponent)
			turn=0
	if opponent.hp<=0:
		print(opponent.name+" was defeated")
		if len(opponents) > 0:
			battle_menu(player,opponents)
		else:
			print("Victory!")
			exit()
	if player.hp<=0:
		ui.game_over()
		#info name, description, consume, inflict.

def playermove(player,opponent):
	turn=0
	entry = int(input(">"))
	ui.clear()
	field(player,opponent)
	if entry <= len(player.skills):
		player.use_skill(player.skills[entry],opponent,player,opponent)
		turn = 1
	return turn