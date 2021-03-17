import sys
import os
import time
#External library
import subprocess
from termcolor import colored, cprint
from playsound import playsound
#import shlex

size = os.get_terminal_size() 
cols = size[0]
rows = size[1]
margin=" "

def clear():
	os.system('clear')


def stats(entity):
	bar_size=cols/1.5
	print(margin+"["+entity.name+"][LV:"+str(entity.lv)+"]")
	hp_bar = gen_bar("HP",entity.hp,entity.max_hp,">",".","green",bar_size) # health
	sp_bar = gen_bar("SP",entity.sp,entity.max_sp,">",".","yellow",bar_size) # stamina
	mp_bar = gen_bar("MP",entity.mp,entity.max_mp,">",".","blue",bar_size) # magic
	print(hp_bar+"\n"+sp_bar+"\n"+mp_bar)
	print(margin+"SE["+str(entity.status_effects)+"]") #status effect

def gen_line(side,middle):
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
				line+=colored("#",color,"on_"+color) #
			else:
				line+=colored("_",color)
	else:
		for x in range(size):
			line+=colored("_",color)
	line+="]"
	return line

def gen_title(side,middle,text):
	filled = int(len(text)/2)+1
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
	for x in range(len(skills)):
		line += margin+"["+str(x)+"] "+str(skills[x]["name"])
		if x<len(skills)-1:
			line+="\n"
	return line

def gen_options(options):
	line=""
	for x in range(len(options)):
		line+=margin+"["+str(x)+"] "+options[x]
		if x<len(options)-1:
			line+="\n"
	return line

def main_menu_selection():
	#print("entrys: \nstart\nquit")
	entry = input(">")
	if entry.lower() == "0":
		os.system('clear')
	elif entry.lower() == "1":
		os.system('clear')
		help_game()
	elif entry.lower() == "2":
		os.system('clear')
		exit_game()
	while entry.lower() not in ["0","1","2"]:
		os.system('clear')
		main_menu()

def main_menu():
	line = gen_line("+","-")
	title = gen_title("|"," ","game title")
	print(line)
	print(title)
	print(line)
	actions=["Play","Help","Quit"]
	print(gen_options(actions))
	print(line)
	main_menu_selection()

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









