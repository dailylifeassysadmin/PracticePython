# Check Primality Functions

# Exercise 11 (and Solution)

# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

range_end = int(input("Enter the ending range: "))

for i in range(1, range_end + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                #print(i, "is not a prime number")
                break
        else:
            print(i, "is a prime number")
    # else:
    #     print(i, "is not a prime number")


# Solution

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
# Exercise 12 (and Solution)
# Ask the user for a number and determine whether the number is prime or not using a function called is_prime that takes one argument (the number to be checked) and returns True if the number is prime and False otherwise.   Use this function to check whether the numbers 1-20 are prime.
# for num in range(1, 21):
#     if is_prime(num):
#         print(f"{num} is a prime number.")
#     else:
#         print(f"{num} is not a prime number.")
# Exercise 13 (and Solution)
# Ask the user for a number and determine whether the number is prime or not using a function
# called is_prime that takes one argument (the number to be checked) and returns True if the number is prime and False otherwise.   Use this function to check whether the numbers 1-20 are prime.  If they are, store them in a list called primes.
primes = []
for num in range(1, 21):
    if is_prime(num):
        primes.append(num)
print("Prime numbers between 1 and 20 are:", primes)
# Exercise 14 (and Solution)
