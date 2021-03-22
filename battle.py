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
		render=""
		render+=line+"\n"
		render+=ui.stats(opponent)+"\n"
		render+="\n"
		distance = dist_p(opponent.x,opponent.y,player.x,player.y)
		render+=ui.margin+"Distance <--["+str(distance)+"]-->\n"
		render+="\n"
		render+=ui.stats(player)+"\n"
		render+=line
		return render

def playermove(player,opponent,entry):
	#entry = int(input(">"))
	ui.clear()
	distance=0
	print(field(player,opponent))
	distance = dist_p(opponent.x,opponent.y,player.x,player.y)
	skill_range = entry["range"]
	if distance<=skill_range:
		player.use_skill(entry,opponent,player,opponent)
		player.moves +=1;
	else:
		text = entry["name"]+" miss, "+opponent.name+" out of range"
		ui.delay_text(text,True,True)
		time.sleep(0.25)
		player.moves +=1;


def skills_menu(player,opponent):
	ui.clear()
	head=""
	head = field(player,opponent)
	print(head)
	if opponent.hp>0 and player.hp>0:
		if player.turn == True:
			skills_names = []
			for skill in player.skills:
				skills_names.append(skill["name"])
			entry = ui.menu(player.skills,skills_names,head)
			#text = ui.skills_options(player)
			print(line)
			playermove(player,opponent,entry)
		else:
			entry = opponent.skills[round(randrange(len(opponent.skills)))]
			opponent.use_skill(entry,player,player,opponent)
			opponent.moves+=1
	if opponent.hp<=0:
		ui.clear()
		print(field(player,opponent))
		text = opponent.name+" was defeated"
		ui.delay_text(text,True,True)
		time.sleep(0.25)
		opponent.death()
	if player.hp<=0:
		ui.clear()
		print(field(player,opponent))
		text = player.name+" was defeated"
		ui.delay_text(text,True,True)
		time.sleep(0.25)
		player.death()
		#info name, description, consume, inflict.

