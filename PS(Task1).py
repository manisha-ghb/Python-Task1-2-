#PS day-1 assignment
#medium questions(if else and elif)

####q-1:write a prgm to find the greatest of three numbers.
def find_greatest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
greatest = find_greatest(num1, num2, num3)
print(f"The greatest number is: {greatest}")

#or

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
greatest = max(num1, num2, num3)
print(f"The greatest number is: {greatest}")


####q-2:check if a year is a leap year.
year = int(input("Enter a year: "))
if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#or--using function

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


####q-4:Calculate the grade of a student based on the marks they score:
# 1. 90-100: Grade A
# 2. 80-89: Grade B
# 3. 70-79: Grade C
# 4. <70: Fail.
marks = float(input("Enter the marks: "))
if 90 <= marks <= 100:
    grade = "Grade A"
elif 80 <= marks < 90:
    grade = "Grade B"
elif 70 <= marks < 80:
    grade = "Grade C"
else:
    grade = "Fail"
print(grade)

#or--using functions

def grades(mark):
    if 90 <= mark<=100:
        print("Grade A")
    elif 80 <= mark < 90:
        print("Grade B")
    elif 70 <= mark < 80:
        print("Grade C")
    else:
        print("Fail")
grades(70)
grades(100)
grades(80)


####q-5:Write a program to check if three sides length form a valid triangle.
side1 = float(input("Enter length of first side: "))
side2 = float(input("Enter length of second side: "))
side3 = float(input("Enter length of third side: "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")

#or--using functions

def traingle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        print("The sides form a valid triangle.")
    else:
        print("The sides do not form a valid triangle.")
traingle(6, 7, 3)
    
