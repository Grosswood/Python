#Computer is guessing
def comStep(minVal, maxVal):
	averageVal = (minVal + maxVal) // 2
	print ('Your number is', averageVal,'?')
	answer = input ()
	if answer == "+":
		comStep((averageVal + 1), maxVal)
	elif answer == "-":
		comStep(minVal, (averageVal - 1))
	else:
		print ('Haha! I knew it!')

#User is guessing		
def humStep (randomNumber):
	playerGuess = int(input ("Please, enter your guess "))
	while playerGuess != randomNumber:
			if playerGuess > randomNumber:
				print ("Your guess is greater")
				playerGuess = int(input ())
			else:
				print ("Your guess is less")
				playerGuess = int(input ())
	print ("Your guess is correct!")

def main():
	gameType = input ("Print '0' if you want Computer to Guess Number in your mind or '1' if you want Computer to come up with random number and guess it yourself ")
	if ((gameType != "0") and (gameType != "1")):
		print ('I believe that mean you want to exit. Farewell though, hope to see you soon again!')
	elif (gameType == "0"):
		maxVal = int(input ("Please, input the desired range "))
		print ('Come up with any number from desired range, type "-" if your number is less, "+" if greater, other inputs will be considered as computer being correct')
		comStep (0, maxVal)
		main ()
	else:
		maxVal = int(input ("Please, input the desired range "))
		maxVal = randint (1, maxVal)
		humStep (maxVal)
		main ()
		
		

from random import randint
	
print ("Welcome to Guess Number Program!")
	
main ()