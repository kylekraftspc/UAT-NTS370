#!/usr/bin/perl
#################################################################
#								#
#								#
# Kyle Kraft - Project 2.3:File Dump Program			#
#								#
#								#
#This is a simple program that takes user input <STDIN>		#
#for a file name and prints out the contents of that  file.	#
#################################################################
#
#
print "Please select a file to print: ";
#This line opens a variable file (named FILE) based on what the user inputs (STDIN)
#This "open" loads the selected file into memory so the script can use it.

open (FILE, <STDIN>);


print "Your selected file contains the following - \n";

#Here we use a while look to print the previously selected file to the user.
while(<FILE>) {
	#Chomp is used to remove the extra line created from the STDIN Enter press. 
	chomp $FILE;
	#This $_ tells the script to use the last variable that was opeend in memory, in this case FILE
	print $_;
}

#The close command should be used once files are done being worked with.  This 
#unloads the file from memory.
close FILE;

