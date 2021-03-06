# Script Name	: check_file.py
# Author		: Craig Richards
# Created		: 20 May 2013 
# Last Modified	: 
# Version		: 1.0

# Modifications	: with statement added to ensure correct file closure

# Description	: Check a file exists and that we can read the file

import sys		# Import the Modules
import os		# Import the Modules

# Readfile Functions which open the file that is passed to the script

def readfile(filename):
	with open(filename, 'r') as f:      # Ensure file is correctly closed under all circumstances
	                                #as far as I can tell, line 17 is another way of writing f = open(filename, 'r')
	    line = f.read()             #we are reading the whole file in the read() function
	print line                      #we are printing the whole file

def main():             #so we are calling the script with the filename
  if len(sys.argv) == 2:		# Check the arguments passed to the script
    filename = sys.argv[1]		# The filename is the first argument , i think the script name is the zeroth argument
    if not os.path.isfile(filename):	# Check the File exists, in this directory
      print '[-] ' + filename + ' does not exist.'  
      exit(0)                   # exit if we don't find the file
    if not os.access(filename, os.R_OK):	# Check you can read the file, do I have access??????
      print '[-] ' + filename + ' access denied'  #if I dont have access we exit
      exit(0)
  else:
    print '[-] Usage: ' + str(sys.argv[0]) + ' <filename>' # Print usage if not all parameters passed/Checked, I don't really understand
    exit(0)                                 
  print '[+] Reading from : ' + filename	# Display Message and read the file contents
  readfile(filename)                #we finally read the file.
  
if __name__ == '__main__':   #since this file is being used as main since its not being imported by another file, the __name__ is the 
  main()                     #execution file name. this will be true as long as this file isn't being imported.
                             #THIS PROGRAM WORKS AS INTENDED! 
