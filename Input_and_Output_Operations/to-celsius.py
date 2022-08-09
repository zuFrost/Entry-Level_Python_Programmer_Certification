#!/usr/bin/env python3

# Python implementation here
fahrenheit = input("What temperature (in Fahrenheit) would you like converted to Celsius? ")
fahrenheit = float(fahrenheit)
celsius = (fahrenheit - 32) / 1.8
print(fahrenheit, 'F is',  round(celsius, 2), "C")