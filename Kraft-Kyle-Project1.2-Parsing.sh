#!/bin/sh

#Kyle Kraft - Project1.2 Parsing
#The purpose of this program will be to take the contents of etc/passwd and seperate out the username, home directory
# and the shell.  The file will first list all entries with only the required information similarly to how it appears
# within the passwd file.  Next, 3 categories will be made each of the required fields. All of this will be in
# alphabetical order.

#This first line will list out all entries in alaphabetical order and place that into a file called Project1-2-Results.txt.
# The sort command will display the file in alaphabetical order, the cut command will take only the information in the
# first (username), sixth (home directory), and seventh field. -d lets the script know that the fields are seperated by :.
# Lastly, the script will then place the output of this command into our file.
# A single > will be used so that each time this script is run, all old information will be lost.
sort ~/etc/passwd | cut -f1,6,7 -d":" > Project1-2-Results.txt


#These lines will serve to help seperate what has been collected to make it easier for humans to read.
echo " "  >> Project1-2-Results.txt
echo "===================================USERNAMES==============================================" >> Project1-2-Results.txt
echo " "  >> Project1-2-Results.txt

#The script will be run 3 more times to collect the remaining fields that are required. 

#Takes only usernames.
sort ~/etc/passwd | cut -f1 -d":" >> Project1-2-Results.txt



echo " "  >> Project1-2-Results.txt
echo "===================================HOME-DIR==============================================" >> Project1-2-Results.txt
echo " "  >> Project1-2-Results.txt

#Takes only the home directory
#Items will still be listed in alphabetical order by username.
sort  ~/etc/passwd | cut -f6 -d":" >> Project1-2-Results.txt


echo " "  >> Project1-2-Results.txt
echo "===================================USER-SHELL==============================================" >> Project1-2-Results.txt
echo " "  >> Project1-2-Results.txt

#Takes only user shells
#Items will still be listed in alphabetical order by username.
sort  ~/etc/passwd | cut -f7 -d":" >> Project1-2-Results.txt
