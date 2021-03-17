import ui
from termcolor import colored, cprint
from random import *

line = ui.gen_line("+","-")
def battle(player,opponent,turn):
	#battle_menu(player,opponent)
	skills_menu(player,opponent)

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

def playermove(player,opponent):
	entry = int(input(">"))
	ui.clear()
	field(player,opponent)
	if entry <= len(player.skills):
		player.use_skill(player.skills[entry],opponent,player,opponent)
		player.moves +=1;

def skills_menu(player,opponent):
	field(player,opponent)
	if opponent.hp>0 and player.hp>0:
		if player.turn == True:
			print(ui.skills_options(player))
			print(line)
			playermove(player,opponent)
		else:
			entry = opponent.skills[round(randrange(len(opponent.skills)))]
			opponent.use_skill(entry,player,player,opponent)
			opponent.moves+=1
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

