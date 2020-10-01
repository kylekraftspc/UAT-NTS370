#!/bin/sh
#Student - Kyle Kraft Project 1.1: Shell Script
#The purpose of this script is to build a basic script that takes the user's
#name as well as the class identifier and displays a welcome message.

#Defined constants that will be called throughout the script
school="UAT"


# Callouts for the user's name and class are identified within the script as $1 and $2. The user will need to provide
#this information to the script before running it. EX: ./<filename> Variable1 Variable2
echo "Hello $1!  You're currently attending $2, at $school!"

