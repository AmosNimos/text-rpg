#status template
#self.status = {"terget":target,"type":"poison","dmg": 5, "turns": 5, chances:"100%"}
#consume {"hp":0,"mp":0,"sp":0}
# growth {"status_effect":self.level*0.5, "status_turn":False, "skill_effect": 2}

tackle_skill={
	"name":"Tackle",
	"description":"A simple phisical attack to seize and throw down the target",
	"level":1,
	"cost_hp":0,
	"cost_sp":10,
	"cost_mp":0,
	"affect_hp":10,
	"affect_sp":0,
	"affect_mp":0,
	"support":False,
	"status":False,
}

bite_skill={
	"name":"Bite",
	"description":"A simple phisical attack to pierce the skin of the target with the teeth, fangs, or mouthparts.",
	"level":1,
	"cost_hp":0,
	"cost_sp":2,
	"cost_mp":0,
	"affect_hp":4,
	"affect_sp":0,
	"affect_mp":0,
	"support":False,
	"status":False,
}


poison_fang_skill={
	"name":"Poison Fang",
	"description":"A special phisical attack to pierce the skin of the target with fangs to inject poison.",
	"level":1,
	"cost_hp":0,
	"cost_sp":15,
	"cost_mp":0,
	"affect_hp":50,
	"affect_sp":0,
	"affect_mp":0,
	"support":False,
	"status":["poison",],
}

# class Skill(name,target,aim,effect,description,price,consume,status):
# 	def __init__(self,name):
# 		self.consume = consume
# 		self.price=price
# 		self.name=name
# 		self.description=description
# 		self.status=status
# 		self.level=0
# 		self.target=target
# 		self.aim=aim #what variable of target does the skill affect
# 		self.effect=effect #how much does it affect the variable exemple -5 or 10
# 		self.growth=growth # the increasse of velua after each level 
# 		self.unlock=unlock #list of skills the this skill unlock to be gain.
	
# 	def level-up(status,level,effect):
# 		effect+=

# 	def use(user,target,aim):
# 		target.aim+=effect
# 		user.

# tackle = Skill("tackle","enemy","hp","-5","A simple phisical attack to seize and throw down the target",50,{"hp":5,"mp":0,"sp":10},False)

# # attack type skills
# class Bite(Attack):
# 	atk_name = "Bite",
# 	atk_type = "Physical",
# 	atk_damage = 5,
# 	status = False
# 	#skills unlock and their cost
# 	unlock = {"Power_bite": 75, "Poison_bite": 200}
# 	consume = {hp:0,mp:0,sp:5}

# class Poison_bite(Attack):
# 	atk_name = "Bite",
# 	atk_type = "Physical",
# 	atk_damage = 5,
	

	 

# def normal_attack(target,dmg):
# 	target.health-dmg

