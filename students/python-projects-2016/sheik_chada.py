#Smera's and Rahi's Python mini project

#In the input section enter your overall grade on a certain subject. 
#This program will tell you wether you have a GPA above a 3.0 or not
 
from array import *
intarray = array('i', [100,98,97,93,92,90,89,87,86,83])
#print intarray[1]
y = int(input())
if(y >= intarray[1] and y <= intarray[0]):
	print("You have a 4.3 GPA!")
elif(y >=intarray[3] and y <=intarray[2]):
	print("Your GPA is 4.0")
elif(y >= intarray[5] and y < intarray[4]):
	print("Your GPA is 3.7")
elif(y >= intarray[7] and y < intarray[6]):
	print("Your GPA is 3.3")
elif(y >= intarray[9] and y < intarray[8]):
	print("Your GPA is 3.0")
else:
	print("Your GPA is not above 3.0")


 
#The following program will be able to calculate what your overall grade is on three tests
#If you have more than three grades in a certain subject
# you can always make more variables and change the divisor into the number of varaibles you have inserted.
#Again this is only an example
y = 95
x = 87
z = 93
print((y+x+z)/3)

#This program will tell you how much you need on your final in order to obtain your "dream grade""
#Again it is only an example 

#In variable "r" enter your "dream" grade. In the variable "y" enter the grade you got on your midterm.
#In variable "x" enter how much percent the midterm is for your grade. In varaible "z" enter the 
#you got on a test (or project). In variable "a" enter the how much percent the test(or project)counted 
#for your grade. Now let the magic happen! 

r = 0.85
y = 0.81
x = 0.6
z = 0.92
a = 0.1

print(r-(-y * x)*(-z * a))




