#Character Input
from datetime import datetime

#Taking input from user for his or her name.
name = input("What is your name: ")
#print(name)

#Taking input from user for his or her age and converting it in integer.
age = int(input("What is your age: "))
#print(age)

#Identifying how much year is remain in that human.
remaining_age = 100-age

#Identifying the current year
current_year = datetime.now().year

#Future year, in which user is going to be 100 years old.
future_year = current_year+remaining_age

print(name + ", will be 100 years old in year: "+ str(future_year))

# End of the program.