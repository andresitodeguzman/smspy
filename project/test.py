
#
# TEST
# The cli testing module for interacting with the program
# 
# Andresito M. de Guzman
# 

# import the process
import process

# sets the number randomly
number = str(1234)

# ask for input
body = input("Text: ")

# sends data to process
response = process.process(number, body)

# prints the response
print(response)
