print("This app will help you tell how many pounds you gain and lose,in a daily lifestyle. You will have to put in how much food your eating, with the addition of calories, and how much exercise you do in a certain day.")
	# Description of problem faced by many people all over the world.
print("This will be a life changing experience!")
print("Proven to studies this program will help you to live longer and happier, without having obesity, or any other problems because of your lifestyle, weight, or anything to do with your diet.")
	#This is not actually proven, this point is to prove MY POINT
print("Our top scientist actually tried this product and is going to help me prove my point.She is Sydney Brenner, most of you probably know her.")
	#This is a real scientist, but did not try our made-up product.
print("Buy this program, it will help your life. BELIEVE ME.")
	# We assume, but it is not proven.
 
your_name = input("\nThis health report is for: ")
print(your_name)
 
cal_intake = int( input(""))
print("\nYou entered your calorie intake for today as: ", cal_intake)
if cal_intake<1200:
	print ("You are healthy.")
else:
	print("You need to eat more healthy because", cal_intake, "is more than what you need.")
 
num_miles = int( input(""))
print("\nThe number of miles you ran today: ",num_miles)
if num_miles>=6:	
	print("You are in very good health, keep doing what your doing!!!")
else:
	print("Do more exercise, and you will be guaranteed to lose a couple of pounds.")
 
curr_age = int( input(""))
print("\nHere is the age that you provided us with:",curr_age)
if curr_age<9:
	print("You are too young to  exercise, GO PLAY OUTSIDE because you are only",curr_age)
else:
	print("You should have started long ago!!!!")
 
veg_serv = int(input(""))
print("\nYou apparently ate this many servings of veggies: ",veg_serv)
if veg_serv>7:
	print("Wow, you are eating the right amount of ", veg_serv, "servings of vegetables.")
else:
	print ("You should eat more servings of vegetables as ",veg_serv, "servings is not enough.")
 
yogaList=[120,126,130,139,144]
print("\nEnter the amount of time that you did yoga in minutes:", yogaList[3])
if yogaList[3]>140:
	print("You are doing GREAT!! Keep it up!!")
else:
	print("You are doing good, but still need to increase your time from ",yogaList[3]," minutes")
 
print("\nTo calculate the amount of protein that your body should intake you multiply your weight and 0.37.")
print("Here is an example:")
print("My weight is 100 pounds.")
print("100*0.37=37")
print("So I should intake 37 grams of protein.")
#This is just an example
age=[20,25,30,35,40,45,50,55,60]
calorieIntake=[1700,1690,1680,1670,1660,1650,1640,1630,1620]
if age[1]>19:
	print("Here you enter your age:",age[0])
	print("Calorie Intake to loose weight:",calorieIntake[0])
else:
	print("YOU ARE TOO YOUNG!!!!")
print("With this program you are guranteed to lose wait.")