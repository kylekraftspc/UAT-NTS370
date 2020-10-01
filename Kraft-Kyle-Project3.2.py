#!/usr/bin/python

########################################################################
# Kraft, Kyle - Project 3.2                                         ####
########################################################################
#
#The purpose of this script is to add numbers at the opposite ends of a
# sequence, show this process to the user, and then print out what 
# all these numbers add up to.
#
# After the example has been done for number 1 to 100, the user can then
# select their own sequence of numbers to perform the calculation with.

#First I declare a range of numbers.  Because python thinks that ranges 
# start at zero, we have to use 101 instead of 100 because we're looking
# for the 101st number in that list. 

GAUSS=range(1,101)
print "================================================================="
print "This is our inital range of numbers to work with!"
#This prints the range that will be worked with.  

print GAUSS
print "================================================================="
print "Now we need to add the first digit and last digit together, over and over!"

#A few variables will be needed in this script and they are defined here. 

#LOOPS is used for the number additions that have been made. I.E. 1+100, 2+99, ect, ect.
LOOPS = 0
#SUM is used to hold the value of the numbers that were added together. 
SUM = 0
#ANSWER is used for the final answer of the additions.  
ANSWER = 0


#Because I wanted to add more than one set of numbers together, I decided to use 
# a function so that I could perform this multiple times. 

def ADD():
    #Global defines the variables that will be used that were declared outside the function
    global LOOPS, SUM, ANSWER
    #Here we add the first value in the list to the last value in the list.
    SUM = GAUSS[0] + GAUSS[-1]
    #This displays that addition to the user.  The .format feature is used to keep the code here more
    # human readable.
    print("{}+{}={}".format(
    GAUSS[0],
    GAUSS[-1],
    SUM,
    )
    )
    #The number of pairs that have been added together is incrimened here.  This is also the number of times 
    # the function has looped. 
    LOOPS = 1 + LOOPS
    print "This is how many pairs of numbers we've added together!"
    print LOOPS
    #Here the two numbers that were worked with are removed from the list. 
    del GAUSS[0],GAUSS[-1]
    print "============================================================="
    #The variable ANSWER has its value set to be displayed to the user.  It's not kept as a part 
    # of the function so that it's not being constantly displayed to the user without purpose.
    ANSWER = LOOPS * SUM

#This while is the first time that the above function will run. It says that while GAUSS
# holds a value in its list, it will run.  
while len(GAUSS) > 0: 
    ADD()

print "Here is the answer to the Gauss problem!"
print ANSWER

#Before moving on, our variables will need to be set back to zero or those answers will carry over to where we don't
# want them. 
ANSWER = 0
LOOPS = 0

print "======================================================="
print "Now it's your turn! Put in any set of consecutive numbers to try it out!"

#Input is taken from the user so they can perform their own test.  This will only work if the low number is a positive
# number and is lower than the higher number. 
LOW = input("What is your low number?\n")
HIGH = input("Now what is your high number?\n")
#The users HIGH number will have 1 added to it so the user doesn't need to be aware that their range would really start at zero.
HIGH = HIGH + 1

print "Bellow you'll see what happens!"

#GAUSS is redefined with the new variables that were supplied by the user and the range is then printed.
GAUSS=range(LOW,HIGH)
print GAUSS

#A new while is used that will call on the previously defined function. This will request that the function stop once the list has 1 or less
# values defined in it.  
while len(GAUSS) > 1:
    ADD()
    #An additional IF statement is needed to handle odd numbered lists. It says that once there is only one number in the list left, add it to
    # our answer.  
    if len(GAUSS) == 1:
        ANSWER = GAUSS[0] + ANSWER

print "Here is the answer to your list!\n"
print ANSWER

