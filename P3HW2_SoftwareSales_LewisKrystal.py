#Software Sales
#CTI-110 P3HW2
#Krystal Lewis
#7/24/2018

#Ask user for number of packages
numberPackages = int(input("Please enter the number of packages bought: "))

#Ask user for price per package
packagePrice = 99

if numberPackages < 10:
    discountRate = 0;
elif numberPackages < 20:
    discountRate = 0.10;
elif numberPackages < 50:
    discountRate = 0.20;
elif numberPackages < 100:
    discountRate = 0.30;
else:
    discountRate = 0.40

#Get subtotal
subTotal = numberPackages * packagePrice

#Get discount amount
discountAmount = discountRate * subTotal

#Get overall total of sale
total = subTotal - discountAmount

print("Amount of discount: $", discountAmount)
print("Total amount: $", total)


