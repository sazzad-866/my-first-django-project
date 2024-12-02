"""
print('"Hellow, world"')
print("'Hellow, world'")
#1#Print Something
a= input("Please deliver yur welcome speech= ")
print(a)

#2# Write a programme to ADD two numbers
a= int(input("Give the First Number= "))
b= int(input("Give the Second Number= "))
sum= a+b
print(f"The summation of the two numbers are ={sum}")

#3#Calculate Square Root of a number
import math
my_num= int(input("Enter the number ="))
root_my_num= math.sqrt(my_num)
print(f"The root of my number is = {root_my_num}")

##
def sqrt(n):
     if n<0:
         print("Its Root is not Real")
     else:
         return n**0.5

my_num= int(input("Give the Number"))
root_num= sqrt(my_num)
print(f"The root of the number is= {root_num}")

#4# Calculate Area of a Triangular
def triangle_type(a,b,c):
    s= (a+b+c)/2
    if a**2 == b**2 + c**2:
        return 0.5*b*c
    else:
        return s*(s-a)*(s-b)*(s-c)

a= int(input("Give the largest side of the Triangle="))
b= int(input("Give the second side of the Triangle="))
c= int(input("Give the third side of the Triangle="))
result= triangle_type(a,b,c)
print(f"The Area of your triangle is = {result}")

#5# Check Even/Odd
def check(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

my_num = int(input("Give the Number ="))
result = check(my_num)
print(f"The number is {result} number ")

#6# Check Prime number
def check(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

my_num = int(input("Give the Number ="))
if check(my_num):
    print("Prime number ")
else:
    print("Not Prime number ")


#7#Fibonacchi
def fibo(n):
    a=0
    b=1
    for _ in range(n):
        print(a, end=" ")
        next= a+b
        a=b
        b=next

fn=int(input("Enter the number of fibonacci series you want ="))
if fn<0:
    print("Please enter a valid number")
else:
    print("The fibonacci series is=")
    fibo(fn)

#8#Factorial of a number

def fac(n):
    result=1
    for i in range(1, n+1):
        result *=i

    return result

fn=int(input("Enter the number of factorial you want ="))
if fn<0:
    print("Please enter a valid number")
if fn==0:
    print("1")
else:
    print(f"The factorial is= {fac(fn)}")

#9#Swap

def swap(x,y):
    p,q=y,x
    return p,q

x=int(input("Enter the First number x ="))
y=int(input("Enter the Second number y ="))
p,q=swap(x,y)
print(f"After Swaping x ={p} and y={q}")

#10# Palindrome char

def pal(x):
    x =x.replace(" ","").lower()
    return x== x[::-1]

x=input("Enter the string x =")
if pal(x):
    print(f"{x} is a Palindrome")
else:
    print(f"{x} is Not a Palindrome")

### Palindrome num

def pal(x):
    x =str(x)
    return x== x[::-1]

x=input("Enter the number x =")
if pal(x):
    print(f"{x} is a Palindrome")
else:
    print(f"{x} is Not a Palindrome")

#11#Find largest

def find_largest(a,b,c):
    if a>=b:
        if a>=c:
            return a
        else:
            return c
    else:
        if b>=c:
            return b
        else:
            return c

a=input("Enter the first number=")
b=input("Enter the secind number=")
c=input("Enter the third number=")
result= find_largest(a,b,c)
print(f"The Largest number is= {result}")

#12#GCD

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

x=int(input("Enter the Largest number a ="))
y=int(input("Enter the Second number b ="))
result=gcd(x,y)
print(f"The Gcd of these two numbers is={result}")

#13#LCM

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def lcm(a,b):
    return abs(a*b)//gcd(a,b)

x=int(input("Enter the Largest number a ="))
y=int(input("Enter the Second number b ="))
result=lcm(x,y)
print(f"The LCM of these two numbers is={result}")

#14#Celsius to Fahrenheit

def far(a):
    return (a* (9/5))+32

x=float(input("Enter the Temperature in Celcius ="))
result=far(x)
print(f"The Temperature in Fahrenheit is={result}°F")

#15#Generate a random number

import random
def ran(a,b):
    return random.randint(a,b)

x=int(input("Enter the Lower bound ="))
y=int(input("Enter the Upper bound ="))
result=ran(x,y)
print(f"The Random value between {x} and {y} is={result}")

###Import random float

import random
def ran(a,b):
    return random.uniform(a,b)

x=float(input("Enter the Lower bound ="))
y=float(input("Enter the Upper bound ="))
result=ran(x,y)
print(f"The Random value between {x} and {y} is={result}")

#16#Find sum of N numbers or start to end numbers

def sumn(a,b):
    sum=0
    for i in range(a,b+1):
        sum+=i
    return sum

x=int(input("Enter the strating point ="))
y=int(input("Enter the end point ="))

if x>0 and x<=y:
    result = sumn(x, y)
    print(f"The Sum of the values between {x} and {y} is= {result}")

else:
    print("Invalid Number")

#17#Count the number of vowel in string
def vow(a):
    vowels="aeiouAEIOU"
    count=0
    for char in a:
        if char in vowels:
            count+=1
    return count

x=input("Enter the string =")
s=vow(x)
print(f"There are {s} vowels in your string")


#18#Remove Punctuation from string
import string
def pun(a):
    s=a.maketrans("","",string.punctuation)
    return a.translate(s)

x=input("Enter the string =")
s=pun(x)
print(f"Here your string after removing punctuation: {s}")


#19#Find the Ascii value of a character
x=input("Enter the character =")
s=ord(x)
print(f"The ascii value of your character is : {s}")

#20#Reverse a number
num=int(input("Give the number= "))
revnum=0
while num!=0:
    digit=num%10
    revnum= revnum*10 + digit
    num=num//10

print(f"the reverse form of your number is= {revnum}")

#21# To find the second largest number in a list
def largest(a):
    uniquenumber= list(set(a))
    if len(uniquenumber) <2:
        return "There is no largest number"
    uniquenumber.sort(reverse=True)
    return uniquenumber[1]

x=list(map(int,input("Enter numbers separated by space= ").split()))
s=largest(x)
print("Here your string after removing punctuation: ", s)

#22# To sort a list in ascending or descending order
number_list= list(map(int, input("Give the number list separeted by space: ").split()))
number_list.sort()
print(f"The list in ascending order is: {number_list}")

##Descending order
number_list= list(map(int, input("Give the number list separeted by space: ").split()))
number_list.sort(reverse=True)
print(f"The list in ascending order is: {number_list}")


#23# To Merge two list
list1= list(map(int, input("Give the first list: ").split()))
list2= list(map(int, input("Give the second list: ").split()))
merge_list= list1+list2
print(f"The merge list is: {merge_list}")


#24# To find the sum of all elements of a list
list= list(map(int, input("Give the list: ").split()))
total_sum= sum(list)
print(f"The sum of all elements of the list is: {total_sum}")

#25# To find common elements between two list
list1= list(map(int, input("Give the first list: ").split()))
list2= list(map(int, input("Give the second list: ").split()))
common_elements= list(set(list1)& set(list2))
print(f"The common elements of {list1} and {list2} is : {common_elements}")


#26# Write a program to count the occurence of each element in a list
a= list(map(int,input("Give the list: ").split()))
element_cnt= {}

for element in a:
    if element in element_cnt:
        element_cnt[element]+=1
    else:
        element_cnt[element]=1

for element,count in element_cnt.items():
    print(f"The element {element} occurce {count} times")

#27#Write a program to remove duplicates from list
def remove_duplicates(a):
    return list(set(a))

x=list(map(int,input("Enter numbers separated by space= ").split()))
s=remove_duplicates(x)
print("Here your string after removing duplicates: ", s)

#
def remove_duplicates(a):
    unique_list=[]
    for element in a:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

x=list(map(int,input("Enter numbers separated by space= ").split()))
s=remove_duplicates(x)
print("Here your string after removing duplicates: ", s)

#28#Write a program to flattern a nested list:
def flattened_nested_list(a):
    flattened_list=[]
    for element in a:
        if isinstance(element,list):
            flattened_list.extend(flattened_nested_list(element))
        else:
            flattened_list.append(element)
    return flattened_list

nested_list=[7,[2,3],4,[2,[3,4],5],6,[7,8]]
result= flattened_nested_list(nested_list)
print("Flattended list: ",result)
#29#Write a programme to check if the list is empty:
def check_list(my_list):
    if not my_list:
        return "This list is Empty"
    else:
        return "This list is Not Empty"
list1=[]
print(check_list(list1))
list2=[1,2,3,4,5]
print(check_list(list2))

#30#Write a programme to find the intersection of two sets
def find_intersection(set1,set2):
    return set1.intersection(set2)
set1_input= input("Give the first set: ")
set2_input= input("Give the secind set: ")

set1= set(map(int,set1_input.split()))
set2= set(map(int,set2_input.split()))
result=find_intersection(set1,set2)
print("The intersect set is: " ,result)

#31#Write a programme to check if a key is exist in a dictionary:
my_dict= {'name':'john', 'age':25, 'city':'new york', 'weight':60}
key_to_check= input("Give the key you want to check: ")
if key_to_check in my_dict:
    print(f"The key '{key_to_check}' is in the dictionary")
else:
    print(f"The key '{key_to_check}' is Not in the dictionary")

#32#Write a programme to merge two dictionaries:
dict1={'a':1, 'b':2, 'c':3}
dict2={'d':4, 'e':5, 'f':6}

dict1.update(dict2)
print("The Marged Dictionary is : ",dict1)

#33#Write a programme to remove a key from a dictionary:
my_dict= {'name':'john', 'age':25, 'city':'new york', 'weight':60}
key_to_remove= input("Give the key you want to remove: ")
if key_to_remove in my_dict:
    remove= my_dict.pop(key_to_remove)
    print(f"The key '{key_to_remove}' is removed with value {remove} in the dictionary")
else:
    print(f"The key doesn't exist in the dictionary")

#34#Write a programme to sort a dictionary by its value:
my_dict={
    'apple':3,
    'banana':1,
    'cherry':2,
    'date':5,
    'elderbarry':4
}
sorted_dictionary= dict(sorted(my_dict.items(), key= lambda item : item[1]))
print("Sorted by Values: ", sorted_dictionary)
sorted_dictionary2= dict(sorted(my_dict.items(), key= lambda item : item[1],reverse=True))
print("Sorted by Values in Reverse: ", sorted_dictionary2)

#35#Write a programme to count the frequency of characters in a string:
def check_freq(a):
    frequency={}
    for char in a:
        if char!= ' ':
            if char in frequency:
                frequency[char] +=1
            else:
                frequency[char] = 1
    return frequency

input_string= input("Give the string: ")
s=check_freq(input_string)
print("Character frequency: ", s)

#36# Write Python code count the most fre of char
def count_fre(l):
    if not l:
        return None
    frequency={}
    for item in l:
        if item in frequency:
            frequency[item]+=1
        else:
            frequency[item]= 1
    most_fre= max(frequency, key=frequency.get)
    return most_fre

my_list=list(map(int,input("Give the elements: ").split()))
result= count_fre(my_list)
print("The most occur: ",result)

#37#Create a lambda fun to add two numbers
add_num= lambda x,y: x+y
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
result= add_num(num1,num2)
print("The summation is : ",result)

#38# Map two lists into a dictionary:
keys=['name', 'age','city']
values=['sajid',21, 'chittagong']
my_dict= dict(map(lambda x,y : (x,y), keys, values))
print(my_dict)


#39# Write a programme To implement a Stack using a list:
class Stack:
    def __init__(self):
        self.stack=[]
    def is_empty(self):
        return len(self.stack)==0
    def push(self,item):
        self.stack.append(item)
        print(f"{item} Pushed to stack")
    def pop(self):
        if self.is_empty():
            return "The stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "The stack is empty"
        return self.stack[-1]
    def size(self):
        return len(self.stack)

stack1=Stack()
stack2=Stack()
stack1.push(10)
stack1.push(20)
stack1.push(15)
stack2.push(30)

print("Top element of stack2 is: ",stack2.peek())
print("Top element is: ",stack1.peek())
print("Stack size is:",stack1.size())
print("Popped element:",stack1.pop())
print("Stack is empty:",stack1.is_empty())

#40# Write a programme to implement a Queue using list:
class Queue:
    def __init__(self):
        self.queue=[]

    def is_empty(self):
        return len(self.queue)==0

    def enqueue(self,item):
        self.queue.append(item)
        print(f"{item} is added to the queue")

    def dequeue(self):
        if self.is_empty():
            return "The queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "The queue is empty"
        return self.queue[0]

    def size(self):
        return len(self.queue)


queue= Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(15)

print("Front element is: ",queue.peek())
print("Queue size is: ",queue.size())
print("Dequeue element: ",queue.dequeue())
print("Queue is empty: ",queue.is_empty())


def check(a):
    s=a.maketrans("","",string.punctuation)
    return a.translate(s)

a= int(input("Give the num:"))
revnum=0
while a!=0:
    digit=a%10
    revnum=revnum*10 +digit
    a=a//10
print("Result: ",revnum)
"""