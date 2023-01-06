
#
# TEST
# The cli testing module for interacting with the program
# 
# Andresito M. de Guzman
# 

# import the process
import os
import process

# sets the number randomly
number = str(1234)

# clears screen (for posix)
# os.system('clear')

# ask for input
body = input("Text: ")

# sends data to process
response = process.process(number, body)

# Prints the response
print('Response: ' + response)