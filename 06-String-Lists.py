# String Lists

# Exercise 6 (and Solution)
# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

word = input("Enter a word: ")

upper_word = word.lower()

if upper_word == upper_word[::-1]:
    print(f"{upper_word} is a palindrome")
else:
    print(f"{upper_word} is not a palindrome")
# Exercise 6a (and Solution)
# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards. Do not ignore spaces, punctuation and capitalization)

# End of programMadam