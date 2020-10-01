#!/usr/bin/python
#
#
#########################################################################################################
# Kraft, Kyle - Final Project										#
#													#
#This is a program that acts as a sort of mini security tool. With it, a user can navigate a 		#
# simple, text based menu to find out more information about the passwd file, perform an 		#
# NMAP scan, inspect the syslog file, and check the version of of HTTP that a web server is using	#
# through telnet on port 80.  This script is expected to be run on a Linux machine and so, I had	#
# no issues using os.system to pass commands directly to the OS from python. 				#
#													#
#													#
#########################################################################################################


#Import os is used so that python can run commands that work on the OS.  Import time is used to create 
# artificial "thinking" periods since I'm not a fan of the spit-everything-at-the-user presentation.
#
import os
import time


#Here I define the only glocal variable that I'll be using.  In this case, it's the variable that controls
# the main menu. 
MENU = "not a number"


#To make the script more readable and scalable, I decided to define each feature as a function.  The four functions I've
# created are PASSWD, NMAP, HTTP, and SYSLOG. With these being defined as functions, it's easy for the script to jump around
# to where the user wants to be. 


#The first function simply takes the contents of the passwd file, sorts it into alphabetical order, saves a copy to
# the users local directory, and prints out that information. 
def PASSWD():
	print "The passwd file list of usernames along with home directory and shell types will be printed shortly\n"
	time.sleep(1)
        os.system('sort /etc/passwd | cut -f1,6,7 -d":" > pwdresult.txt')
        os.system('cat pwdresult.txt')
	print "\nIf you wish to view this file later, a copy has been placed in your current direcotry as pwdresult.txt\n"
	return

#Here is where NMAP can be ran by the user.  It can take either a URL or a full IP.  Before running, the user is prompted to
# to ensure that they wish to continue.  
def NMAP():
	#Here our two variables needed for this function are defined.  RUN is used to make sure the user wishes to proceed 
	# with the scan and IP is used to collect the URL or IP that the user wishes to perform the scan against.
	RUN = " "
	IP = "255.255.255.255"

	#This while loop runs unless the user answers N to the warning banner.  If the user selects n, the while loop will end
	# and the user will be placed back at the main menu. 
	while RUN != 'n':
		print "\nThis will attempt to perform a verbose NMAP scan of a desired network range.  Are you sure you wish to proceed?"
		RUN = raw_input("\nPlease enter (y)es to continue or (n)o to cancle out\n")
		if RUN == 'y':
			#If they user selects yes, the user is prompted for information and is given examples of what is expected. Even
			# if the user provides bad information, nmap will still run but will return that nothing was able to be found. 
			print "\nPlease enter the an IP or a web address range for the scan. The results of this scan will be placed in your currect direcotry.\n"
			IP = raw_input("Example range 10.140.1.1-10 or www.uat.edu. ")
			print "Please wait while the NMAP scan completes.  This could take a minute.  Press CTRL+C to cancel and return to the main menu."
			#Just like the passwd file dump, the nmap results will be placed in a file that the user can look at once the script has closed.
			os.system("nmap -A {} > nmapresult.txt".format(
			IP,
			)
			)
			os.system('cat nmapresult.txt')
			return
			
		elif RUN == 'n':
			print "\nReturning to main menu.\n"
		elif RUN != 'y' and RUN != 'n' :
			print "Please enter either y or n."


#Here the function to check what version a web server is running on port 80 is defined. I saw that the nmap scan from above could also list this information but I
# wanted a second way of accessing this information.  Here I attempt a telnet to the users specified device on port 80, put that output into a file called telnet.txt.
# From there, grep is used to find the line that has the HTTP version and then cut is used to print only the HTTP version.  However, since I was unable to figure out
# how to pass information from python into the telnet session, so that way I could  push the command "HEAD / HTTP/1.0", I used a slightly messy workaround. 

def HTTP():
	URL = " "
	print "Welcome to the web server version check!\n"
	print "Here you can check what version of HTTP a website is using."
	URL = raw_input("\nPlease enter the URL you wish to check!\n")
	#Here is my inelegant solution to my problem.  By using "yes ' '" in front of my telnet command, this is supposed to pass a string to the session on the first 
	# prompt.  However, regardless of what I used, using this causes the session to error out. The good news for me is that a part of the error message returns the 
	# HTTP version that is running. The other issue that comes out of this is that the error messages from telnet are still sent to the user.  I wish I would have
	# had more time to troubleshoot this and get this part working correctly. 
	os.system("yes \' \' | telnet {} 80 > telnet.txt".format(
	URL,
	)
	)
	print "The version of HTTP that is being run on this server is listed below!"
	time.sleep(.5)
	os.system("cat test.txt | grep HTTP | cut -d \' \' -f1")
	print "\nReturning to main menu\n"
	time.sleep(2)

#The last function that I have defined is a submenu that allows the user to inspect the syslog file. It works in almost exactly like the main menu. 
def SYSLOG():
	MENU2 = "Stuff"
	while MENU2 != 'q':
		print "\nWelcome!  Here you can check your log files either manually or check any failed login attempts!\n"
		print "Please choose from the following.\n"
		print "[1] Check the syslog file manually. (Prints syslog)."
		print "[2] Check for failed login attempts."
		print "[q] Return to previous menu."
		MENU2 = raw_input("Please enter your selection. ")
		if MENU2 == 'q':
			print "\nReturning to main menu."
			time.sleep(.5)
			return
		elif MENU2 == '1':
			#This is placeholder syslog file since Jeremy couldn't get me access to the system syslogfile. I asked that a failed login attempt
			# be put in the file so that I could have the script bring up a failed login attempt to show to the user. 
			print "Printing syslog file... Please wait..."
			time.sleep(1)
			os.system("more /home/kkraft/syslog")
		elif MENU2 == '2':
			print "Printing failed login attempts... Please wait..."
			time.sleep(1)
			os.system("cat /home/kkraft/syslog | grep Failure")



#The last part of the program is the first part that the user will use.  Here the user can enter a value (it's recorded as a string) between
# 1 and 4 or q to navigate the program. 			
while MENU != 'q':
	print "\nWelcome to the security script!\n"
	print "[1] View local PASSWD file.  (Alphabetical)"
	print "[2] Perform NMAP scan."
	print "[3] Inspect log files."
	print "[4] Check a web server version."
	print "[q] Quit"
	#This is always going to be a string.  Use raw_input instead of input.
	MENU = raw_input("\nWhat would you like to do? ")
	
	#Here the menu options that the user have chosen will be compaired to MENU and the appropriate function will be called.  
	if MENU == 'q':
		print "\nThank you for using this program!\n"
	elif MENU == '1':
		time.sleep(.5)
		PASSWD()
	elif MENU == '2':
		time.sleep(.5)
		NMAP()
	elif MENU == '4':
		time.sleep(.5)
		HTTP()
	elif MENU == '3':
		time.sleep(.5)
		SYSLOG()
print "Bye for now!" 





















