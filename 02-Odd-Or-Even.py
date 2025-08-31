#Odd Or Even

print("This program will check, if the given number is odd or even.")

#Taking input from user for his or her desired number.
num = int(input("Please provide a number: "))

#Checking with if statement that given number is fully divisible or not and based on that identifying the Odd and Even number.
if num%2==0 and num!=0:
    print("The given number is Even.")
elif num==0:
    print("The number is zero.")
else:
    print("The given number is Odd.")


# End of the program.