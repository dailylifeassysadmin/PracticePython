# Reverse Word Order
# strings
# Exercise 15 (and Solution)
# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:

# My name is Michele
# Then I would see the string:

# Michele is name My
# shown back to me.

word = input("Enter a long string containing multiple words: ")
result = word.split(" ")

# print(result.reverse())

new_result = []

for i in range(1, len(result)+1):
    new_result.append(result[-i])
    # new_result = new_result[0:0:-1]

# print("newresult:", new_result)
new_result = " ".join(new_result)
print(new_result)

# new_result[0:]
# print("Newdata", new_result[::-1])
# result = result[-1]
# print(result)

# Using functions as part of the solution.

def reverse_word_order(word):
    result = word.split(" ")
    new_result = []
    for i in range(1, len(result)+1):
        new_result.append(result[-i])
    new_result = " ".join(new_result)
    return new_result

print(reverse_word_order(word))

# print("Reversed word order:", reverse_word_order(word))
# End of program