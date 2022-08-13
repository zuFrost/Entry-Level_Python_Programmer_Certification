#!/usr/bin/env python3.7

""" 
The range function returns an iterable object that makes it incredibly easy to iterate 
through a large list of integers without needing to create the list up front. In this hands-on lab, 
we're going to create the char_range generator that will do the same thing, 
except it will provide us with a range of characters based on Unicode code points 
for the starting character and ending character, with an optional step value.

Here's our ideal usage in the REPL with a for loop and turning the generator into a list:

>>> for char in char_range('a', 'e'):
...     print(char)
...
a
b
c
d
e
>>> list(char_range('a', 'e', 2))
['a', 'c', 'e']
>>> list(char_range('e', 'a', 2))
  'e', 'c', 'a']
Notice that we're able to handle the case where the starting code point is larger 
than the ending code point. In these situations, we'll need to change the step value 
to be a negative number. Additionally, unlike the range function, 
we want the result of char_range to include the stop character instead of omitting it.

We'll be implementing the char_range function in the using-generators.py file, 
and we can see if our implementation meets the expectations by running the file 
through the Python interpreter:

$ python3.7 using-generators.py
Traceback (most recent call last):
  File "using-generators.py", line 12, in <module>
    char_range
NameError: name 'char_range' is not defined
If we run into an expectation that we don't meet, then the error should explain 
what is expected compared to what is happening.
"""

# Define the `char_range` generator here
#>>> ord("a")
#97
#>>> chr(97)
#'a'
def char_range(first_char, last_char, step=1):
    i = ord(first_char)
    while i <= ord(last_char):
        yield chr(i)
        i += 1

# Tests to verify the implementation of char_range
# *Do not modify
##################################################

# Ensure that `char_range` is a generator function
from inspect import isgeneratorfunction

assert isgeneratorfunction(
    char_range
), f"Expected char_range to be a generator function but was not."

# Ensure that the result *does* includes the stop character
assert list(char_range("a", "e")) == [
    "a",
    "b",
    "c",
    "d",
    "e",
], f"Expected ['a', 'b', 'c', 'd', 'e'] but got {repr(list(char_range('a', 'e')))}"

# Iterate backwards if the start code point is higher than the stop code point

assert list(char_range("e", "a")) == [
    "e",
    "d",
    "c",
    "b",
    "a",
], f"Expected ['e', 'd', 'c', 'b', 'a'] but got {repr(list(char_range('e', 'a')))}"

# Properly step if a step value is provided

assert list(char_range("a", "e", 2)) == [
    "a",
    "c",
    "e",
], f"Expected ['a', 'c', 'e'] but got {repr(list(char_range('a', 'e', 2)))}"

# Step properly if the start code point is higher than the stop code point

assert list(char_range("e", "a", 2)) == [
    "e",
    "c",
    "a",
], f"Expected ['e', 'c', 'a'] but got {repr(list(char_range('e', 'a', 2)))}"

