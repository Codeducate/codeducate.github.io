"""
This project will convert a temperature to another form of temperature, 
with Fahrenheit, Celsius, and Kelvin.
"""
#This can be Kelvin, Fahrenheit, or Celsius
print("What scale is your starting temperature in?")
x = input()

#Same for this
print("What scale do you want to convert your temperature to?")
y = input()

#This is the temperature
print("What is your starting temperature?")
Z=int(input())
# This is all converting from Kelvin
if (x == "Kelvin" and y == "Kelvin"):
	print(Z)
elif (x == "Kelvin" and y == "Fahrenheit"):
	C= Z-273
	F=9/5*(C)+32
	print (F)
elif (x == "Kelvin" and y == "Celsius"):
	C=Z-273
	print (C)
# THis is all converting from Fahrenheit
elif (x == "Fahrenheit" and y == "Kelvin"):
	C= (Z-32) * (5/9)
	K= C+273
	print(K)
elif (x == "Fahrenheit" and y == "Fahrenheit"):
	print(Z)  
elif (x == "Fahrenheit" and y == "Celsius"):
	C=(Z-32) *(5/9)
	print(C)
# This is all converting to Celsius
elif (x == "Celsius" and y == "Kelvin"):
	K=Z-273
	print (K)
elif(x == "Celsius" and y == "Fahrenheit"):
	F=(9/5) * Z +32
	print (F)
elif(x == "Celsius" and y == "Celsius"):
	print(Z)
else:
	print("Sorry, we are unable to process your request. Please restart and try again!")

	
f=["Meghana Guttikonda","Sadhika Dhanasekar", "Subhi Saibaba"]

t=(12,12,14)

v = 4
while(v<5):
	print("Thank you for using our program!")
	v = v + 1

m = 59
while(m<60):
	print("Please try as many times as you want!")
	m = m + 1

for s in range (0, 2):
	print(s)
print("This was a required thing, ignore it!")


print("This program was created by ", f)