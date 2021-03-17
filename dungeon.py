import numpy as np
import random as rn
from termcolor import colored
import os
from curtsies import Input
from ui import gen_line
import game
import time

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
				for enemy in game.adversary:
					if x == enemy.x and y == enemy.y:
						creature=True
				if cursor_active == True and (x==cursor_position[0] and y==cursor_position[1]):
					linetxt+=" "+colored("?",'white')
				elif(x==game.player.x and y==game.player.y):
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
	game.player.x = xx
	game.player.y = yy

def spawn_enemy(w,h):
	#player spawn
	for enemy in game.adversary:
		xx=rn.randrange(1,w-1)
		yy=rn.randrange(1,h-1)
		while grid[xx][yy] != 0:
			xx=rn.randrange(1,w-1)
			yy=rn.randrange(1,h-1)
		enemy.x=xx
		enemy.y=yy

def enemy_movement():
	for enemy in game.adversary:
		for loop in range(round(enemy.spd/10)):
			#debug = look
			debug=str(enemy.name)+" turn"
			while enemy.moves < enemy.atribute["spd"]:
				moved = False
				while moved == False:
					look = rn.randrange(0,4)
					if look == 0:
						if grid[enemy.x+1][enemy.y] == 0 and enemy.x+1<w-1:
							enemy.x+=1
							moved=True
					elif look == 1:
						if grid[enemy.x-1][enemy.y] == 0 and enemy.x-1>0:
							enemy.x-=1
							moved=True
					elif look ==2:
						if grid[enemy.x][enemy.y+1] == 0 and enemy.y+1<h-1:
							enemy.y+=1
							moved=True
					elif look ==3:
						if grid[enemy.x][enemy.y-1] == 0 and enemy.y-1>0:
							enemy.y-=1
							moved=True
					if moved==True:
						os.system('clear')
						display(grid)
						print(debug)
						time.sleep(1)
						enemy.moves+=1
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
		spawn()
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
	print(x)
	print(y)
	print(grid[x][y])
	if x == game.player.x and y == game.player.y:
		return game.player.name
	for enemy in game.adversary:
		if x == enemy.x and y == enemy.y:
			return enemy.name
	if grid[x][y]==0:
		return "Nothing"
	if grid[x][y]==1:
		return "Wall"
	if grid[x][y]==2:
		return "Ladder"



def player_controller(cursor_active,cursor_position,debug):
	if cursor_active == False and game.player.turn == True:
		if keypress == 'l':
			if(grid[game.player.x+1][game.player.y]!=1):
				game.player.x+=1;
				game.player.moves+=1;
				#add (player move +=1, if move > spd: enemy move)
				#debug = "Move Right"
		if keypress == 'h':
			if(grid[game.player.x-1][game.player.y]!=1):
				game.player.x-=1;
				game.player.moves+=1;
				#debug = "Move Left"
		if keypress == 'j':
			if(grid[game.player.x][game.player.y-1]!=1):
				game.player.y-=1;
				game.player.moves+=1;
				#debug = "Move Up"
		if keypress == 'k':
			if(grid[game.player.x][game.player.y+1]!=1):
				game.player.y+=1;
				game.player.moves+=1;
				#debug = "Move Down"
		if grid[xx][yy] == 2:
			debug = "Ladder"
			if(floor>0):
				choice = input("Ladder available action (up,down,nothing)")
				#when using ladder save floor current floor and generate next floor, or load previus.
			else :
				choice = input("Ladder available action (down,nothing)")
		if keypress == ';':
			cursor_active = True
			cursor_position=[game.player.x,game.player.y]
		if game.player.moves > game.player.atribute["spd"]:
			debug=str(game.player.moves)+" spd: "+str(game.player.atribute["spd"])
			game.player.turn=False
			game.player.moves=0
	elif game.player.turn == True:
		if keypress == 'l' and cursor_position[0]<w-1:
			cursor_position[0]+=1;
				#debug = "Move Right"
		if keypress == 'h' and cursor_position[0]>0:
			cursor_position[0]-=1;
				#debug = "Move Left"
		if keypress == 'j':
			cursor_position[1]-=1 and cursor_position[1]>0;
				#debug = "Move Up"
		if keypress == 'k'  and cursor_position[1]<h-2:
			cursor_position[1]+=1;
			#cursor controller
		if keypress == ';':
			cursor_active = False
		debug=appraisal(int(cursor_position[0]),int(cursor_position[1]))
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
	cursor_active,cursor_position,debug = player_controller(cursor_active,cursor_position,debug)

	#permenent controlle
	if keypress == '\x1b':
		debug = "Exit"
		print(debug)
		exit()
	os.system('clear')
	if game.player.turn == False:
		enemy_movement()
		game.player.turn=True
		debug=str(game.player.name)+" turn"
	display(grid)
	print(str(debug))