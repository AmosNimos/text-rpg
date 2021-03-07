import numpy as np
import random as rn
from termcolor import colored
import os
from curtsies import Input
from ui import gen_line

def main():
	with Input(keynames='curses') as input_generator:
		for e in input_generator:
			return e

def display(grid):
	print(gen_line("+","-"))
	linetxt=""
	for y in range(len(grid)):
		print(linetxt)
		linetxt="  "
		try:
			for x in range(len(grid[y])):
				if(x==xx and y==yy):
					linetxt+=" "+colored(str(grid[x][y]),'red')
				elif(grid[x][y]==0):
					linetxt+=" "+colored(".",'white')
				elif(grid[x][y]==1):
					linetxt+=" "+colored("#",'white')
		except:
			pass
			#print("error")
	print("")
	print(gen_line("+","-"))

def gen_grid():
	for y in range(int((rows)-4)):
		grid.append([])
		for x in range(int((cols/2)-2)):
			grid[y].append(0)
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

size = os.get_terminal_size() 
cols = size[0]
rows = size[1]
grid=[]
grid = gen_grid()
grid = gen_wall()
grid = gen_automata()
#Columns = []
#Rows = []
xx=0
yy=0

#gen grid


os.system('clear')
display(grid)

while True:
	keypress = main()
	debug=""
	if keypress == 'd':
		if(grid[xx+1][yy]!=1):
			xx+=1;
			debug = "Move Right"
	if keypress == 'a':
		if(grid[xx-1][yy]!=1):
			xx-=1;
			debug = "Move Left"
	if keypress == 'w':
		if(grid[xx][yy-1]!=1):
			yy-=1;
			debug = "Move Up"
	if keypress == 's':
		if(grid[xx][yy+1]!=1):
			yy+=1;
			debug = "Move Down"
	if keypress == '\x1b':
		debug = "Exit"
		print(debug)
		exit()
	os.system('clear')
	display(grid)
	#if debug == "":
		#print("press w,a,s,d key")
	print(debug)

