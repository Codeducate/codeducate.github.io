print("welcome to my calculator")
typeofsum = input("would you like addition(+), subtraction(-), multiplication(*), or division (/)?")
print(typeofsum)
 
if typeofsum == "A":
	number1 = int(input("please enter number - "))
	number2 = int(input("please enter number - "))
	print (number1 + number2)
 
elif typeofsum == "S":
	number1 = int(input("please enter number - "))
	number2 = int(input("please enter number - "))		
	print (number1 - number2)
 
elif typeofsum == "M":
	number1 = int(input("please enter number - "))
	number2 = int(input("please enter number - "))		
	print (number1 * number2)
 
elif typeofsum == "D":
	number1 = int(input("please enter number - "))
	number2 = int(input("please enter number - "))		
	print (number1 / number2)