#DataTypes
#int , float, string, complex, list, tuple, boolean, dictionary, set, none, range...
#----Int-----
int1=4
print(type(int1))
print(int1)
int2=6
print(type(int2))
print(int2)
print(int1+int2)
print(int1-int2)
print(int1*int2)
print(int1/int2)
print(int1**int2)

#----Float----
float1=2.0
print(type(float1))
print(float1)
float2=3.5
print(type(float2))
print(float2)
print(float1+float2)
print(float1-float2)
print(float1*float2)
print(float1/float2)
print(float1**float2)

#---Complex---
c=3+4j
print(type(c))
print(c)
c=5+3j
print(c)
a=5+8j
b=8+5j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

#---String---
d="Manisha"
print(type(d))
print(d)
print(type("Manisha"))
print("Manisha")

#---list---
#List- List is a ordered collection of data items and can be changeable (Mutable)
e=[20, 30, 40]
print(type(e))
print(e)
print(e[0])
print(e[1])
print(e[2])
e.append(60)
print(e)
e.remove(40)
print(e)
list=[0,3,4,'String',True,[1,"Hello",3]]
print(id(list)) 
print(type(list))
print(len(list))
print(list)
print(list[3])
print(list[5])
print(list[0:8:2])
print(list[-5])
print(list[5][1]) 
print(len(list[5])) 
list[4]="False" 
print(list)
list[5][1]="Bye"
print(list[5])
print(len(list[5][1]))

#----Tuple---
#Tuple - Tuple is ordered collection of data items but unchangeable (Immutable)
tuple=(1,2,3,4.5,[1,2,3],"String")
print(tuple)
print(id(tuple)) 
print(type(tuple))
print(len(tuple))
print(tuple[4])
print(tuple[-4])

#--Boolean--
#Booleans - True or False
a=294
print(a==293)
print(a==294)
print(94>93)
print(93>94)
print(93>=93)
print(int(False))
print(int(True))

# ----Dictionary------
#  Collection of items, which is used to store items in key value pair, we can access through keys only(Mutable data type)
dict={1:'Satyanarayana',2:'Anitha',3:'Manisha',4:'Sindhu',5:'Manikanta',6:'Shiva',7:'Shankar'}
print(dict[2])
print(dict)
dict[1]='BB2'
print(dict) 
dict['key-1']='value-1'
print(dict)
dict['key-1']='updated-value-1'
print(dict)

# ----Set----
#Set-Collection of elements(Unique, Unordered, Finite) and it is Immutable data type
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
z = range(3, 20, 2)
for n in z:
  print(n)


