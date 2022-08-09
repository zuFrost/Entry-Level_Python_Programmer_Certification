name = input("What is your name? ")
color = input("What is your favorit color? ")
age = int(input("Haw old are you today? "))

#NAME is AGE years old and loves the color COLOR.

#1st variant
# print(name)
# print("is " + str(age) + " years old")
# print("and loves the color " + color + ".")

#2st variant
print(name, end=" ")
print("is " + str(age) + " years old", end=" ")
print("and loves the color " + color + ".", end=" ")