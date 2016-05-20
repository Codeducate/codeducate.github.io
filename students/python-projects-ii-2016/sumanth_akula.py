import time
import sys
import os

var = True
while var:
    print("Copyright 1969 Apple inc. (c)  Designed by Apple in Calafornia, Made in china")
    time.sleep(2) # delays for 2 seconds
    print("Initilizing boot sequence.  Stand by for POST.")  
    time.sleep(0.5) # delays for 0,5 seconds
    print("POST complete, Loading calculator OS X...")
    time.sleep(5) # delays for 5 seconds
    print("Welcome to Calculator OS X. Select an operation that you would like to do:")
    print("")
    print("###########################################")
    print("##           1-Addition                  ##")
    print("##           2-Subtraction               ##")
    print("##           3-Division                  ##")
    print("##           4-Multiplication            ##")
    print("##           5-Exit                      ##")
    print("###########################################")
    print("")
    answer = int(input("Choose what you want to do here: "))
    os.system("cls")
    time.sleep(1.5) # delays for 1.5 seconds
    #
    if(answer == 1):
        print("loading, please wait...")
        time.sleep(3) # delays for 3 seconds
        os.system("cls")
        print("You have selected Addition!")
        x = int(input("Please type your first number here: "))
        y = int(input("Please type your second number here: "))
        print("Calculating, please wait...")
        time.sleep(2) # delays for 2 seconds
        print(x + y)
        time.sleep(10) # delays for 10 seconds
        print("Please standby for reboot")
        time.sleep(0.5) # delays for .5 seconds
        #
    elif(answer == 2):
        print("loading, please wait...")
        time.sleep(3) # delays for 3 seconds
        os.system("cls")
        print("You have selected Subtraction!")
        x = int(input("Please type your first number here: "))
        y = int(input("Please type your second number here: "))
        print("Calculating, please wait...")
        time.sleep(2) # delays for 2 seconds
        print(x - y)
        time.sleep(10) # delays for 10 seconds
        print("Please standby for reboot")
        time.sleep(0.5) # delays for .5 seconds
        #
    elif(answer == 3):
        print("loading, please wait...")
        time.sleep(3) # delays for 3 seconds
        os.system("cls")
        print("You have selected Division!")
        x = int(input("Please type your first number here: "))
        y = int(input("Please type your second number here: "))
        print("Calculating, please wait...")
        time.sleep(2) # delays for 2 seconds
        print(x / y)
        time.sleep(10) # delays for 10 seconds
        print("Please standby for reboot")
        time.sleep(0.5) # delays for .5 seconds
        #
    elif(answer == 4):
        print("loading, please wait...")
        time.sleep(3) # delays for 3 seconds
        os.system("cls")
        print("You have selected Multiplication!")
        x = int(input("Please type your first number here: "))
        y = int(input("Please type your second number here: "))
        print("Calculating, please wait...")
        time.sleep(2) # delays for 2 seconds
        print(x * y)
        time.sleep(10) # delays for 10 seconds
        print("Please standby for reboot")
        time.sleep(0.5) # delays for .5 seconds
    elif(answer == 5):
        print("Exiting Calculator OS X.  Standby for Shutdown...")
        time.sleep(2) # delays for 2 seconds
        exit()

    else:
        print("invalid input!  Standby for reboot")
        time.sleep(3) # delays for 3 seconds