from random import randint

def d (dice):
#private random for dices
	return (randint (1, dice))
	
def D (dice):
#public random
	result = (randint (1, dice))
	print ("d", dice, "rolls for", result)
	return result
	
def hit (playerNumber):
#When player injured randomly chooses struck limb
	limbs = ["left leg", "right leg", "left arm", "right arm", "torso", "head"]
	print ("Player #", playerNumber, "injured his", limbs[(d(6) - 1)])

def enterStats (playerNumber, skills):
#Input of detailed player characteristics
	print ("Enter for player #", playerNumber[0],":")
	for i in range (0, 8):
		playerNumber.append(int (input (skills[i])))


def displayStats (encounterStats, skills):
#Reminder for encounter stats
	print ("Total hit point for encounter is", encounterStats[0])
	print ("Vulnerabilities towards:")
	for i in range (0, 8):
		print (skills[i], encounterStats[i+1])

	
def turn(player, encounterStats, skills):
#One turn for one player
	print ("Player #", player[0], "in action!")
	damage = 0
	for act in range (1, 3):
		print ("Choose action #", act, "(F, R, K, S, H, T, G, N, '0' is for change vulnerability):")
		action = int(input())
		if action == 0:
			new = int(input("Choose vulnerability to change "))
			encounterStats[new] = int(input("Input new amount "))
			action = int(input ("Choose new action "))
		for stat in range (0, player[action]):
			damage = (2 * D(20) * encounterStats[action]) + damage
		encounterStats[0] = encounterStats[0] - damage
		print ("Damage is", damage)
		print ("Hit points left", encounterStats[0])
		if encounterStats[0] <= 0:
			break


	
		
def firstEncounter(p1, p2, p3, skills):
#Weak skeleton
	encounterStats = [200, 1.5, 1, 0.75, 0.25, 0.25, 1, 1.5, 1]
	displayStats (encounterStats, skills)
	print ('Weak skeleton is aproaching')
	while (encounterStats[0] > 0):
#Players turn	
		turn (p1, encounterStats, skills)
		if (encounterStats[0] > 0):
			turn (p2, encounterStats, skills)
		if (encounterStats[0] > 0):	
			turn (p3, encounterStats, skills)
#NPC turn			
		if (encounterStats[0] > 0):
			print ("Skeleton strikes back!")
			if (d(3) != 3):
				print ("He misses!")
			else:
				hit(d(3))

	
	
	
	

	
	

def main():
	numberOfPlayers = int(input ("Please, enter number of players "))		
	p1 = [1]
	p2 = [2]
	p3 = [3]
	skills = ["Fighting", "Ranged", "Knowledge", "Speech", "Healing", "Trickery", "Guts", "Notice"]
#Auto input (0 player debug, all skills = 1)	
	if numberOfPlayers == 0:
		for i in range (0 ,8):
			p1.append(1)
			p2.append(1)
			p3.append(1)
	else:
#Input skills for players
		print ("Wow! THE REAL PLAYERS!")
		enterStats (p1, skills)
		if (numberOfPlayers > 1) :
			p2[0] = 2
			enterStats (p2, skills)
		if (numberOfPlayers > 2) :
			p3[0] = 3
			enterStats (p3, skills)
	firstEncounter(p1, p2, p3, skills)

	
	
	
	
main ()


