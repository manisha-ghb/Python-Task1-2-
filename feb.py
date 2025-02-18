# ##11th Feb

# # functions-it is a block of code which runs whenever we call it.
# #parameters and arguments
# #parameters- we can give variables in fuunction defination
# #Arguments- we can give variables in function call
# #positional arguments
# #keyword arguments
# #default arguments
# #return statements
# #syntax: def fuction-name(): (Statements)

# #example1
# def basic_function(a , b):   #parameters
#     print("hiee")
#     print("Good Morning , Hyd")
#     print(a + b)
#     print(a - b)
#     print(a * b)
#     print(a / b)
#     print(a % b)


# basic_function(3 , 6)   #Arguments-Positional arguments

# basic_function(9 , 8)

# basic_function(a=7 , b=6) #Keyword arguments

# #example2   ---default parameters
# def example_function(a , b , r , pie=3.14):
#     print("circle area")
#     print(pie * r * r)

# example_function( a=2 , b=4 , r=10 , pie=3.14)
# example_function(a=2 , b=2 , r=4)

# #example3
# # def example1_function(a , b , pie=3.14 , r):   #--parameter without a default follows parameter with a default
# #     print("hello")
# #     print(pie*r*r)

# # example1_function(b=2 , a=3 , r=4)

# #example4----return statements
# def example2_function(a , b , r=10 , pie=3.14):
#     print(a)
#     print(b)
#     return a + b

# res = example2_function(4, 5)
# print(res+3)

# def hello_function(a , b , r=5 , pie=3.14):
#     print("hello")
#     print(a)
#     print(b)
#     if(5<2):
#         return a-b
#     print(pie)
#     print(pie*r*r)

# res=hello_function(2, 3)


# def even_or_odd(num1):
#     if num1 % 2 == 0:
#         return "Even"
#     else:
#         return "odd"
# print(even_or_odd(50))

##12th Feb
# def hello_function(a , b , r=5 , pie=3.14):
#     print("hello")
#     print(a)
#     print(b)
#     if(5>2):
#         return a-b, a+b, a*b, a/b
#     print(pie)
#     print(pie*r*r)

# res=hello_function(2, 3)
# print(res)


# def sum(a,b):
#     print(a)
#     print(b)
#     return a+b
# res1=sum(4,5)
# print(res1)

# def sum(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#     return a+b+c
# res2=sum(2,3,4)
# print(res2)

# def sum(a, b, c, d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     return a+b+c+d
# res3=sum(3,4,5,6)
# print(res3)    

#Arbitary Arguments

# def sum(a , b):
#     return a+b
# def sum(a, b, c):
#     return a+b+c
# def sum(a, b, c, d):
#     return a+b+c+d

# res=sum(2,3)
# res=sum(2,3,4)
# res=sum(2,3,4,5)
# def sum(a, *b):
#     print(a)
#     print(b)
# sum(1,2,3,4,5,6,7,8,9)


# def sum(a, *b):
#     res = a
#     for k in b:
#         res += k
#     print(res)

# sum(1,2,3,4,5,6,7,8,9)

#Keywords Arbitary Arguments
# def sum(**kargs):
#     print(type(kargs))
#     print(kargs)
# sum(num0=1, num1=2, num2=3, num3=4, num4=5)

# def sum(**kargs):
#     res = 0
#     for i, j in kargs.items():
#         print(i , j)
# sum(num0=1, num1=2, num2=3, num3=4, num4=5)

# def sum(**kargs):
#     res=0
#     for i , j in kargs.items():
#         res += j
#         print(res)
# sum(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9)

# def form(**kargs):
#     print(type(kargs))
#     print(kargs)
# form(username=Manisha, password=1234 , dob=6-1-2003)

#Types of Functions
#1.Void Function - function without return statement 
#2.Function with Return Statements - function with return statements
#3.Lambda Functions - single line operations, optimization, anonymous

# lam_example = lambda x, y, z: x + y + z
# print(lam_example(1,2,3))

# #map(function, iterable)

# def sqr(x):
#     return x*x
# res=map(sqr, [1, 2, 3, 4])
# print(list(res))

# res=map(lambda x: x**3 , [1,2,3,4,5])
# print(list(res))

# res=map(lambda x: x**4 , [1,2,3,4,5])
# print(list(res))

#filter
def check_neg_num(x):
    # if x<0:
    #     return True
    # return False
    return x<0

print(list(filter(check_neg_num, [-2, -3, -1, 22, 13, 15])))

##17th feb
#DECORATORS
def example_decorator(func):
    def wrapper():
        print("Chech A4 sheets")
        print("Chech cartridge")
        func()
        print("Thankyou")

    return wrapper
@example_decorator
def printer():
    print("Printing in progress...")

printer()

