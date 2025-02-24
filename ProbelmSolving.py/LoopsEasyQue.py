##loops
#Easy Questions

#q-1: Print all numbers from 1 to 100 using a for loop.
for i in range(1,101):
    print(i)

#q-2:Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)
def sum_of_natural_numbers(n):
    return n*(n+1)//2
print(sum_of_natural_numbers(2));


#q-3: Print all even numbers between 1 and 50 using a while loop.
num=2
while num<=50:
    print(num)
    num+=2

#q-4:write a program to display the multiplication table of a given number. first 20.
num = int(input("Enter a number: "))
for i in range(1, 21):
    print(f"{num} x {i} = {num * i}")
#or
def multiplication(n):
    for i in range(1,21):
        print(f"{n} x {i} = {n*i}")
multiplication(5)

#q-5:Reverse a number using a while loop. also can we get the sum of all the digits.
num = int(input("Enter a number: "))
reversed_num = 0
sum_of_digits = 0
while num > 0:
    digit = num % 10         
    reversed_num = reversed_num * 10 + digit  
    sum_of_digits += digit    
    num = num // 10     
print(f"Reversed Number: {reversed_num}")
print(f"Sum of Digits: {sum_of_digits}")

#q-6:write a program to count the number of digitd in a given number using a while loop.
num = int(input("Enter a number: "))
digit_count = 0
num = abs(num)
while num > 0:
    num = num // 10  
    digit_count += 1  
if digit_count == 0:
    digit_count = 1
print(f"The number of digits is: {digit_count}")

#q-7: write a program that keeps asking the user to enter numbers until they enter a negative number. use a while loop.
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        print("You entered a negative number, exiting the loop.")
        break
    print(f"You entered {num}, which is positive.")