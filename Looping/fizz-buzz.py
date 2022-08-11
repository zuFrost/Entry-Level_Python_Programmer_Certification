#!/usr/bin/env python3.7
""" 
A typical Fizz-Buzz problem goes like this:

Write a program that prints the numbers from 1 - 100. 
For each multiple of three print "Fizz" instead of the number. 
For multiples of five print "Buzz" instead of the number. 
If a number is a multiple of three and five then print "FizzBuzz". 
Solving this problem requires 2 key components: looping and conditionals.

We're going to write a script that prompts the user for the number of items to process (starting with 1). 
For each number, we'll print either "Fizz", "Buzz", "FizzBuzz", or the number. 

The criteria for what to print is:

Print "FizzBuzz" if the number is divisible by 3 and 5.
Print "Fizz" if the number is divisible by 3.
Print "Buzz" if the number is divisible by 5.
Otherwise print the number.
Here's how the final script should work:

$ ./fizz-buzz.py
How many values should we process: 20
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
"""

#prompts the user for the number of items to process (starting with 1)
number = int(input("Input number of items to process (starting with 1): "))
#print(number)

for i in range(1,number+1):
#    print(i)
#Print "FizzBuzz" if the number is divisible by 3 and 5.
    if (i % 3 == 0) & (i % 5 == 0):
        print("FizzBuzz")
#Print "Fizz" if the number is divisible by 3.
    elif (i % 3 == 0):
        print("Fizz")
#Print "Buzz" if the number is divisible by 5.        
    elif (i % 5 == 0):
        print("Buzz")
#Otherwise print the number.
    else:
        print(i)

