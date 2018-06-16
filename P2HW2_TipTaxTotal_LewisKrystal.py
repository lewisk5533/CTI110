#CTI-110
#P2HW2 - Tip Tax Total
#Krystal Lewis
#6/16/2018

#This program calculates the total cost of a meal purchased at a restuarant

#Calculate the food cost 
print("Find total food cost")
food = float(input("food: "))
tax = float(input("salesTax: "))
print("Total Amount: ", food * tax + food)

#Calculate the tip amount
print("Find the tip amount")
totalAmount =float(input("Total Amount: "))
tipCost = float(input("tip: "))
print("Tip Amount: ", totalAmount * tipCost)

#Calculate the total cost
print("Find total cost of meal")
totalAmount = float(input("Total Amount: "))
tipAmount = float (input("Tip Amount: "))
print("Total Cost: ", totalAmount + tipAmount)




