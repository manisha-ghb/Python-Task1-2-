# Question - 2b - 3
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


# Question - 2b - 4
def printing():
    for i in range(1,101):
        if i%3 ==0 and i%5==0:
            print(i)
printing()


# Question - 2a - 4
def table(num):
    for j in range(1,num+1):
        for i in range(1,21):
            print(j,"*",i,"=",j*i)
# table(10)
table(10)