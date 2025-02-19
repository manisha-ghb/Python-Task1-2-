#revise topics
#how to declare different types of datatypes
#conditional statements - if and else statements, elif
#loops - while, for, jump statements- break, continue
#functions - declaring a function and call a function, return statements usage
#inbuilt functions - atleast the most famous once - string and list

#variables
a = 85
b = 58
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print("Manisha")
str = "Mani_ @123"
print(len(str))
#indexing
print(str[0])
print(str[-1])
#slicing operation
print(str[0:5])
print(str[6:11])
#To print memory address of number or string
str1="Mani"
print(id(str1))
str2="Mani"
print(id(str2))
#DataTypes
#----Int-----
int1=4
print(type(int1))
print(int1)
#----Float----
float1=2.0
print(type(float1))
print(float1)
#---Complex---
c=3+4j
print(type(c))
print(c)
#---String---
d="Manisha"
print(type(d))
print(d)
#---list-----
list=[0,3,4,'String',True,[1,"Hello",3]]
print(id(list)) 
print(type(list))
print(len(list))
print(list)
#----tuple---
tuple=(1,2,3,4.5,[1,2,3],"String")
print(tuple)
print(id(tuple)) 
print(type(tuple))
print(len(tuple))
#--Boolean--
#Booleans - True or False
a=294
print(a==293)
print(a==294)
# ----Dictionary------
dict={1:'Satyanarayana',2:'Anitha',3:'Manisha',4:'Sindhu',5:'Manikanta',6:'Shiva',7:'Shankar'}
print(dict[2])
print(dict)
# ----Set----
set={2,4,5,2,2,2,2,4,6}
print(set)
#--None---
num=5
num=None
print(num)
print(type(num))
print(id(num))
#--Range--
x=range(10)
for n in x:
    print(n)
y = range(3, 6)
for n in y:
  print(n)
#OPERATORS
#---Arithmetic Operators
print("ARITHMETIC OPERATIONS")
print(8+5)
print(8-5)
print(8*5)
print(8/5)
print(8//5)
#---logical operators--
print("Logical Operators")
#and--Returns True if both statements are true
print(True and False)
print(False and True)
print(True and False)
print(False and False)
#or--Returns True if one of the statements is true
print(True or False)
print(False or True)
print(True or False)
print(False or False)
#not--Reverse the result, returns False if the result is true
print(not True)
print(not False)
#---Bitwise Operators---
print("Bitwise Operators")
# &(AND)
print(6 & 3)
print(8 & 4)
# |(OR)
print(6 | 3)
print(8 | 4)
# ^(XOR)
print(6^3)
print(8^4)
# ~(NOT)
print(~3)
print(~5)
# <<(Zero fill left shift)
print(3<<2)
print(6<<4)
# >>(Signed right shift)
print(8>>2)
print(7>>3)
#-------If Condition-----
print("-----If-----")
num1 = 0
if num1 == 0:
    print("Pushpa The Rise")
a = 33
b = 200
if b > a:
    print("b is greater than a")
#-----Else Condition------
print("-----Else-----")
num1 = 1
if num1 ==0:
    print("KGF-1")
else:
    print("KGF-2")
#else if - elif
print("-----elif-----")
num1 = 5
if num1 > 0:
    print("positive")
elif num1 == 0:
    print("zero")
elif num1 ==-1:
    print("-1")
else:
    print("Negative")
#-----whileloop----
num1=1
while num1<=100:
    print(num1)
    num1+=1
#-----forloop----
for num2 in range(100,0,-1):
    print(num2)
#---break--
for i in range(0,21):
    if i%2==0:
        print(i)
    if i==9:
        break
#---continue---
for i in range(1,10):
    print(i, "manisha")
    if i==2 or i==5:
        continue
    print(i)
#--reduce--
num1=15
if num1 % 7 == 0:
    pass
else:
    print("something to print")

from functools import reduce
#functions
def basic_function(a , b):   #parameters
     print("hiee")
     print("Good Morning , Hyd")
     print(a + b)
     print(a - b)
     print(a * b)
     print(a / b)
     print(a % b)
basic_function(3 , 6)  #Arguments-Positional arguments
basic_function(a=7 , b=6) #Keyword arguments
#---default parameters
def example_function(a , b , r , pie=3.14):
    print("circle area")
    print(pie * r * r)

example_function( a=2 , b=4 , r=10 , pie=3.14)
example_function(a=2 , b=2 , r=4)
# #example4----return statements
def example2_function(a , b , r=10 , pie=3.14):
    print(a)
    print(b)
    return a + b

res = example2_function(4, 5)
print(res+3)

def even_or_odd(num1):
    if num1 % 2 == 0:
      return "Even"
    else:
        return "odd"
print(even_or_odd(50))
#Arbitary Arguments
def sum(a, *b):
    print(a)
    print(b)
sum(1,2,3,4,5,6,7,8,9)
def sum(a, *b):
    res = a
    for k in b:
        res += k
    print(res)
sum(1,2,3,4,5,6,7,8,9)
#Keywords Arbitary Arguments
def sum(**kargs):
    print(type(kargs))
    print(kargs)
sum(num0=1, num1=2, num2=3, num3=4, num4=5)

def sum(**kargs):
    res = 0
    for i, j in kargs.items():
       print(i , j)
sum(num0=1, num1=2, num2=3, num3=4, num4=5)

lam_example = lambda x, y, z: x + y + z
print(lam_example(1,2,3))
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
