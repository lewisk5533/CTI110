#Program to ask user for nonnegative integer
#CTI-110
#Krystal Lewis
#7/20/2018

#Determine integer
userInteger = int(input("Enter a nonnegative integer: "))

#Create while loop
while userInteger < 1:
    userInteger = int(input("Please enter a positive number: "))

factorial = 1

#Calculate Factorial
for number in range(1, userInteger + 1):
    factorial = factorial * number
    
print("the factorial of", userInteger, "is", factorial)
    


