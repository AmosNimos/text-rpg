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
xx=0
yy=0
grid=[]
adversary = []
player_symbol = "@"
stair_symbol = "H"
wall_symbol = "#"
empty_symbol = "."
enemy_symbol = "&"
door_symbol = "+"
debug=""
dungeon_floor=1



#rows == height
w = int((rows)-8)
h = w
cursor_active=False
cursor_position = [0,0]

player = entities.Spider("Player",True,dungeon_floor)

def gen_enemy():
	amounth = round(w/3)
	enemy=[]
	for index in range(amounth):
		power=0
		enemy.append(entities.Insect("",False,dungeon_floor))
	return enemy
		#enemy.hp = max_hp


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
					linetxt+=" "+colored("?",'green')
				elif(x==player.x and y==player.y):
					#display player
					linetxt+=" "+colored(player_symbol,'green', 'on_cyan')
				elif creature == True:
					linetxt+=" "+colored(enemy_symbol,'red','on_magenta')
				elif(grid[x][y]==0):
					linetxt+=" "+colored(empty_symbol,'white')
				elif(grid[x][y]==1):
					linetxt+=" "+colored(wall_symbol,'white')
				elif(grid[x][y]==2):
					linetxt+=" "+colored(stair_symbol,'yellow')
				elif(grid[x][y]==3):
					linetxt+=" "+colored(door_symbol,'cyan')
				#display monster here
		except:
			pass
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

def gen_symetry():
	side=rn.randint(0,3)
	if side == 1 or side == 3:
		half_w = round(w)
		half_h = round(h/2)
		sym=rn.randint(0,1)
		for x in range(half_h):
			if rn.randint(0,sym)==0:
				for y in range(half_w):
					if grid[y][x] == 1:
						grid[y][half_h+(half_h-x)]=1
					elif grid[y][x] == 0:
						grid[y][half_h+(half_h-x)]=0
	if side == 2 or side == 3:
		half_w = round(w/2)
		half_h = round(h)
		sym=rn.randint(0,1)
		for y in range(half_w):
			if rn.randint(0,sym)==0:
				for x in range(half_h):
					if grid[y][x] == 1:
						grid[half_w+(half_w-y)][x]=1
					elif grid[y][x] == 0:
						grid[half_w+(half_w-y)][x]=0
	return grid

def update_player(xx,yy):
	player.x = xx
	player.y = yy

def check_for_entities(x,y,user):
	r = False
	e=""
	for enemy in adversary:
		if enemy.x == x and enemy.y == y and enemy != user:
			r = True
			e=enemy.name
	if x == player.x and y == player.y and player != user:
		r = True
		e=player.name
	return r,e



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
						r,e = check_for_entities(enemy.x+1,enemy.y,enemy)
						if r == False:
							enemy.x+=1
							moved=True
						elif e == player.name:
							print("attack")
				elif look == 1:
					if grid[enemy.x-1][enemy.y] == 0 and enemy.x-1>0:
						r,e = check_for_entities(enemy.x-1,enemy.y,enemy)
						if r == False:
							enemy.x-=1
							moved=True
						elif e == player.name:
							print("attack")
				elif look ==2:
					if grid[enemy.x][enemy.y+1] == 0 and enemy.y+1<h-1:
						r,e = check_for_entities(enemy.x,enemy.y+1,enemy)
						if r == False:
							enemy.y+=1
							moved=True
						elif e == player.name:
							print("attack")
				elif look ==3:
					if grid[enemy.x][enemy.y-1] == 0 and enemy.y-1>0:
						r,e = check_for_entities(enemy.x,enemy.y-1,enemy)
						if r == False:
							enemy.y-=1
							moved=True
						elif e == player.name:
							print("attack")
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
	djf=dungeon_floor
	if player.moves > player.atribute["spd"]-1:
		player.turn=False
		player.moves=0
	if cursor_active == False and player.turn == True:
		debug=str(player.name)+" turn, moves ["+str(player.moves)+"/"+str(player.atribute["spd"])+"]"
		if keypress == 'l' and player.x<w-1:
			if(grid[player.x+1][player.y]!=1):
				r,e = check_for_entities(player.x+1,player.y,player)
				if r == False:
					player.x+=1;
					player.moves+=1;
					debug=str(player.name)+" turn, moves ["+str(player.moves)+"/"+str(player.atribute["spd"])+"]"
				else:
					debug="this direction is obstucted by a "+str(e)
			else:
				debug="this direction is obstucted by a wall"
				#debug = "Move Right"
		if keypress == 'h' and player.x>0:
			if(grid[player.x-1][player.y]!=1):
				r,e = check_for_entities(player.x-1,player.y,player)
				if r == False:
					player.x-=1;
					player.moves+=1;
					debug=str(player.name)+" turn, moves ["+str(player.moves)+"/"+str(player.atribute["spd"])+"]"
				else:
					debug="this direction is obstucted by a "+str(e)
			else:
				debug="this direction is obstucted by a wall"
				#debug = "Move Left"
		if keypress == 'j' and player.y>0:
			if(grid[player.x][player.y-1]!=1):
				r,e = check_for_entities(player.x,player.y-1,player)
				if r == False:
					player.y-=1;
					player.moves+=1;
					debug=str(player.name)+" turn, moves ["+str(player.moves)+"/"+str(player.atribute["spd"])+"]"
				else:
					debug="this direction is obstucted by a "+str(e)
			else:
				debug="this direction is obstucted by a wall"
				#debug = "Move Up"
		if keypress == 'k' and player.y<h-2:
			if(grid[player.x][player.y+1]!=1):
				r,e = check_for_entities(player.x,player.y+1,player)
				if r == False:
					player.y+=1;
					player.moves+=1;
					debug=str(player.name)+" turn, moves ["+str(player.moves)+"/"+str(player.atribute["spd"])+"]"
				else:
					debug="this direction is obstucted by a "+str(e)
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
			ladder_down=False
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
				elif grid[cursor_position[0]][cursor_position[1]]==2:
					ladder_down=True
			if ladder_down == True:
				djf=dungeon_floor+1

			cursor_active = False
	else:
		print("...")
	return cursor_active,cursor_position,debug,djf

def spawn_enemy():
	#player spawn
	xx=0
	yy=0
	for enemy in adversary:
		xx=rn.randrange(1,w-1)
		yy=rn.randrange(1,h-1)
		while grid[xx][yy] != 0 or check_for_entities(xx,yy,enemy)==True:
			xx=rn.randrange(1,w-1)
			yy=rn.randrange(1,h-1)
		enemy.x=xx
		enemy.y=yy

#gen dungeon floor
adversary = gen_enemy()
grid = gen_grid(w,h)
grid = gen_wall()
grid = gen_automata()
grid = gen_symetry()
grid = spawn_player(w,h)
spawn_enemy()
os.system('clear')
display(grid)

while True:
	keypress = main()
	current_floor=dungeon_floor
	cursor_active,cursor_position,debug,dungeon_floor = player_controller(cursor_active,cursor_position)
	if dungeon_floor>current_floor:
		print("ladder up")
		exit()
	elif dungeon_floor<current_floor:
		print("ladder down")
		exit()
	#permenent controlle
	if keypress == '\x1b':
		debug = "Exit"
		print(debug)
		exit()
	os.system('clear')
	if player.turn == False:
		enemy_movement()
		debug=player.name+" turn"
		player.turn=True
	display(grid)
	print(str(debug))