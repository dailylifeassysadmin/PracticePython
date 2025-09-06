# List Overlap

# Exercise 5 (and Solution)
# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list2 = []

for i in a:
    if i in b:
        list2.append(i)
        #print(i)

#list = list(set(list))
print(list(set(list2)))
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# list = []

# Extras:
# 1st method
# Randomly generate two lists to test this

import random
a = random.sample(range(1, 50), 10)
b = random.sample(range(1, 40), 10)
# print(a)
# print(b)

new_list = []

for i in a:
    if i in b:
        new_list.append(i)

print(list(set(new_list)))

# 2nd method
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

print(list(set([i for i in a if i in b]))) # List comprehension method

print(list(set(a) & set(b)))  # Another method using set intersection

# print(list(set(a).intersection(set(b))))  # Another method using set intersection
print(list(set(a).intersection(b)))  # Another method using set intersection
# print(list(set(b).intersection(a)))  # Another method using set intersection

# End of program.