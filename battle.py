import ui
from termcolor import colored, cprint
from random import *
import math
import time

line = ui.gen_line("+","-")

def dist_p(x1,y1,x2,y2):
	dis = round(math.sqrt((x2-x1)**2+(y2-y1)**2))
	return dis


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
		print(line)
		ui.stats(opponent)
		print("")
		distance = dist_p(opponent.x,opponent.y,player.x,player.y)
		print(ui.margin+"Distance <--["+str(distance)+"]-->")
		print("")
		ui.stats(player)
		print(line)

def playermove(player,opponent,entry):
	#entry = int(input(">"))
	ui.clear()
	distance=0
	field(player,opponent)
	if entry <= len(player.skills):
		distance = dist_p(opponent.x,opponent.y,player.x,player.y)
		skill_range = player.skills[entry]["range"]
		if distance<=skill_range:
			player.use_skill(player.skills[entry],opponent,player,opponent)
			player.moves +=1;
		else:
			text = player.skills[entry]["name"]+" miss, "+opponent.name+" out of range"
			ui.delay_text(text,True,True)
			time.sleep(0.25)
			player.moves +=1;

def skills_menu(player,opponent):
	field(player,opponent)
	if opponent.hp>0 and player.hp>0:
		if player.turn == True:
			text,cursor = ui.skills_options(player)
			print(text)
			print(line)
			playermove(player,opponent,cursor)
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

