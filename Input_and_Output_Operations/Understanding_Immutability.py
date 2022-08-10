my_str = 'testing'
print(my_str)
print(my_str.capitalize())
print(id(my_str))
print(id(my_str.capitalize()))
print(id('testing'))
other_str = my_str
print(id(other_str))
print(id(other_str) == id(my_str))
