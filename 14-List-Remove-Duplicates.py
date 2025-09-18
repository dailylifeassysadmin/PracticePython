# List Remove Duplicates

# Exercise 14 (and Solution)
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

# listn = [1, 1, 2, 3, 4, 4, 5, 5, 6]
listn = [1, 2, 3, 4, 5, 6, 23422, 243, 234, 23, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# This is first way of removing duplicate elements.
print(list(set(listn)))

# This is second way of removing the duplicate elements.
output_list = []
for item in listn:
    if item not in output_list:
        output_list.append(item)
print(output_list)

# End of Program