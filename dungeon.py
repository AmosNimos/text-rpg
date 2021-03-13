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
enemy_symbol = "%"


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
				if(x==game.player.x and y==game.player.y):
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


w = int((rows)-4)
h = int((cols/2)-2)
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

def spawn_enemy():
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
			look = rn.randrange(0,4)
			debug = look
			if look == 0:
				if grid[enemy.x+1][enemy.y] == 0 and enemy.x+1<w-1:
					enemy.x+=1
			elif look ==1:
				if grid[enemy.x-1][enemy.y] == 0 and enemy.x-1>0:
					enemy.x-=1
			elif look ==2:
				if grid[enemy.x][enemy.y+1] == 0 and enemy.y+1<h-1:
					enemy.y+=1
			elif look ==3:
				if grid[enemy.x][enemy.y-1] == 0 and enemy.y-1>0:
					enemy.y-=1

def spawn_player():
	#player spawn
	xx=rn.randrange(0,w)
	yy=rn.randrange(0,h)
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

grid = gen_grid(w,h)
grid = gen_wall()
grid = gen_automata()
#Columns = []
#Rows = []
xx=0
yy=0

grid = spawn_player()
spawn_enemy()


#gen grid


os.system('clear')
display(grid)

while True:
	keypress = main()
	debug=""
	if keypress == 'd':
		if(grid[game.player.x+1][game.player.y]!=1):
			game.player.x+=1;
			#add (player move +=1, if move > spd: enemy move)
			#debug = "Move Right"
	if keypress == 'a':
		if(grid[game.player.x-1][game.player.y]!=1):
			game.player.x-=1;
			#debug = "Move Left"
	if keypress == 'w':
		if(grid[game.player.x][game.player.y-1]!=1):
			game.player.y-=1;
			#debug = "Move Up"
	if keypress == 's':
		if(grid[game.player.x][game.player.y+1]!=1):
			game.player.y+=1;
			#debug = "Move Down"
	if keypress == '\x1b':
		debug = "Exit"
		print(debug)
		exit()
	if grid[xx][yy] == 2:
		debug = "Ladder"
		if(floor>0):
			choice = input("Ladder available action (up,down,nothing)")
			#when using ladder save floor current floor and generate next floor, or load previus.
		else :
			choice = input("Ladder available action (down,nothing)")
	enemy_movement()
	os.system('clear')
	display(grid)
	#if debug == "":
		#print("press w,a,s,d key")
	print(debug)