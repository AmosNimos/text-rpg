#enemy monster attack
#changing dungeon floor (save up to 5 previus floor) (seal previus path warning)
#add randomness to attack and stuff like dmg*random(0.5,1.5)
#name idea:

import random as rn
start = ["maou","titan","demon","monster","death","blood","spirit","dungeon","god","infernal","symphony","domination"]
middle = [" & "," of "," "] #" of the "
end = ["rise","rising","evolution","possession","reign","infinite","legend","execution","struggle","world","cry","evil","survival","dead","order","king","collapse"]

names=[]
for x in end:
	for y in start:
		names.append(y+middle[rn.randint(0,2)]+x)

print(names[rn.randint(0,len(names)-1)])
print(names[rn.randint(0,len(names)-1)])
print(names[rn.randint(0,len(names)-1)])
print(names[rn.randint(0,len(names)-1)])
print(names[rn.randint(0,len(names)-1)])
print(names[rn.randint(0,len(names)-1)])

