#!/usr/bin/perl -w


#Kyle Kraft - Project 2.1: Perl Script
#The purpose of this script is to demonstrate the use of the CHOMP and CHOP commands.
#The first line is used to take a variable from a user.  Instead of takeing commnads from a user with READ 
#like with bash, here a variable is set to equil <STDIN> to take input from the user. Lastly, the input is 
#run through CHOMP as this will remove the new line that is added when taking information from a user.
#Perl uses PRINT instead of ECHO. \n is used at the end of the print to move make a new line.
print "Please enter a test phrase that is 6 characters in length. \n";
chomp ($name = <STDIN>);

#Here chop is used as it will delete the last character off of a string.
chop($name);

print "This is the phrase minus 1 character: $name\n";

chop($name);

print "This is the phrase minus 1 character: $name\n";

chop($name);

print "This is the phrase minus 1 character: $name\n";

chop($name);

print "This is the phrase minus 1 character: $name\n";

chop($name);

print "This is the phrase minus 1 last character: $name\n";

