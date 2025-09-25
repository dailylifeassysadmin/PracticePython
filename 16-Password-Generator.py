# # Password Generator

# # Exercise 16 (and Solution)
# # Note: this is a 4-chili exercise, not because it introduces a concept, but because this exercise is more like a project. Feel free to skip this and come back when you’re more ready!

# # Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# # The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# # Extra:

# # Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random

lower_letter = 'abcdefghijklmnopqrstuvwxyz'
upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special_char = '''!"#$%&'()*+,-./:;<=>?@[]^'\\'_`{|}~'''

password_lis = []

# for i in range(12):
# 	password_lis.append(random.choice(special_char))

# -----------This is testing purpose-----------
# new_password = str("".join(password_lis))
# print(new_password)
# -----------Ending this testing block-----------

strength = input("Enter password strength (weak, medium, strong): ").lower()
length = int(input("Enter password length: "))

for i in range(length):
	if strength == "weak":
		password_lis.append(random.choice(lower_letter))
	elif strength == "medium":
		new_char = lower_letter + upper_letter
		password_lis.append(random.choice(new_char))
	elif strength == "strong":
		new_char = lower_letter + upper_letter + digits + special_char
		password_lis.append(random.choice(new_char))
	else:
		print("Invalid strength level. Choose 'weak', 'medium', or 'strong'.")

new_password = str("".join(password_lis))
print(new_password)