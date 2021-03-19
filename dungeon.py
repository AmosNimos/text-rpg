import numpy as np
import random as rn
from termcolor import colored
import os
from curtsies import Input
from ui import gen_line
import game
import time
import battle
import entities

size = os.get_terminal_size() 
cols = size[0]
rows = size[1]
grid=[]
player_symbol = "@"
stair_symbol = "H"
wall_symbol = "#"
empty_symbol = "."
enemy_symbol = "*"
debug=""

#rows == height
w = int((rows)-8)
h = w
cursor_active=False
cursor_position = [0,0]

player = entities.Spider("Player",True)
enemy1 = entities.Insect("Bugs",False)
enemy2 = entities.Insect("Big Bug",False)
adversary = [enemy1,enemy2]

#0=empty, 1=wall, 2=stair
def display(grid):
	#print(gen_line("+","-"))
	linetxt=""
	for y in range(len(grid)):
		print(linetxt)
		linetxt="  "
		try:
			for x in range(len(grid[y])):
				creature=False
				for enemy in adversary:
					if x == enemy.x and y == enemy.y:
						creature=True
				if cursor_active == True and (x==cursor_position[0] and y==cursor_position[1]):
					linetxt+=" "+colored("?",'white')
				elif(x==player.x and y==player.y):
					#display player
					linetxt+=" "+colored(player_symbol,'white')
				elif creature == True:
					linetxt+=" "+colored(enemy_symbol,'red')
				elif(grid[x][y]==0):
					linetxt+=" "+colored(empty_symbol,'white')
				elif(grid[x][y]==1):
					linetxt+=" "+colored(wall_symbol,'white')
				elif(grid[x][y]==2):
					linetxt+=" "+colored(stair_symbol,'yellow')
				#display monster here
		except:
			pass
			#print("error")
	print("")
	print(gen_line("+","-"))

def gen_grid(w,h):
	for x in range(w):
		grid.append([])
		for y in range(h):
			grid[x].append(0)
	return grid

def gen_wall():
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if rn.randrange(0,5)==0:
				grid[y][x]=1
	return grid

def gen_automata():
	nebor=0
	w=len(grid)
	for y in range(w):
		h=len(grid[y])
		nebor=0
		for x in range(h):
			if x>2 and y>2 and x<h-3 and y<w-5:
				if grid[y][x-1]==1:
					nebor+=1
				if grid[y][x+1]==1:
					nebor+=1
				if grid[y-1][x]==1:
					nebor+=1
				if grid[y+1][x]==1:
					nebor+=1
				if grid[y-1][x-1]==1:
					nebor+=1
				if grid[y+1][x+1]==1:
					nebor+=1
				if grid[y-1][x+1]==1:
					nebor+=1
				if grid[y+1][x-1]==1:
					nebor+=1
				if nebor>2:
					grid[y][x]=0
				if nebor<2:
					grid[y][x]=1
				nebor=0
	return grid

def update_player(xx,yy):
	player.x = xx
	player.y = yy

def check_for_entities(x,y,user):
	r = False
	for enemy in adversary:
		if enemy.x == x and enemy.y == y and enemy != user:
			r = True
	if enemy.x == player.x and enemy.y == player.y and player != user:
		r = True
	return r

def spawn_enemy(w,h):
	#player spawn
	for enemy in adversary:
		xx=rn.randrange(1,w-1)
		yy=rn.randrange(1,h-1)
		while grid[xx][yy] != 0 or check_for_entities(xx,yy,enemy)==True:
			xx=rn.randrange(1,w-1)
			yy=rn.randrange(1,h-1)
		enemy.x=xx
		enemy.y=yy

def enemy_movement():
	for enemy in adversary:
		#debug = look
		debug=str(enemy.name)+" turn, moves ["+str(enemy.moves)+"/"+str(enemy.atribute["spd"])+"]"
		while enemy.moves <= enemy.atribute["spd"]:
			moved = False
			while moved == False:
				look = rn.randrange(0,4)
				if look == 0:
					if grid[enemy.x+1][enemy.y] == 0 and enemy.x+1<w-1:
						if check_for_entities(enemy.x+1,enemy.y,enemy) == False:
							enemy.x+=1
							moved=True
				elif look == 1:
					if grid[enemy.x-1][enemy.y] == 0 and enemy.x-1>0:
						if check_for_entities(enemy.x-1,enemy.y,enemy) == False:
							enemy.x-=1
							moved=True
				elif look ==2:
					if grid[enemy.x][enemy.y+1] == 0 and enemy.y+1<h-1:
						if check_for_entities(enemy.x,enemy.y+1,enemy) == False:
							enemy.y+=1
							moved=True
				elif look ==3:
					if grid[enemy.x][enemy.y-1] == 0 and enemy.y-1>0:
						if check_for_entities(enemy.x,enemy.y-1,enemy) == False:
							enemy.y-=1
							moved=True
				if moved==True:
					os.system('clear')
					display(grid)
					print(debug)
					time.sleep(0.1)
					enemy.moves+=1
					debug=str(enemy.name)+" turn, moves ["+str(enemy.moves)+"/"+str(enemy.atribute["spd"])+"]"
		enemy.moves=0
	os.system('clear')

def spawn_player(w,h):
	#player spawn
	xx=rn.randrange(4,w-4)
	yy=rn.randrange(4,h-4)
	update_player(xx,yy)
	grid[xx][yy] = 0
	#spawn stair
	if(yy<h-1):
		grid[xx][yy+1] = 2
	elif(xx<w-1):
		grid[xx+1][yy] = 2
	elif(xx>1):
		grid[xx-1][yy] = 2
	elif(yy>1):
		grid[xx][yy-1] = 2
	else:
		pass
	return grid

def spawn(target):
	xx=rn.randrange(0,w)
	yy=rn.randrange(0,h)
	while grid[xx][yy] != 0:
		xx=rn.randrange(0,w)
		yy=rn.randrange(0,h)
	target.x = xx
	target.y = xx

def main():
	with Input(keynames='curses') as input_generator:
		for e in input_generator:
			return e

def appraisal(x,y):
	# the amount of information of each apresal is equivalent to the wiz level, just like moves is equivalent to spd, the information are stored as string in list
	print(x)
	print(y)
	print(grid[x][y])
	if x == player.x and y == player.y:
		return player.name
	for enemy in adversary:
		if x == enemy.x and y == enemy.y:
			return enemy.name
	if grid[x][y]==0:
		return "Ground"
	if grid[x][y]==1:
		return "Wall"
	if grid[x][y]==2:
		return "Ladder"

def check_for_wall(from_x,from_y,to_x,to_y):
	if from_y == to_y:
		if from_x < to_x:
			while from_x < to_x:
				if grid[from_x][from_y] == 1:
					return True
				from_x+=1
		else:
			while to_x < from_x:
				if grid[from_x][from_y] == 1:
					return True
				to_x+=1
	if from_x == to_x:
		if from_y < to_y:
			while from_y < to_y:
				if grid[from_x][from_y] == 1:
					return True
				from_y+=1
		else:
			while to_y < from_y:
				if grid[from_x][from_y] == 1:
					return True
				to_y+=1
	return False

def player_controller(cursor_active,cursor_position):
	debug=""
	if player.moves > player.atribute["spd"]-1:
		player.turn=False
		player.moves=0
	if cursor_active == False and player.turn == True:
		debug=str(player.name)+" turn, moves ["+str(player.moves)+"/"+str(player.atribute["spd"])+"]"
		if keypress == 'l' and player.x<w-1:
			if(grid[player.x+1][player.y]!=1):
				if check_for_entities(player.x+1,player.y,player) == False:
					player.x+=1;
					player.moves+=1;
					debug=str(player.name)+" turn, moves ["+str(player.moves)+"/"+str(player.atribute["spd"])+"]"
				else:
					debug="this direction is obstucted by a creature"
			else:
				debug="this direction is obstucted by a wall"
				#debug = "Move Right"
		if keypress == 'h' and player.x>0:
			if(grid[player.x-1][player.y]!=1):
				if check_for_entities(player.x-1,player.y,player) == False:
					player.x-=1;
					player.moves+=1;
					debug=str(player.name)+" turn, moves ["+str(player.moves)+"/"+str(player.atribute["spd"])+"]"
				else:
					debug="this direction is obstucted by a creature"
			else:
				debug="this direction is obstucted by a wall"
				#debug = "Move Left"
		if keypress == 'j' and player.y>0:
			if(grid[player.x][player.y-1]!=1):
				if check_for_entities(player.x,player.y-1,player) == False:
					player.y-=1;
					player.moves+=1;
					debug=str(player.name)+" turn, moves ["+str(player.moves)+"/"+str(player.atribute["spd"])+"]"
				else:
					debug="this direction is obstucted by a creature"
			else:
				debug="this direction is obstucted by a wall"
				#debug = "Move Up"
		if keypress == 'k' and player.y<h-2:
			if(grid[player.x][player.y+1]!=1):
				if check_for_entities(player.x,player.y+1,player) == False:
					player.y+=1;
					player.moves+=1;
					debug=str(player.name)+" turn, moves ["+str(player.moves)+"/"+str(player.atribute["spd"])+"]"
				else:
					debug="this direction is obstucted by a creature"
			else:
				debug="this direction is obstucted by a wall"
				#debug = "Move Down"
		if grid[xx][yy] == 2:
			debug = "Ladder"
			if(floor>0):
				choice = input("Ladder available action (up,down,nothing)")
				#when using ladder save floor current floor and generate next floor, or load previus.
			else :
				choice = input("Ladder available action (down,nothing)")
		if keypress == ';':
			cursor_position=[player.x,player.y]
			cursor_active = True
			debug=appraisal(int(cursor_position[0]),int(cursor_position[1]))

		if player.moves >= player.atribute["spd"]:
			debug=str(player.name)+" turn, moves ["+str(player.moves)+"/"+str(player.atribute["spd"])+"]"
			debug+="\nend of turn?"

	elif player.turn == True and cursor_active == True:
		if keypress == 'l' and cursor_position[0]<w-1:
			cursor_position[0]+=1;
				#debug = "Move Right"
		if keypress == 'h' and cursor_position[0]>0:
			cursor_position[0]-=1;
				#debug = "Move Left"
		if keypress == 'j' and cursor_position[1]>0:
			cursor_position[1]-=1;
				#debug = "Move Up"
		if keypress == 'k'  and cursor_position[1]<h-2:
			cursor_position[1]+=1;
			#cursor controller
		debug=appraisal(int(cursor_position[0]),int(cursor_position[1]))
		if keypress == ';':
			for enemy in adversary:
				if cursor_position[0] == enemy.x and cursor_position[1] == enemy.y:
					if enemy.x == player.x or enemy.y == player.y:
						if check_for_wall(player.x,player.y,enemy.x,enemy.y)==False:
							#if no wall are found between the two
							battle.battle(player,enemy,True)
						else:
							debug=str(enemy.name)+" out of reach."
					else:
						#debug="uh... not sure about that."
						debug=str(enemy.name)+" out of reach."
			cursor_active = False
	else:
		print("...")
	return cursor_active,cursor_position,debug


grid = gen_grid(w,h)
grid = gen_wall()
grid = gen_automata()
#Columns = []
#Rows = []
xx=0
yy=0

grid = spawn_player(w,h)
spawn_enemy(w,h)


os.system('clear')
display(grid)

while True:
	keypress = main()
	cursor_active,cursor_position,debug = player_controller(cursor_active,cursor_position)

	#permenent controlle
	if keypress == '\x1b':
		debug = "Exit"
		print(debug)
		exit()
	os.system('clear')
	if player.turn == False:
		enemy_movement()
		player.turn=True
	display(grid)
	print(str(debug))