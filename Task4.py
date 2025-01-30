#OPERATORS
#Logical-Operator, #Bitwise-Operator

#---Logical-Operator---(and, or, not)

#-------AND-------
#and--Returns True if both statements are true
x = 5
print(x > 3 and x < 10)# returns True because 5 is greater than 3 AND 5 is less than 
y=20
print(y<16 and y<25)#returns false
a = 10
b = 10
c = -10
if a > 0 and b > 0:
    print("The numbers are greater than 0")
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
       print("Atleast one number is not greater than 0")

#----------OR----------
#or--Returns True if one of the statements is true
x = 5
print(x > 3 or x < 4)# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
print(x > 6 or x < 3)#returns false
a = 10
b = -10
c = 0
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

#---------NOT------
#not--Reverse the result, returns False if the result is true
x = 5
print(not(x > 3 and x < 10))# returns False because not is used to reverse the result
print(not(x > 6 and x < 10))#returns true
a = 10

if not a:
    print("Boolean value of a is True")
if not (a % 3 == 0 or a % 5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")


#Bitwise-Operators
#(&-and, |-or, ^-xor, ~-not, <<-zero fill left shift, >>-signed right shift)

#------&----------
# &(AND)-Sets each bit to 1 if both bits are 1
print(6 & 3)
print(8 & 4)
a = 10
b = 4
print("a & b =", a & b)

#------|---------
# |(OR)-Sets each bit to 1 if one of two bits is 1
print(6 | 3)
print(8 | 4)
a = 10
b = 4
print("a | b =", a | b)

#------^---------
# ^(XOR)-Sets each bit to 1 if only one of two bits is 1
print(6^3)
print(8^4)
a = 10
b = 4
print("a ^ b =", a ^ b)

#------~--------
# ~(NOT)-Inverts all the bits
print(~3)
print(~5)
a = 10
b = 4
print("~a =", ~a)

#------<<-----
# <<(Zero fill left shift)-Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(3<<2)
print(6<<4)
a = 5
b = -10
print("a << 1 =", a << 1)
print("b << 1 =", b << 1)

#------>>------
# >>(Signed right shift)-Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print(8>>2)
print(7>>3)
a = 10
b = -10
print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)