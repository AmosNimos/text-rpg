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
	"range":1,
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
	"range":1,
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
	"range":1,
	"support":False,
	"status":["poison",],
}

poison_status={
	"type":"poison",
	"level":1,
	"last":1,
}