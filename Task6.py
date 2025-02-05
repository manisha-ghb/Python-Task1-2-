#   Day 1
list1 = [1,2,3,4,5,6]
new_list = []
for i in list1:
  if i%2==0:
    new_list.append(i)
print(new_list)



# Question 2

num_list = [1, 2, 3, 4, 5]
Even=0
Odd=0
for i in num_list:
    if(i%2==0):
        Even+=i
    else:
        Odd+=i
print("Even Sum", Even, 'Odd Sum', Odd)


# Question 3
input = ["abcd", "efghi", "ghifh", "dsfk", "sddfs"]
output=""
for i in input:
    output = output+ i[0]
print(output)



# Question 4 using loop
str = 'python'
rev=''
for i in range(0, len(str)):
    rev = str[i] + rev
print("Reverse String : ", rev)



# Question 4 using slicing
str='python'
print(str[::-1])



#  Day 2
# Question 1
num1=1
while num1<=100:
    print(num1)
    num1+=1


# Question 2 using while loop
num=100
while num>=1:
    print(num)
    num-=1



# Question 2 using for loop
for num2 in range(100,0,-1):
    print(num2)



# Question 3
org=1234
rev=0
while org>0:
    rev = (rev*10) + (org % 10 )  
    org = org//10
print("Reverse Number", rev)
