def sum (a, b):	#PLUS operation
	return a + b
	
def nus (a, b):	#MINUS operation
	return a - b
	
def div (a, b):	#MULTIPLYING operation
	return a / b
	
def mul (a, b):	#DIVISION operation
	return a * b
	
def main ():
	oper = input ("Please, define the desired operation (+,-,*,/) ") #Defining operation
	if (oper == "exit"): #Exiting
		print ("See you!")
	elif (oper != "+") and (oper != "-") and (oper != "*") and (oper != "/"): #Validation of operation
		print ("Sorry, I don't know that operation :(\nA friendly reminder: you can always print 'exit' to leave")
		main ()
	else:
		var1 = int (input ("Be kind to enter first argument "))	#Entering arguments
		var2 = int (input ("Defining the second one could be also very useful "))
		if oper == "+":	#Calling for calculating functions
			print ("The result is ", sum (var1, var2))
		elif oper == "-":
			print ("The result is ", nus (var1, var2))
		elif oper == "*":
			print ("The result is ", mul (var1, var2))
		else:
			if (var2 == 0):	#Necessary checking 
				print ("Oh, not the dividing by zero!")	#Proper reaction
			else:
				print ("The result is ", div (var1, var2))
		print ("You can always print 'exit' to leave")
		main()
		
	
	
print ("Hello, it's nice to see you!")
main ()