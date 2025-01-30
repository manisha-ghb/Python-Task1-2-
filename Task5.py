#Control statements - Controls flow of execution of a code
#Control statements - Conditional statements, Loops and Jump statements


#Conditional Statements- if, else, elif

#-------If Condition-----
print("-----If-----")
num1 = 0
if num1 == 0:
    print("Pushpa The Rise")
num1 = 1
if num1 == 1:
    print("Bahubali")
num1 = 2
if num1 == 2:
    print("Game Changer")
a = 33
b = 200
if b > a:
    print("b is greater than a")



#-----Else Condition------
print("-----Else-----")
#--------------
num1 = 1
if num1 ==0:
    print("KGF-1")
else:
    print("KGF-2")
#--------------
num1 = 6
if num1 > 0:
    print("Positive")
else:
    if num1 == 0:
        print("Zero")
    else:
        print("Negative")
#---------------
num1 = 0
if num1 > 0:
    print("Positive")
else:
    if num1 == 0:
        print("Zero")
    else:
        print("Negative")
#--------------
num1 = 1
if num1 > 0:
    if num1 == 1:
        print("one")
    else:
        print("positive")
else:
    if num1 == 0:
        print("Zero")
    else:
        print("Negative")
#---------------
num1 = 0
if num1 > 0:
    if num1 == 1:
        print("one")
else:
    if num1 == 0:
        print("Zero")
    else:
        print("Negative")
#---------------
num1 = -1
if num1 > 0:
    if num1 == 1:
        print("one")
    else:
        print("positive")
else:
    if num1 == 0:
        print("Zero")
    else:
        if num1 == -1:
            print("-1")
        else:
            print("Negative")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")



#else if - elif
print("-----elif-----")
#---------------
num1 = 5
if num1 > 0:
    print("positive")
elif num1 == 0:
    print("zero")
elif num1 ==-1:
    print("-1")
else:
    print("Negative")

#--------------
num1 = 0
if num1 > 0:
    print("positive")
elif num1 == 0:
    print("zero")
elif num1 ==-1:
    print("-1")
else:
    print("Negative")

#-------------------
num1 = -1
if num1 > 0:
    print("positive")
elif num1 == 0:
    print("zero")
elif num1 ==-1:
    print("-1")
else:
    print("Negative")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
