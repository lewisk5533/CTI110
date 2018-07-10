#Grade Average
#7/10/2018
#CTI-110 P5HW1 - Test Average Grade
#Krystal Lewis
#

def main():
    number = getInput()
    ave = calc_average(number)
    determine_grade(ave)

def calc_average(number):
    total = 0
    for x in range(1, number + 1):
        grade = float(input("Enter grade: "))
        total = total + grade

    ave = total / number
    return ave

def determine_grade(ave):
    if ave > 89 and ave < 101:
        print("You made an A!")
    elif ave > 79 and ave < 90:
        print("You made a B!")
    elif ave > 69 and ave < 80:
        print("You made a C!")
    elif ave > 59 and ave < 70:
        print("You made a D!")
    elif ave >= 0 and ave < 60:
        print("You made an F!")
    else:
        print("Invalid input. Try again.")

def grade():
    grade = gradeOne + gradeTwo + gradeThree + gradeFour + gradeFive
    return grade

def getInput():
    num = int(input("How many grades would you like to enter? "))
    return num

main()
