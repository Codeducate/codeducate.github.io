#This program will tell people how much calories they can consume until they have reached their limit.

print("How old are you")
age = int(input())
print("How many calories have you consumed today?")
cc = int(input())
print("Are you a male or female?")
gender = input()
print("Thanks! We are currently calculating your data")
if age <= 3 and gender=="female":
	print("You have consumed", 1000-cc)
elif age <= 3 and gender=="male":
	print("You have consumed”, 1000-cc)

elif (4 <= age <= 8 and gender==("female"):	print("You have consumed", 1200-cc)
elif (4<=age <= 8 and gender=="male"):
	print("You have consumed”, 1400-cc)
elif (9 <= age <= 13 and gender=="female"):
	print("You have consumed", 1600-cc)
elif (9<=age <= 13 and gender=="male"):
	print("You have consumed”, 1800-cc)
elif (14 <= age <= 18 and gender=="female"):
	print("You have consumed", 1800-cc)
elif (14<=age <= 18 and gender=="male"):
	print("You have consumed”, 2200-cc)