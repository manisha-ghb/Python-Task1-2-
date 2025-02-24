#17feb-2025
#problem solving
#3 Things-33%(understanding the question carefully)
#algorithm-3%
#how to code it in programming language
#bonus - edge cases
#code quality


#19feb,2025
#if else and if else ladder
#Easy QUestions
#q-1:write a program to check if a given number is positive ,negative or zero.
def number(num):
    if num>0:
        print("positive")
    else:
        if num<0:
            print("negaitve")
        else:
            print("zero")    

number(2)
number(-1)
number(0)

#q-2:determine if a number is odd or even.
def num(num1):
    if num1%2==0:
        print("Even")
    else:
        print("odd")
num(3)
num(2)
#or
# res = "even" if num1%2==0 else "odd"
# print(res)

#q-3:check if a person is eligible to vote(age>=18).
def votes(age):
    if age>=18:
        print("eligible")
    else:
        print("not eligible")
votes(18)
votes(16)
#or
# res="eligible" if age >== 18 else "not eligible"
# print(res)

#q-4:write a prgm to find the greatest of two numbers.
def greatestOfTwoNumber(num1,num2):
    if num1>num2:
        return num1
    return num2
print(greatestOfTwoNumber(2,3))
#(or)
def greatestOfTwoNumbers(a,b):
    if a>b:
        print("a is greater than b")
    else:
        print("a is less than b")

greatestOfTwoNumbers(2,3)
greatestOfTwoNumbers(5,3)

#q-5:print "pass" if a student scores more than 40marks; otherwise, print "fail"
def student(marks):
    if marks>40:
        print("pass")
    else:
        print("fail")

student(50)
student(39)

#q-6: write a program to display the day of the week based on a number input(1 for monday, 2 for tuesday, etc..)
def week(day):
    if day==1:
        print("Monday")
    elif day==2:
        print("tuesday")
    elif day==3:
        print("wednesday")
    elif day==4:
        print("thursday")
    elif day==5:
        print("friday")
    elif day==6:
        print("saturday")
    elif day==7:
        print("sunday")
    else:
        print("Invalid")

week(7)

#q-7:implement a simple calculator to perform addition, subtraction, multiplication and division
operation = input("enter operation to perform").lower()
num1=int("enter first number")
num2=int("enter second number")

if operation == 'add':
    print(num1 + num2)
elif operation == 'sub':
    print(num1 - num2)
elif operation == 'mul':
    print(num1 * num2)
elif operation == 'div':
    if num2 == 0:
        print("Division not possible")
    else:
        print(num1 / num2)

#q-8:write a program to display the name of a month based on the month number(1 for jan, 2for feb, etc..)
def monthName(month):
    if month==1:
        print("january")
    elif month==2:
        print("feb")
    elif month==3:
        print("march")
    elif month==4:
        print("april")
    elif month==5:
        print("may")
    elif month==6:
        print("june")
    elif month==7:
        print("july")
    elif month==8:
        print("aug")
    elif month==9:
        print("sep")
    elif month==10:
        print("oct")
    elif month==11:
        print("nov")
    elif month==12:
        print("dec")
    else:
        print("invalid")

monthName(2)
monthName(6)

#medium questions
#q-3:write a prgm to classify a character entered by the user as a vowels, comsonants or neither
char = input("enter  a single character").lower()
if len(char) not in [1]:
    print("invalid string")
else:
    if char in ['a','e','i','o','u']:
        print("vowels")
    else:
        print("consonants")
#or
char = input("enter  a single character").lower()
if len(char) not in [1]:
    print("invalid string")
else:
    if char in ['a','e','i','o','u']:
        print("vowels")
    elif char.isalpha(): #isalpha-returns true if character is only alphabet, otherwise it returns false
        print("consonants")
    else:
        print("other or special character")


