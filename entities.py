#living entities
import skills
import ui
import time
import battle
import random as rn

class corps:
	def __init__(self,name,player,level):
		self.name=name+" corps"
		self.lv=level #level

class Monster:
	def __init__(self,name,player,level):
		self.name=name
		self.lv=level #level
		self.xp=0
		self.player=player
		self.rank=0
		self.max_sp=200 
		self.sp=self.max_sp #stamina point
		self.max_hp=100
		self.hp=self.max_hp #health point
		self.max_mp=0
		self.mp=self.max_mp #magic point
		self.sustenance=self.max_sp
		self.alive=True
		self.skills=[skills.tackle_skill]
		self.turn=player
		self.atribute={"spd":0,"agi":0,"wiz":0,"str":0,"dex":0,"res":0,"sta":0}
		self.moves=0
		self.titles=[]
		self.size=0
		#stamina how long you can use your full speed bedor it decrease to one move per turn, befor each move remove health.
		#each spiecies have their own random atribute rules.
		self.se=[] #status effect
		self.x = 0
		self.y = 0
		self.experience=0 #xp
		self.age = 1
		# longevity depend on the species
		self.longevity=0


	def use_skill(self,skill,target,player,opponent):
		if self.hp >= skill["cost_hp"] and self.sp >= skill["cost_sp"] and self.mp >= skill["cost_mp"]:
			self.hp-=skill["cost_hp"]
			self.sp-=skill["cost_sp"]
			self.mp-=skill["cost_mp"]
			if self.hp<0:
				self.hp=0
			if self.sp<0:
				self.sp=0
			if self.mp<0:
				self.mp=0
			ui.clear()
			print(battle.field(player,opponent))
			#add a miss parameter
			#print(skill["name"]+"consume "+str(skill["cost_hp"])+" hp, "+str(skill["cost_sp"])+" sp, "+str(skill["cost_mp"])+" mp.")
			text = self.name+" use "+skill["name"]+"."
			ui.delay_text(text,True,True)
			time.sleep(0.25)
			target.hp-=skill["affect_hp"]
			target.sp-=skill["affect_sp"]
			target.mp-=skill["affect_mp"]
			if target.hp<0:
				target.hp=0
			if target.sp<0:
				target.sp=0
			if target.mp<0:
				target.mp=0	
			ui.clear()
			print(battle.field(player,opponent))
			text = target.name+" get hit by "+skill["name"]+"."
			ui.play("data/hit.wav")
			ui.delay_text(text,True,True)
			time.sleep(0.25)
			if skill["support"]==False:
				if skill["affect_hp"]>0:
					text = target.name+" loose "+str(skill["affect_hp"])+" hp."
					ui.delay_text(text,False,True)
					time.sleep(0.25)
				if skill["affect_sp"]>0:
					text = target.name+" loose "+str(skill["affect_sp"])+" sp."
					ui.delay_text(text,False,True)
					time.sleep(0.25)
				if skill["affect_mp"]>0:
					text = target.name+" loose "+str(skill["affect_mp"])+" mp."
					ui.delay_text(text,False,True)
					time.sleep(0.25)

			else:
				self.hp+=skill["affect_hp"]
				self.sp+=skill["affect_sp"]
				self.mp+=skill["affect_mp"]
			ui.time.sleep(0.50)
		else:
			ui.clear()
			print(battle.field(player,opponent))
			missing=""
			if self.hp < skill["cost_hp"]:
				text = self.name+" cant use "+skill["name"]+" not eneugh (HP)."
				ui.delay_text(text,True,True)
				time.sleep(0.35)
			if self.sp < skill["cost_sp"]:
				text = self.name+" cant use "+skill["name"]+" not eneugh (SP)."
				ui.delay_text(text,True,True)
				time.sleep(0.35)
			if self.mp < skill["cost_mp"]:
				text = self.name+" cant use "+skill["name"]+" not eneugh (MP)."
				ui.delay_text(text,True,True)
				time.sleep(0.35)

	def death(self):
		if self.hp<=0:
			self.alive = False
			self.name+=" corps"

	def recover(self,value):
		self.xp+=value
		self.hp+=value
		self.sp+=round(value/2)
		self.mp+=round(value/3)
		if self.hp>self.max_hp:
			self.hp=self.max_hp
		if self.sp>self.max_sp:
			self.sp=self.max_hp
		if self.mp>self.max_mp:
			self.mp=self.max_mp


	def gain_skill(self,new_skill):
		self.skills.append(new_skill)

##Animal classes
class Insect(Monster):

	def __init__(self,name,player,level):
		scale = [0.5,1,1.5,2]
		monster_rank = ["Small","Regular","Large","Giant"]
		value=0
		size_index = round(rn.randint(0,3))
		size = scale[size_index]
		super().__init__(name,player,level)
		self.skills.append(skills.bite_skill)
		self.atribute={"spd":1,"agi":4,"wiz":1,"str":1,"dex":4,"res":2,"sta":4}
		if player == False:
			self.lv=level
			self.size=size
			self.name=str(monster_rank[size_index])+" Bug"
		else:
			self.lv=1
		value = rn.randint(2,16)
		self.max_hp = round(level*value*size)
		self.hp = self.max_hp
		value = rn.randint(1,8)
		self.max_sp = round(level*value*size)
		self.sp = self.max_sp
		value = rn.randint(0,4)
		self.max_mp = round(level*value*size)
		self.mp = self.max_mp

class Spider(Insect):
	def __init__(self,name,player,level):
		super().__init__(name,player,level)
		self.skills.append(skills.poison_fang_skill)
		self.atribute={"spd":8,"agi":6,"wiz":1,"str":2,"dex":8,"res":2,"sta":6}
		#self.skills.append("web")

#x = Insect("bob")
#x.gain_skill("fire")

#class mammal()
#class bird()
#class reptiles()
#class amphibian()
#class arthropods()





