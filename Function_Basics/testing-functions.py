#!/usr/bin/env python3.7

""" 
Functions are one of the fundamental building blocks for writing well-factored, 
understandable code. Another benefit of functions is that we're able to package up code 
so that we don't need to think about the actual logic within the function. 
We can focus on the results, depending on our inputs. 
Viewing our functions as black boxes where we provide inputs and receive outputs 
means that we can also write automated tests to ensure that our functions 
(which might not even be written yet) behave the way that we expect. 
This is known as Test-Driven Development. We can use the assert statement 
to write some basic "tests" that utilize a function and ensure that the output is what we expect. 
We're going to work through the testing-functions.py file, 
writing and modifying functions to get the assertions throughout the file so that it doesn't throw errors.

When we run the testing-functions.py file we should see errors like this:

$ python3.7 testing-functions.py
Traceback (most recent call last):
  File "testing-functions.py", line 3, in <module>
    assert split_name("Kevin Bacon") == {
NameError: name 'split_name' is not defined
This process will show us the line where the issue was encountered, and show us the differences between our expected and actual values.
"""

def split_name(name):
    split_name_dict = {"first_name": "", "last_name": ""}
    split_name_dict.update({"first_name": name.split()[0]})
    if len(name.split()) == 2:
        split_name_dict.update({"last_name": name.split()[1]})
    elif len(name.split()) == 3:
        split_name_dict.update({"last_name": name.split()[1] + " " + name.split()[2]})
    else:
         ()   
    return split_name_dict


# 1) Write a `split_name` function that takes a string and returns a dictionary with first_name and last_name

assert split_name("Kevin Bacon") == {
    "first_name": "Kevin",
    "last_name": "Bacon",
}, f"Expected {{'first_name': 'Kevin', 'last_name': 'Bacon'}} but received {split_name('Kevin Bacon')}"

# 2) Ensure that `split_name` can handle multi-word last names

assert split_name("Victor Von Doom") == {
    "first_name": "Victor",
    "last_name": "Von Doom",
}, f"Expected {{'first_name': 'Victor', 'last_name': 'Von Doom'}} but received {split_name('Victor Von Doom')}"


#print(int(my_str))
#print(str(my_num))


def is_palindrome(string):
    #if string.isdigit(): #not correct AttributeError: 'int' object has no attribute 'isdigit'
    if isinstance(string, int):
        dig_to_str = str(string)
        return (list(reversed(dig_to_str)) == list(dig_to_str))
    elif isinstance(string, str):
        return (list(reversed(string)) == list(string))
    
# 3) Write an `is_palindrome` function to check if a string is a palindrome (reads the same from left-to-right and right-to-left)


assert is_palindrome("radar") == True, f"Expected True but got {is_palindrome('radar')}"
assert is_palindrome("stop") == False, f"Expected False but got {is_palindrome('stop')}"

# 4) Make `is_palindrome` work with numbers

assert is_palindrome(101) == True, f"Expected True but got {is_palindrome(101)}"
assert is_palindrome(10) == False, f"Expected False but got {is_palindrome(10)}"

# 5) Write a `build_list` function that takes an item and a number to include in a list
def build_list(string, num=1):
    i = 1
    my_list = []
    while i <= num:
        my_list.append(string)
        i += 1
    return my_list


assert build_list("Apple", 3) == [
    "Apple",
    "Apple",
    "Apple",
], f"Expected ['Apple', 'Apple', 'Apple'] but received {repr(build_list('Apple', 3))}"
assert build_list("Orange") == [
    "Orange"
], f"Expected ['Orange'] but received {repr(build_list('Orange'))}"
