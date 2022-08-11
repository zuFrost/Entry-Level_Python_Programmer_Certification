#!/usr/bin/env python3.7
""" 
A typical Fizz-Buzz problem goes like this:

Write a program that prints the numbers from 1 - 100. 
For each multiple of three print "Fizz" instead of the number. 
For multiples of five print "Buzz" instead of the number. 
If a number is a multiple of three and five then print "FizzBuzz".

Solving this problem requires 2 key components: looping and conditionals. 
We're going to write a simplified program only using the conditional portion 
that will take any given number that we provide and print the Fizz-Buzz value. 
Here's how it will work:

$ ./fizz-buzz-item.py
Enter an integer value: 15
FizzBuzz
$ ./fizz-buzz-item.py
Enter an integer value: 21
Fizz
$ ./fizz-buzz-item.py
Enter an integer value: 17
17
"""
number = int(input("Enter an integer value from 1 - 100: "))
#print("Your number is: ", number)
#For each multiple of three print "Fizz"
if (number % 3) == 0:
    fizz_flag = True
else:
    fizz_flag = False
#print("fizz-flag is: ", fizz_flag)

if (number % 5) == 0:
    buzz_flag = True
else:
    buzz_flag = False
#print("buzz-flag is: ", buzz_flag)    

if fizz_flag & buzz_flag:
    print("FizzBuzz")
elif fizz_flag:
    print("Fizz")
elif buzz_flag:
    print("buzz")
else:
    print(number)
