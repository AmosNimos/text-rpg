#enemy monster attack
#changing dungeon floor (save up to 5 previus floor) (seal previus path warning)
#add randomness to attack and stuff like dmg*random(0.5,1.5)
#name idea:

import random as rn
start = ["maou","titan","demon","monster","death","blood","spirit","dungeon","god","infernal","symphony","domination","creature","beast","behemoth","villain","fiend","soul","immortal","undying","eternal","ruler","infamous","corrupt","grave","crypt","tomb"]
middle = [" & "," of "," "] #" of the "
end = ["rise","rising","evolution","possession","reign","infinite","legend","execution","struggle","world","cry","evil","survival","dead","order","king","collapse","cathacombs","feast","dynasty","control","ascendancy","command","empire","power","supremacy","sin"]

#rn.randint(0,2)

def gen_name():
	names=[]
	for x in end:
		for y in start:
			names.append(y+middle[2]+x)
	return names[rn.randint(0,len(names)-1)]

