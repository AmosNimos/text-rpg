import sys
import os
import time
#External library
import subprocess
from termcolor import colored, cprint
from playsound import playsound
from curtsies import Input
import numpy as np
#import shlex

size = os.get_terminal_size() 
cols = size[0]
rows = size[1]
margin=" "

def play(sound):
	playsound(sound)

def clear():
	os.system('clear')

def main():
	with Input(keynames='curses') as input_generator:
		for e in input_generator:
			return e

def axis_menu(options,names,head,cursor):
	h=6
	w=int(len(names)/h)
	names = np.reshape(names, (h, w))
	keypress=""
	line=""
	view_range=4
	back_view=4
	#initialise menu
	n=0
	for y in range(h):
		for x in range(w):
			if cursor[0] == x and cursor[1]== y:
				line += margin+"["+str(names[y,x])+"]"
			else:
				line += margin+" "+str(names[y,x])+" "
			n+=1
		line+="\n"

	clear()
	print(head)
	print(line)
	line=""
	#update menu
	while keypress != ";":
		more=False
		keypress = main()
		if keypress=="l":
			if cursor[0]<h:
				cursor[0]+=1
			else:
				cursor[0]=0
		if keypress=="h":
			if cursor[0]==0:
				cursor[0]=h;
			else:
				cursor[0]-=1;
		if keypress=="k":
			if cursor[1]+2<w:
				cursor[1]+=1
			else:
				cursor[1]=0
		if keypress=="j":
			if cursor[1]==0:
				cursor[1]=w-2;
			else:
				cursor[1]-=1;
		n=0
		for y in range(h):
			for x in range(w):
				if cursor[0] == x and cursor[1]==y:
					line += margin+"["+str(names[y,x])+"]"
				else:
					line += margin+" "+str(names[y,x])+" "
				n+=1
			line+="\n"
		clear()
		print(head)
		print(line)
		line=""


	return names[cursor[1],cursor[0]],cursor

def menu(options,names,head):
	cursor=0
	keypress=""
	line=""
	view_range=4
	back_view=4
	#initialise menu
	for x in range(len(names)):
		if x<cursor+view_range and x>=cursor:
			if cursor == x:
				line += margin+"▸ "+str(names[x])
				#line += margin+"[+] "+str(names[x])
			else:
				line += margin+"▫ "+str(names[x])
				#line += margin+"[-] "+str(names[x])
			if x<len(names)-1:
				line+="\n"
	clear()
	print(head)
	print(line)
	line=""

	#update menu
	while keypress != ";":
		more=False
		keypress = main()
		if keypress=="k":
			if cursor<len(options)-1:
				cursor+=1
			else:
				cursor=0;
		if keypress=="j":
			if cursor==0:
				cursor=len(options)-1
			else:
				cursor-=1;

		if cursor > back_view:
			line += margin+"[-] <---\n"
		for x in range(len(names)):
			if x<cursor+view_range and x>=cursor-back_view:
				if cursor == x:
					line += margin+"▸ "+str(names[x])
				else:
					line += margin+"▫ "+str(names[x])
				if x<len(names)-1:
					line+="\n"
			if len(names)>cursor+view_range:
				more=True
		if more==True:
			line += margin+"[-] --->"
		clear()
		print(head)
		print(line)
		line=""

	for option in range(len(options)):
		if cursor == option:
			return options[option]
	return "error"

def stats(entity):
	render=""
	status_effects=""
	bar_size=cols/1.5
	render+=margin+"["+entity.name+"][LV:"+str(entity.lv)+"]\n"
	hp_bar = gen_bar("HP",entity.hp,entity.max_hp,">",".","green",bar_size) # health
	sp_bar = gen_bar("SP",entity.sp,entity.max_sp,">",".","yellow",bar_size) # stamina
	mp_bar = gen_bar("MP",entity.mp,entity.max_mp,">",".","blue",bar_size) # magic
	render+=hp_bar+"\n"+sp_bar+"\n"+mp_bar+"\n"
	for status in entity.se:
		status_effects+=str(status["type"])+", lv."+str(status["level"])+" last."+str(status["last"])
	render+=margin*2+"[status:"+str(status_effects)+"]\n" #status effect
	return render

def gen_line(side,middle):
	middle = "─"
	line=side
	for x in range(cols-2):
		line+=middle
	line+=side
	return line

def delay_text(text,delay,newline):
	if delay == True:
		spd = 0.02
		for letter in text:
			sys.stdout.write(letter)
			sys.stdout.flush()
			playsound('data/bip.wav')
			time.sleep(spd)
		if newline == True:
			sys.stdout.write("\n")
			sys.stdout.flush()
			playsound('data/bip.wav')
	else:
		print(text)
		playsound('data/bip.wav')


def gen_text_line(text,side,middle):
	line="["+str(text)+"]"
	size=cols-(len(line)+1)
	for x in range(size):
		line+=middle
	line+=side
	return line

def gen_bar(text,current,total,front,back,color,size):
	size = int(size-(len(margin)+2))
	line=margin*2+"["+text+":"+str(current)+"/"+str(total)+"|"
	if total > 0:
		bar_size = current/total*size
		for x in range(size):
			if x<bar_size:
				line+=colored("█",color,"on_"+color) #
			else:
				line+=colored("▁",color)
	else:
		for x in range(size):
			line+=colored("_",color)
	line+="]"
	return line

def gen_title(side,middle,text):
	filled = int(len(text)/2)
	while (int(cols/2)-filled)*2+len(text)>cols:
		filled+=1
	if (filled % 2) != 0:
		filled+=1
	if (len(text) % 2) != 0:
		text+=middle
	line=side
	for x in range(int(cols/2)-filled):
		line+=middle
	line+=text.upper()
	for x in range(int(cols/2)-filled):
		line+=middle
	line+=side
	return line

def skills_options(target):
	line=""
	skills = target.skills
	cursor=0
	keypress=""
	while keypress != ";":
		keypress = main()
		if keypress=="k":
			if cursor<len(skills)-1:
				cursor+=1
			else:
				cursor=0;
		if keypress=="j":
			if cursor==0:
				cursor=len(skills)-1
			else:
				cursor-=1;
		for x in range(len(skills)):
			if cursor == x:
				line += margin+"[*] "+str(skills[x]["name"])
			else:
				line += margin+"["+str(x)+"] "+str(skills[x]["name"])
			if x<len(skills)-1:
				line+="\n"
		clear()
		print(line)
		line=""
	return line,cursor

def gen_options(options):
	line=""
	for x in range(len(options)):
		line+=margin+"["+str(x)+"] "+options[x]
		if x<len(options)-1:
			line+="\n"
	return line


game_title = "monster of the dungeon"
def main_menu():
	line = gen_line("+","-")
	title = gen_title("|"," ",game_title)
	option = gen_title(""," ","[START]")
	keypress=""
	head = ""
	clear()
	head += line+"\n"
	head += title+"\n"
	head += line
	entry = menu([0,1,2],["start","help","exit"],head)
	if entry == 2:
		exit()
	elif entry == 1:
		clear()
		print("euh... use [h,j,k,l] to move and [;] to do other stuff.")
		exit()
	else:
		clear()
	# while keypress != ";":
	# 	keypress = main()
	# 	clear()
	# 	print(line)
	# 	print(title)
	# 	print(line)
	# 	print(option)
	# 	print(line)

def game_over():
	line = gen_line("+","-")
	title = gen_title("|"," ","game over")
	actions=["Play","Help","Quit"]
	print(gen_options(actions))
	print(line)
	main_menu_selection()

def start_game():
	pass

def exit_game():
	print("bye bye")
	sys.exit()

def help_game():
	print("I am too lazy to write help.")
	print("figure things out on your own.")









