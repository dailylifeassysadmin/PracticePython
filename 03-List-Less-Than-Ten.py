#List Less Than Ten

# Exercise 3 (and Solution)
# Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for elements in a:
    if elements <= 5:
        print(elements)

#Extras Task:
#1
new_list = []

for elements in a:
    if elements <= 5:
        new_list.append(elements)

print(new_list)

#2
new_list2 = [elements for elements in a if elements <= 5]

print(new_list2)

#3

num = int(input("Please input a number: "))
for elements in a:
    if elements <= num:
        print(elements)

# End of program.