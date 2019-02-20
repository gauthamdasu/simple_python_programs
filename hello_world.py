#Hi this is a sample hello world program which takes name as input and prints the name as output in python
# here '#' stands for single comment .
import sys
'''
you can use ''' ''' for commenting multiple lines.
'''
if sys.version_info[0] < 3:
	name = raw_input("Hello what is your name?\n") # take input from the user through the string 'name'
	print ("Hello "+ name + " ")
	print ("You are using python version below 3\n")
else :
	name = input("Hello what is your name?\n") # take input from the user through the string 'name'
	print("Hello "+ name + " ")
	print ("You are using python version above 3\n")
