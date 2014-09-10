from random import randint
def hit (victim):
#randomly chooses struck limb
	i = randint (0, 5)
	limbs = ["left leg", "right leg", "left arm", "right arm", "torso", "head"]
	print (victim + " hits " + limbs[i])

def d (dice):
#random for dices
	return (randint (1, dice))

def enterStats (playerNumber):
#Input of detailed player characteristics
	print ("For player #", playerNumber[0],":")
	playerNumber.append(int (input ("Enter Strength ")))
	playerNumber.append(int (input ("Enter Dexterity ")))
	playerNumber.append(int (input ("Enter Intelligence ")))

def displayStats (encounterStats):
#Reminder for encounter stats
	print ("Total hit point for encounter is", encounterStats[0])
	print ("Vulnerability towards Strength is", encounterStats[1])
	print ("Vulnerability towards Dexterity is", encounterStats[2])
	print ("Vulnerability towards Intelligence is", encounterStats[3])
	
def turn(player, encounterStats):
#One turn for one player
	print ("Player #", player[0], "in action!")
	action = int(input("Choose main action(str/dex/int):"))
	damage = d(20)
	print ("d20 rolls for", damage)
	damage = 1 * damage * player[action] * encounterStats[action]
	print ("Damage is", damage)
	encounterStats[0] = encounterStats[0] - damage
	print ("Hit points left", encounterStats[0])
	
	action = int(input("Choose secondary action(str/dex/int):"))
	damage = d(20)
	print ("d20 rolls for", damage)
	damage = 0.5 * damage * player[action] * encounterStats[action]
	print ("Damage is", damage)
	encounterStats[0] = encounterStats[0] - damage
	print ("Hit points left", encounterStats[0])
	print ("Time for encounter response!")
		
def firstEncounter(p1, p2, p3):
#Weak skeleton
	encounterStats = [100, 2, 1, 0.5]
	displayStats (encounterStats)
	print ('Weak skeleton is aproaching')
	while (encounterStats[0] > 0):
		turn (p1, encounterStats)
		turn (p2, encounterStats)
		turn (p3, encounterStats)
	
	
	
	

	
	

def main():
	numberOfPlayers = int(input ("Please, enter number of players "))		
	p1 = [1]
	p2 = [0]
	p3 = [0]
	enterStats (p1)
	if (numberOfPlayers > 1) :
		p2[0] = 2
		enterStats (p2)
	if (numberOfPlayers > 2) :
		p3[0] = 3
		enterStats (p3)
	firstEncounter(p1, p2, p3)


main ()
#for x in range (3):
#	print (x)