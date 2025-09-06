# Divisors

# Exercise 4 (and Solution)
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If 
# you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input("Please input a number: "))
divisors = []
for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)
print(divisors)
# End of program.
# Extras:
# 1. Ask the user for a second number and print out all the common divisors
num2 = int(input("Please input a second number: "))
common_divisors = []
for i in range(1, min(num, num2) + 1):
    if num % i == 0 and num2 % i == 0:
        common_divisors.append(i)

print("Common divisors:", common_divisors)
# 2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
common_divisors_one_liner = [i for i in range(1, min(num, num2) + 1) if num % i == 0 and num2 % i == 0]
print("Common divisors (one-liner):", common_divisors_one_liner)
# 3. Find the largest common divisor between the two numbers
if common_divisors:
    largest_common_divisor = max(common_divisors)
    print("Largest common divisor:", largest_common_divisor)
else:
    print("No common divisors found.")
# End of program.
# End of program.