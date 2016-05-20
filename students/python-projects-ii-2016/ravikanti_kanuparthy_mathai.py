print("This app will help you keep track of where in the world your packages that you have ordered are at the time and place.")
print("Packages can be tracked with any service ground.")
#This is similar to a UPS tracker, used worldwide
#This can be used on any type of ordering website; not only UPS, and amazon
a=["UPS","amazon","slick deals","Groupon","Overstock","Deal Trend","Fab","Living Social", "Yippit", "Scout Mob", "Savored", "Woot", "Bloom Spot"]
b=["olive garden","pizza hut","domino's","papa john's","chipotle","harris teeter","giant","panera bread","subway","my thai place","bangrak","california tortilla","california pizza kitchen","costco"]
c=["walmart","target","justice","aeropostale","hollister","macy's","sears","The children's place","forever 21","monsoon","abercrombie kids","khol's"]
#more shops below; not to be crowded in each list
d=["american eagle","bath and body works","ann taylor","pink","banana republic","books-a-million","charlotte ruse"]
e=["champ's sports","nike","under aromour","reebok","adidas","famous footwear","payless","dick's sporting goods","claire's","pandora"]
f=["Forever 21", "Justice", "Hollister", "Aeropostale", "Charlotte Russe", "Hot Topic", "Pink", "Roxy", "Jcpenny"]
g=["Lowes", "Home Depot", "Wayfair", "Pier one imports", "Home Goods","Sams Club","Kirkland","Hobby Lobby","Pottery Barn", "World Market"]
h=["Bob's Furniture", "Marlos","Haverty","Bellfort Furniture","Bassett Furniture","Ashley Homestore","Value City Furniture","Slumberland","Contemperary Concepts","Hamiltons","Ethan Allen","La-Z-Boy"]
i=["Boons and Son Jewlery","May Jewelers", "Charleston Alexendar", "Tiny Jewel Box", "Pampilonia", "Jareds"]
j=["books-a-million","Barnes and Nobles","Hudsen Booksellers","Scott Craigs Bookstore","Skyland Books","Powell's Books","Wild Rumpus","John K. King","Strand Book Store","Politics and Prose"]
k=["Hobby Lobby", "Kirklands","Pottery Barn", "Crate&Barrel"]
# i is For jewlery stores
#This is the end of the lists.
print("Make sure you log in so that your packages are yours, and will be sent to you.")
print("1.Type in the store you are ordering from")
print("2.See if the store is available")
print("3.If it is avialable, and you are logged in, you will be able to see where your package is at that time and day.")
print("4.If you have any questions, please call 703-689-1890, or email avapackaging@gmail.com")
store= input("")
if store == "a":
	print("You entered ", a)
	print("The store is available- make sure you are logged in and continue")
else:
	print("You entered ", store)
	print("Sorry for the inconvinience- we will work on adding the store")
	print("If not fixed soon please call us at 703-689-1890")
#These stores sell different types of packages.
stores= input("")
if stores  == "e":
	print("You have entered", e)
	print("Is this your selected store?")
	print("If yes, please continue; if no, please click the back button on your computer, and select your chosen topic.")
	print("This store is available, make sure you are logged in, so you won't have a problem as you continue")
else:
	print("You entered:", stores)
	print("We are really sorry for your inconvinience")
	print("Please email us at avapackages@gmail.com with your suggestion")
	
# Note to self: Should we do this for all the stores?

	'''
	Multi line code
	to be used
	'''
Stores=input("")
if Stores == "b":
	print("You have entered",b)
	print("This is an available store.")
	print("Is this your selected store?")
	print("If yes,please continue; if no, please try again")
else:
	print("You entered:",stores)
	print("We are really sorry for your inconvinience")
	print("Please email us with any suggesetions or problems with our app, at avapackages@gmail.com")
	
#This is our third store for inputs and outputs

Ava=input("")
if Ava == "c":
	print("You have entered",c)
	print("Please continue if this is your correct store.")
else:
	print("You entered:",Ava)
	print("Since this store is unavailable, we will work on adding it.")
	print("We are really sorry for your inconvinience, but please email us with suggestions.")
	
vaa=input("")
if vaa == "k":
	print("You have entered",k)
	print("Please continue if this is your correct store.")
else:
	print("You entered:",vaa)
	print("Since this store is unavailable, we will work on adding it.")
	print("We are really sorry for your inconvinience, but please email us with suggestions.")
	
print("Now we are going to tell you in how many days your package is going to come.")

x=input(int())
for x in range(0,4):
	print("It will arrive within a week!")

print("This is for the weight of the package")
y=input(int())
for y in range(0,3):
	print("Wow, it is light!")
	
print("So excited!!!!")
print("Now let see whether it will arrive on time.")

z=input(int())
for z in range(0,2):
	print("Oh it is only coming two days late")

print("It seems like the program is really excited for you!")
		





