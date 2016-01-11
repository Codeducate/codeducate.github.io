

#the first input is mathematics

a=int(input())

a2 = str(a)

#the second input is science

b=int(input())

b2 = str(b)

#the third input is english

c=int(input())

c2 = str(c)


#the fourth input is your language course (spanish,french,latin,german)

d=int(input())

d2 = str(d)


#the fifth input is history

e=int(input())

e2 = str(e)

my_average = ((a + b + c + d + e)/5)
#__________________________________________________________________________________________________________
#this section is for mathematics

if a>=98:
	
	print ("You are doing great in math!" + "-" + a2)

elif a>=93:

	print ("You are doing good in math" + "-" + a2)

elif a>=90:

	print ("You are on the right path in math, but you can do better!" + "-" + a2)

elif a>=88:

	print ("Come on, you just need to study harder and bump your grade up to an A" + "-" + a2)

elif a>=83:

	print ("Come on I know you can step up your grade in math" + "-" + a2)

elif a>=80:

	print ("From now on you need to study for every test" + "-" + a2)

else:

	print ("go to this site and start helping yourself: http://www.classzone.com/cz/books/algebra_1_2007_na/book_home.htm?state=VA" + "  " + "-" + a2)
#______________________________________________________________________________________
#this section is for science

if b>=98:

	print ("You are doing great in science!" + "-" + b2)

elif b>=93:

	print ("You are doing good in science" + "-" + b2)

elif b>=90:

	print ("You are on the right path in science, but you can do better!" + "-" + b2)

elif b>=88:

	print ("Come on, you just need to study harder and bump your grade up to an A" + "-" + b2)

elif b>=83:

	print ("Come on I know you can step up your grade in science" + "-" + b2)

elif b>=80:

	print ("From now on you need to study for every test" + "-" + b2)

else:

	print ("http://www.lcps.org/cms/lib4/VA01000195/Centricity/Domain/4996/Notes%20Book%20Semester%201%20Characteristics-Genetics.pdf" + "  " + "-" + b2)
#____________________________________________________________________________________
#this section is for English

if c>=98:
	
	print ("You are doing great in English!" + "-" + c2)

elif c>=93:

	print ("You are doing good in English" + "-" + c2)

elif c>=90:

	print ("You are on the right path in English, but you can do better!" + "-" + c2)

elif c>=88:

	print ("Come on, you just need to study harder and bump your grade up to an A" + "-" + c2)

elif c>=83:

	print ("Come on I know you can step up your grade in English" + "-" + c2)

elif c>=80:

	print ("From now on you need to study for every test" + "-" + c2)

else:

	print ("http://interactivesites.weebly.com/language-arts.html" + "  " + "-" + c2)
#______________________________________________________________________________________



if d>=98:
	
	print ("You are doing great in your language course!" + "-" + d2)

elif d>=93:

	print ("You are doing good in your language course" + "-" + d2)

elif d>=90:

	print ("You are on the right path in your language course, but you can do better!" + "-" + d2)

elif d>=88:

	print ("Come on, you just need to study harder and bump your grade up to an A" + "-" + d2)

elif d>=83:

	print ("Come on I know you can step up your grade in English" + "-" + d2)

elif d>=80:

	print ("From now on you need to study for every test" + "-" + d2)

else:

	print ("https://quizlet.com/" + "  " + "-" + d2)
#________________________________________________________________________________

if e>=98:
	
	print ("You are doing great in history!" + "-" + e2)

elif e>=93:

	print ("You are doing good in history" + "-" + e2)

elif e>=90:

	print ("You are on the right path in history, but you can do better!" + "-" + e2)

elif e>=88:

	print ("Come on, you just need to study harder and bump your grade up to an A" + "-" + e2)

elif e>=83:

	print ("Come on I know you can step up your grade in history" + "-" + e2)

elif e>=80:

	print ("From now on you need to study for every test in history" + "-" + e2)

else:

	print ("http://americanhistory.abc-clio.com/" + "  " + "-" + e2)
#____________________________________________________________________________________

if my_average>=98:
	
	print ("You are doing great in school!")

elif my_average>=93:

	print ("You are doing good in school")

elif my_average>=90:

	print ("You are on the right path in school, but you can do better!")

elif my_average>=88:

	print ("Come on, you just need to study harder and bump your average grade into an A in school")

elif my_average>=83:

	print ("Come on I know you can step up your grade in school")

elif my_average>=80:

	print ("From now on you need to study for every test in school")

else: print ("You need to give more importance to school:(")

print (str((my_average)) + (" is your average grade in school"))