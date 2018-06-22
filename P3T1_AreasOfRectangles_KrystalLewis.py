# Area of two rectangles
#Krystal Lewis
#6/22/2018

#Get the length and width of rectangle 1
length1 = int(input("Enter the length of rectangle 1: "))
width1 = int(input("Enter the width of rectangle 1: "))

#Get the length and width of rectangle 2
length2 = int(input("Enter the length of rectangle 2: "))
width2 = int(input("Enter the width of rectangle 2: "))

#Calculate the area of rectangles.
area1 = length1 * width2
area2 = length2 * width2

#Determine which has the greater area. 

if area1 > area2:
    print("Rectangle 1 has the greatest area.")

elif area2 > area1:
    print("Rectangle 2 has the greatest area.")

else:
    print("Both rectangles have the same area.")
    
