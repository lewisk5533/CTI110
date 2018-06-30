#Distance, Speed, and Time
#Krystal Lewis
#6/30/2018

#Define the main method

def main():
    calculateValue()

def calculateValue():
    #Get the speed of vehicle
    for speed in range(1):
        print("What is the speed of vehicle?")
        speed = int(input()) 
        #Get the time traveled
        for time in range(1):
            print("How many hours has it traveled?")
            time = int(input())

    #Multiply speed and time
    distance = speed * time 
    print("You've traveled a total of", distance, "miles")

#Use a while loop to control how many time main() will be called 
choice = 'y'
while choice == 'y':
    main()
    choice = input("Do you want to run the program again? y or n")
main()


