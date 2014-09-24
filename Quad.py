#Discriminant
def dis (c1, c2, c3):
	return c2**2 - 4 * c1 * c3

#Final replica
def final ():
	decis = input ("Do you want to try different coefficients? (yes/no) ")
	if decis == ("yes"):
		main ()
	elif decis == ("no"):
		print ("A shame though. Hope to see you soon! :) ")
	else:
		print ('I guess that meant "no". See you soon then! :) ')


	
def main ():
#Input variables
	c1 = int (input ("First: "))
	c2 = int (input ("Second: "))
	c3	= int (input ("Third: "))
	disc = dis (c1, c2, c3)
#Identifying range
	if disc < 0:
		print ("Thank you! Unfortunately, discriminant of above mentioned equation is below zero, therefore there's no solution in rational numbers ")
		final ()
#Calculation for answer
	else:
		print ("There's solution for equation:\n", (-c2 / (2 * c1) - (disc ** 0.5) / (2 * c1)))
		if disc > 0:
			print (-c2 / (2 * c1) + (disc ** 0.5) / (2 * c1))
		final ()

		
	
	
print ("Hello! Hope you're having a good day! Please enter coefficients for Quadratic equation")
main ()