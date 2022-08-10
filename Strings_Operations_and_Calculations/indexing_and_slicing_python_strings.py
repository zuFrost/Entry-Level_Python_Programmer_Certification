#!/usr/bin/env python3

"""
Create the string-info.py Script and Take User Input
Print the First, Last, and Middle Characters from the User's Input
Print the Even Index Characters and Odd Index Characters
Print the String in Reverse
"""

"""
We're going to write a script that takes user input, so that we're not working with static content, and print out some information and permutations of the string that the user has entered. Our string-info.py script will print the following information about the user provided message:

The first character
The last character
The middle character (for even length strings we'll return the integer just after the exact center).
Every even index character
Every odd index character
The message in reverse

Here's our script in action:

$ python3.7 string-info.py
Enter a message: Test Message
First character: T
Last character: e
Middle character: e
Even index characters: Ts esg
Odd index characters: etMsae
Reversed message: egasseM tseT
"""
work_str = input("Enter a message: ")
# print(work_str)
# First character: T
print('First character: ', work_str[0])
# Last character: e
print('Last character: ', work_str[-1])
# Middle character: e
print('Middle character: ', work_str[int((len(work_str)/2)) ])
# Even index characters: Ts esg
print('Even index characters: ', work_str[::2])
#Odd index characters: etMsae
print('Odd index characters: ', work_str[1::2])
#Reversed message: egasseM tseT
print('Reversed message: ', work_str[::-1])
