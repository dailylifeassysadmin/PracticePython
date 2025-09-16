# Fibonacci

# Exercise 13 (and Solution)
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
 

# n = int(input("type: "))

# listn = [0, 1, 1]

# if n == 0:
#     print([0])

# elif n == 1:
#     print([0,1])

# elif n ==2:
#     print([0, 1, 1])

# else:
#     for i in range(3, n + 1):
#         listn.append(listn[-2]+listn[-1])

#     print(listn)

# End of program

listn = [0, 1, 1]

def fibonacci_numbers(n):

    
    if n == 0:
        print([0])

    elif n == 1:
        print([0,1])

    elif n ==2:
        print([0, 1, 1])

    else:
        for i in range(3, n + 1):
            listn.append(listn[-2]+listn[-1])

        return(listn)

    #return(listn)

print(fibonacci_numbers(int(input("type: "))))

# End of program as a function
