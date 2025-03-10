#q-1: Print the first 10 terms of the Fibonacci series using a for loop.
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b

#or
num1, num2 = 0, 1
print(num1)
print(num2)
for i in range(0,13):
    temp = num1 + num2
    print(temp)
    num1 = num2
    num2 = temp
#q-2: Check if a given number is a prime number using a for loop.
num1 = int(input("Enter a number to check for prime"))
#approach 1
if num1 in [0,1] or num1 < 0:
    print("neither prime nor composite")
else:
    count = 0
    for i in range(1, num1+1):
        if num1 % i == 0:
            count += 1

    print("prime") if count == 2 else print("not a prime")

#approach 2
if num1 in [0,1] or num1 < 0:
    print("neither prime nor composite")
else:
    spy = True
    for i in range(2, num1):
        if num1 % i == 0:
            spy = False
            print("Not a prime")
            break
    if spy:
        print("prime")
            
#approach 3
if num1 in [0,1] or num1 < 0:
    print("neither prime nor composite")
else:
    spy = True
    for i in range(2, num1 // 2 + 1):
        if num1 % i == 0:
            spy = False
            print("Not a prime")
            break
    if spy:
        print("prime")

#approach 4
if num1 in [0,1] or num1 < 0:
    print("neither prime nor composite")
else:
    spy = True
    for i in range(2, int(num1 ** 0.5) + 1):
        if num1 % i == 0:
            spy = False
            print("Not a prime")
            break
    if spy:
        print("prime")



#q-3: Write a program to calculate the factorial of a number using a while loop.
def factorial(number):
    if number>=0:
        fact = 1
        start = 1
        while start<number:
            start +=1
            fact*=start
        return fact
    return "Invalid input"
print(factorial(5))
print(factorial(0))
print(factorial(-5))
#q-4: Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.
def printing():
    for i in range(1,101):
        if i%3 ==0 and i%5==0:
            print(i)
printing()
#q-5: Implement a menu-driven program where the user can choose to: 1. Find the square of a number. 2.Find the cube of a number 3.Exit.

#q-6: Implement a basic login system where the user has three attempts to enter the correct password using a loop.