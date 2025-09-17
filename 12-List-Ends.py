# List Ends

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]

def list_ends(lst):
    if len(lst) < 2:
        return "List must contain at least two elements."
    return [lst[0], lst[-1]]

result = list_ends(a)
print(result)  # Output: [5, 25]

# End of program