#program:

'''
print ("Hai Bro")
print ("Hello" , "World" , "hai" , "bro" ,sep="_ _ _ ")
'''

'''
print("Hello" , end="\t")
print("Welcome")
'''

'''
print("Hello\nWorld")
'''

'''
print("Hello World" , end = "\t yes its ended")
'''

#list
'''
fruits=['orange' , 'apple' , 'pear' , 'banana' , 'kiwi' , 'apple' , 'banana']
print(fruits)
#tuples and sequences

t=12345,56789,'hello'
print(t)
#set

basket ={'apple','orange','banana'}
print(basket)
#dictionaries

tel={'jack':4098,'sape':4139}
print(tel)
'''
#binary language
'''
print(10>9)

print(10==5)

print(10<9)

a=5
print(a)
print("b")
'''
#false
'''
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
'''

#true
"""
print(bool("abc"))
print(bool(123))
print(bool([]))
"""

'''
x=1
y=2.8
z=1j
print(type(x))
print(type(y))
print(type(z))
'''

#integer
'''
x=1
y=12334454547658980
z=-2354577
print(type(x))
print(type(y))
print(type(z))

'''

#float
'''
x=1.10
y=1.0
z=-35.56
print(type(x))
print(type(y))
print(type(z))
'''

#float with e,E,to indicate the power of 10
'''
x=23e2
y=12E3
z=-56.7e100
print(type(x))
print(type(y))
print(type(z))

'''

#comple j as the imadinary part
'''
x=3+4j
y=5j
z=-5j
print(type(x))
print(type(y))
print(type(z))
'''

#type conversion
'''
x=1
y=2.8
z=1j

#convert from int to float:
a=float(x)
#convert from int to int:
b=int(x)
#convert from int to complete
c=complex(x)

print(type(a))
print(type(b))
print(type(c))
'''

#random no
'''
import random
print(random.randrange(1,10))
'''

#type casting
'''
x=str("si")
y=str(1)
z=str(3.0)
print(type(x))
print(type(y))
print(type(z))
'''

#input
'''
x=7
print(type(x))
print(x)

y=1.2
print(type(y))
print(x)

z=7j
print(type(z))
print(z)
'''

#string are arrays
'''
a="hello , world"
print(a[1])
'''

#length function
'''
a="hello,world"
print(len(a))
'''
#check function
'''
txt="the best things in life are free"
print("best" in txt)
'''
#slicing strings
'''
b="hello , world"
print(b[1:9])
'''

'''
b="hello,world"
print(b[2:])
'''

'''
b="hello,world"
print(b[:9])
'''

'''
b="hello,world"
print(b[-6:-4])

'''

#modify the string
'''
a="hello,world"
print(a.upper())
'''

'''
a="hello,world"
print(a.lower())

b="HELLO,WORLD"
print(a.lower())
'''

'''
a="       hello,world  !"
print(a.strip())
'''

#replace string
'''
a="hello,world"
print(a.replace("e","o"))
'''

#string concatenation
'''
a="hello"
b="world"
c=a+b
print(c)

a="hello"
b="world"
c= a+ "   " +b 
print(c)
'''

'''
a="hello"
b="world"
c = a+"     " +b
print(c)
'''

#Error File
"""
age = 35
txt = age + "my name is john , I am"
print(txt)
"""


'''
age = 36
txt = "my name is john , and i am {}"
print (txt.format(age))
'''

'''
quantity = 3
itemno = 567
price = 49.95
myorder = " i want {} pieces of item {} for {} dollars "
print (myorder)
print (myorder.format (quantity , itemno , price))
'''

'''
quantity = 2
itemno = 567
price = 49.94
myorder = "I want to pay {2} dollars for {0}\"pieces\"of item {1}."
print (myorder.format(quantity , itemno , price))
'''

'''
a = "hello , world"
print (a.split(" "))
'''

'''
a = "hello , world"
print(a.split("l"))
'''

#output

'''
print('python is powerful')
print('Good Morning! ' , end='')
print('It is rainy day')
'''

#input

'''
num = input ('Enter a Number:')
print('You Entered: ' , num)
print('Data type of num:' , type(num))
'''

#type casting
'''
num = int (input ('Enter a number:'))
print(type(num))
print
'''

#example:
'''
a = int (input("Enter the A value: "))
b = int (input("Enter the B value: "))
print(a+b)
'''

#Arithmetic operator

'''
x = 10
y = 5

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)
'''

#python assignment operators

'''
x = 5000
print (x)

x+=3
print(x)
x-=3
print(x)
x*=3
print(x)
x/=3
print(x)
x%=3
print(x)
x//=3
print(x)
x**=3
print(x)
'''

#python comparison operators

'''
a = 32
b = 7

print('a==b:' , a==b)
print('a>b:' , a>b)
print('a<b:' , a<b)
print('a!=b:' , a!=b)
print('a<=b:' , a<=b)
print('a>=b:' , a>=b)
'''

#logical operators
'''
a=5
print('is this statement true?:' , a>3 and a<5)

print('any one statement is true?: ' , a>30 or a<6)

print('Each statement is true then return false and vice_versa : ' , not (a>3 and a<5))
'''

#Identity operators

'''
a = ["rose" , "lotus"]
b = ["rose" , "lotus"]
c = a

print (a is c)
print (a is not c)
print (a is b)
print (a is not b)
print (a==b)
print (a!=b)
'''

#Membership operators

'''
x = ["Rose" , "Lotus"]
print('is value present?' , "Rose" in x)

print('is value not present?' , "riya" not in x)
'''

#simple if

'''
a = 89
b = 90
c = 69
if(a<b):
  print("a is greater than b")
  print("jack")
  print("a value is :" , a , "\n b value is :" , b)
'''

#if else

'''
a = 100
b = 90
c = 69
if(a>b):
    print("a is greater than b")
else:
    print("b is greater than a")
print(" a value is :" , a , "\n b value is :" , b)
'''

'''
name = input ('Enter A Name:')
age = int (input('Enter A Age:'))
if (age>18):
   print (name + " your eligble to vote")
else:
    print ("not eligble to vote")
'''

#if else ladder

'''
a = 100
b = 90
c = 150

if (b>a):
    print ("b is lower than a")
elif (c>a):
    print("c is greater than a")
else:
    print(" a value is :" ,a,"\n b value is :" ,b)
'''

#nested if

'''
a = 100
b = 90
c = 10

if (b>a):
    print("b is greater than a")
    if (b>c):
        print("b is greater than both")
    else:
        print("a is greater than b")
else:
    print("c is greater than b")
'''


'''
if (a>b and a>c):
      pass
'''



'''
Name = input ('enter a name :')
age = int (input('enter a age :'))
place = input ('enter your place :')
if (age>20):
    if (place=="titanic"):
        print ("eligible to ocean ship")
    else:
        print ("place not supported")
else:
    print("your age is eligible")
'''

#stribg formating
'''
name = "nithish"
age = 22

print("this is %s and my age is %d"%(name,age))
print("this is " , name)
print("this is " + name)
print("my age is " , age)
print("my age is " , + age)
print("this " , name , age)
'''

#simple for
'''
for x in range (30):
    print ("we're on the %d" %(x))
'''

#for and break
'''
for x in range (30):
    if (x==5):
        break
    print(x)
'''


'''
for x in range (30):
    print (x)
    if (x==8):
        break
'''


'''
for x in range (30):
    if (x==9):
        print (x)
        break
'''

#continue statement
'''
fruits = ["apple" , "banana , cherry ,gowa"]
for x in fruits:
    if x == "banana":
        continue
    print (x)
'''


'''
for x in range (30):
    if x>10:
        continue
    print(x)
'''

#for else

'''
for x in range (10):
    print(x)
else:
    print ('loop ended')
'''

#for using string

'''
txt = "hello world"
for x in txt:
    print(x)
'''

'''
txt = "Hellow World"
for x in txt:
    print(x, end = "")
'''

'''
txt = "hello  World"
for x in txt:
    print(x, end = "")
'''

'''
txt="Hello World"
for x in txt:
    print(x,end="\t")
'''


#collections in for loop
'''
collection = ['hey',5,'d']
print(collection[0])
print(collection[1])
print(collection[2])

for x in collection:
    print(x)
'''

'''
collection = ['Hey',5,'d']
for x in collection:
    print(x)
'''


#Nested loops
'''
for x in range(3):
 for y in range(3):
    print(x,y)
'''

'''
for x in range (3):
 for y in range(3):
     print(x,y)
else:
    print("y statement finish")
'''

'''
adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry","guowah"]
for x in adj:
    for y in fruits:
        print(x,y)
'''


#list in for loop
'''
a = [[1,2,3,],[4,5,6],[7,8,9],[10,11,12]]
for b in a:
    for x in b:
        print(x)
'''


#in crease value 3
'''
for x in range (2,30,5):
    print(x)
'''

'''
for x in range (7):
    pass
'''


#while loop
'''
i = 1
while i<5:
    print(i)
    i+=1
'''


#while using break
'''
i = 1
while i<6:
    if i==4:
        break
    print(i)
    i+=1
'''


#while else
'''
i=1
while i<6:
    print(i)
    i+=(1)
else:
    print("i is no longer less than 6")
'''


#example fibbonacil limit
'''
a=int(input("fibbonacil limit :"))
i=1
x=0
y=1
while (i<a):
    
    z=x+y
    print(z)
    x=y
    y=z
    i+=1
else:
    print("z statement finish")
'''

#reverse string
'''
a = ("mum")
b = a[::-1]
print(b)
if (a==b):
    print("palintron")
else:
    print("not palintron")
'''

'''
a = ("reverse")
b = a [::-1]
print(b)
if (a==b):
    print("palintron")
else:
    print("not palintron")
'''

'''
a = input ("enter the string :")
b = a[::-1]
print(b)
if (a==b):
    print("palintron")
else:
    print("not palintron")
'''

#double lists reverse for loop
'''
a = [[1,2,3],[4,5,6],[7,8,9]]
b = []
for g in a:
    g=g[::-1]
    b+=[g]
    print(b)
    c=b[::-1]
    print(c)
'''

#palintron in for loop
'''
a = ("MadaM")
for p in a:
    for x in p :
        print(x)
b = a[::-1]
print(b)
if (a==b):
    print("palintron")
else:
    print("not palintron")
'''

#for loop

'''
i=1
x=0
y=1

for i in range (10):
  z= x+y
  print(z)
  x=y
  y=z
  i+=1
'''

#input for loop
'''
a=int(input("Enter the value :"))
i = 1
x = 0
y = 1
for i in range (a):
    z=x+y
    print(z)
    x=y
    y=z
    i+=1
'''

#1
'''
n = 5;
for i in range (n):
    for j in range (i):
        print (' * ',end=" ")
    print('')
for i in range (n,0,-1):
    for j in range (i):
        print(' * ',end=" ")
    print('')
'''

#2
'''
numbers = (1,2,3,4,5,6,7,8,9,10)
count_odd = 0
count_even = 0
for x in numbers:
    if not x %9:
        count_even+=1
    else:
        count_odd+=1
print("number of even numbers :", count_even)
print("number of even numbers :",count_odd)
'''

#3

'''
result_str="";
for row in range (0,7):
    for column in range (0,7):
        if (((column == 1 or column ==5) and row !=0) or ((row ==0 or row==0 or row==3) and (column>1 and column<5))):
            result_str=result_str+"*"
        else:
            reslut_str=result_str+""
        result_str=result_str+""
        print(result_str);
'''

#4
'''
print ("Number pattern")
row = 5
for i in range (1,row + 1,1):
    for j in  range (1,i+1):
        print(j,end=" ")
    print("")
'''

#for exercise
#1
'''
def reverse_words (sentence):
    words = sentence.split(" ")
    new_word_list=[word[::-1]for word in words]
    res_str=" ".join(new_word_list)
    return res_str
str1="My Name Is Jessa"
print(reverse_words(str1))
'''

#2
number_list = [10,20,30,40,50,60,70,80,90,100]
i = 10
n = len(number_list)
while i<n:
    if number_list[i]>50:
       del number_list[i]
       n=n-1
else:
    i=i+1
print(number_list)
