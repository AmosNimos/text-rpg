#living entities
import skills
import ui
import time
import battle


class Monster:
	def __init__(self,name,player):
		self.name=name
		self.max_sp=200 
		self.sp=self.max_sp #stamina point
		self.max_hp=100
		self.hp=self.max_hp #health point
		self.max_mp=0
		self.mp=self.max_mp #magic point
		self.lv=0 #level
		self.alive=True
		self.player=False
		self.skills=[skills.tackle_skill]
		self.status_effects=[] #se
		self.x = 0
		self.y = 0
		self.experience=0 #xp
		self.spd = 20

	def use_skill(self,skill,target,player,opponent):
		if self.hp >= skill["cost_hp"] and self.sp >= skill["cost_sp"] and self.mp >= skill["cost_mp"]:
			self.hp-=skill["cost_hp"]
			self.sp-=skill["cost_sp"]
			self.mp-=skill["cost_mp"]
			battle.field(player,opponent)
			#add a miss parameter
			#print(skill["name"]+"consume "+str(skill["cost_hp"])+" hp, "+str(skill["cost_sp"])+" sp, "+str(skill["cost_mp"])+" mp.")
			text = self.name+" use "+skill["name"]+"."
			ui.delay_text(text,True,True)
			time.sleep(0.25)
			target.hp-=skill["affect_hp"]
			target.sp-=skill["affect_sp"]
			target.mp-=skill["affect_mp"]
			battle.field(player,opponent)
			text = target.name+" get hit by "+skill["name"]+"."
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
			missing=""
			if self.hp < skill["cost_hp"]:
				print(self.name+" cant use "+skill["name"]+" not eneugh hp.")
			if self.sp < skill["cost_sp"]:
				print(self.name+" cant use "+skill["name"]+" not eneugh sp.")
			if self.mp < skill["cost_mp"]:
				print(self.name+" cant use "+skill["name"]+" not eneugh mp.")

	def death(self):
		if self.hp<=0:
			self.alive = False

	def gain_skill(self,new_skill):
		self.skills.append(new_skill)

##Animal classes
class Insect(Monster):
	def __init__(self,name,player):
		super().__init__(name,player)
		self.skills.append(skills.bite_skill)

class Spider(Insect):
	def __init__(self,name,player):
		super().__init__(name,player)
		self.skills.append(skills.poison_fang_skill)
		#self.skills.append("web")

#x = Insect("bob")
#x.gain_skill("fire")

#class mammal()
#class bird()
#class reptiles()
#class amphibian()
#class arthropods()





