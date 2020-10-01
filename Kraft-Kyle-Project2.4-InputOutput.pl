#!/usr/bin/perl
#########################################################
# Kraft, Kyle - Project 2.4: Input and Output Filename###
#########################################################

#########################################################
#This is a brief exercise on taking information from one file, manipulating it, and placing that file into a
# new location. 
#
#
#The use of warnings and strict help to find mistakes within the script and inform the user of these issues.  
#Strict will also abort the script if it were to find erros. 

use strict;
use warnings;

#Here I define two variables to help in error checking.  
my $in = 0;
my $out = 0;

#Here we will take the name of the file that we wish to minipulate.  Chomp is used to remove the return 
# key from the input. 
print "Please enter the name of the INPUT filename - \n";
chomp (my $INPUT = <STDIN>);

#This is repeated again for the output file.  
print "Now please enter the name of the OUTPUT filename - \n";
chomp (my $OUTPUT = <STDIN>);

print "Awesome! Now wait one moment while we check if $INPUT and $OUTPUT exist!\n";


#In the following IF statements, error checking is done to see if the files that will be worked with exist first.
# The -e checks to see if INPUT exists and -r will ensure that the file is readable. If the file is found and is 
# readable, the error checking variable is set to 1.  If the file fails this check, the variable is set to 0 and 
# an error message will be displayed.

if (-e $INPUT and -r $INPUT) {
	print "$INPUT looks good!\n";
	$in = 1;
} else {
	print "Sorry! I didn't find that INPUT file!\n";
	$in = 0;
}

#Here we do the same checks that were done for  INPUT. The difference heere is that instead of looking to see if the
# file is readable, the file is checked to ensure we can write to it.  
if (-e $OUTPUT and -w $OUTPUT) {
	print "$OUTPUT looks good!\n";
	$out = 1;
} else {
	print "Sorry! I didn't find that OUTPUT file!\n";
	$out = 0;
}

#Here is one last error check to make sure that both INPUT and OUTPUT are ready. As mentioned before, if the file 
# is ready for our script the corresponding variable was set to 1, if not it was set to 0.  This IF statement checks
# these two.  If both are set to 1 (both passed), then the script proceeds, if one or the other is NOT 1, the script 
# will end with the DIE commond. 
if ($in == 1 and $out == 1) {
	print "Looks like we're ready to go!\n"
} else {
	print "Something seems wrong. Please check the filenames and try again.\n";
	die}

#Here both files are opened so that they can be loaded inot memory and be used.  Note that when we open OUTPUT, we specify
# with the >> that we wish to append information into the file that was set for OUTPUT. 
open (INPUT, "$INPUT");
open (OUTPUT, ">>$OUTPUT");

#This WHILE is used to replace information in the INPUT file.  Specifically, "s/home/export\/home/; is used to find 
# any instance of the word home in the file and replace it with export/home. The extra \ in the file is needed so that
# perl will ignore the following / and will treat that as a normal string instead of the expected command seperation. 
while (<INPUT>) {
chomp;
s/home/export\/home/;

#Here, the information that is going to be written will be printed to the user. The variable $_ is used to identify the last
# the last variable that perl has worked with. 
print "$_\n" ;

#Finally, the changes will be placed into the OUTPUT file. 
print OUTPUT "$_\n";
}

#Close is used here to close out the two files and tell the system that the memory used for these files can be reallocated.
close $OUTPUT;
close $INPUT;
