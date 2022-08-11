#!/usr/bin/env python3.7

""" 
Our script variations.py will allow us to provide a string and then it will present us with some permutations (all lowercase, all uppercase, etc), of that string. 
The script will also tell us the string's first and last words, when they are sorted alphabetically. 
We'll need to utilize numerous methods on the str class and some of the functions used to sort lists to make all of this this happen. 
Here's how we want the script to be used:

$ ./variations.py
Enter a message: This is my message
Lowercase: this is my message
Uppercase: THIS IS MY MESSAGE
Capitalized: This is my message
Title Case: This Is My Message
Words: ['This', 'is', 'my', 'message']
Alphabetic First Word: is
Alphabetic Last Word: This
"""

# Enter a message: This is my message
work_str = input("Enter a message: ")
#print(work_str)

# Test string for debaging
#test_str = "This is my message"
#print(test_str)

# Lowercase: this is my message
#print("Lowercase: " + test_str.lower())
print("Lowercase: " + work_str.lower())

# Uppercase: THIS IS MY MESSAGE
#print("Uppercase: " + test_str.upper() )
print("Uppercase: " + work_str.lower())

# Capitalized: This is my message
#print("Capitalized: " + test_str.capitalize())
print("Capitalized: " + work_str.capitalize())

# Title Case: This Is My Message
#print("Title Case: " + test_str.title())
print("Title Case: " + work_str.title())

# Words: ['This', 'is', 'my', 'message']
#print("Words: ",  test_str.split())
print("Words: ",  work_str.split())

# Alphabetic First Word: is
#words_list = test_str.split()
#print("Alphabetic First Word: ",  sorted( words_list )[0])
words_list = work_str.split()
print("Alphabetic First Word: ",  sorted( words_list )[0])

# Alphabetic Last Word: This
#print("Alphabetic Last Word: ",  sorted( words_list )[-1])
print("Alphabetic Last Word: ",  sorted( words_list )[-1])