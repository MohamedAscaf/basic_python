#error file

'''
age = 26

txt = age + "my name is john  , i am"
print (txt)
'''

"""
age = 36

txt = "myname is john , and i am {}"
print(txt.format (age))
"""

'''
quantity = 1
itemno = 786 
price = 12.21
myorder = "i want {} pieces of item {} for {} dollars."

print(myorder)

print(myorder.format(quantity,itemno,price))
'''

"""
quantity = 1
itemno = 123
price = 12.21
myorder = "I want to pay {2} dollars for {0} \"pieces\"of item {1}."
print(myorder.format(quantity , itemno , price))

"""

'''
a = "hello python"
print(a.split(" "))
'''
"""
a = "hello , python"
print(a.split("o"))
"""

#output
'''
print ('python is coding')
print ('good afternon' , end=' ')
print (' it is coding day')
'''

#input
"""
num = input ('enter num:')
print('you entered:' , num)
print('data type of num:' , type(num))
"""

'''
num= int(input('enter anumber: '))
print(type(num))

'''

#input
"""
num = int (input ('enter a number: '))
print (type(num))

"""

#example

'''
a = int (input("enter type A value: "))
b = int (input("enter type B value: "))
print(a+b)

'''

#Arithmetic oprater
"""
x = 5
y = 2

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)
"""

#python assignment operators

'''
x = 1000
print (x)
x+=1
print (x)
x-=1
print (x)
x*=1
print(x)
x/=1
print (x)
x%=1
print (x)
x//=1
print (x)
x**=1
print (x)

'''

#python comoarison operators
"""
a = 26
b = 7

print ('a==b:' , a==b)
print ('a>b:' , a>b)
print ('a<b:' , a<b)
print ('a!=b:' , a!=b)
print ('a<=b:' , a<=b)
print ('a>=b:' , a>=b)

"""

#logical opertator
""""
a = 5

print (' is this statement true?: ' , a>1 and a<7)



print ('any one statement is true?:' , a>30 or a<6)

print (' each statement is true then return false and vice-versa:' , not (a>5 and a<7))

"""

#identity operatyors

'''
a = [ "jack" , "rose" ]
b = [ "jack" , "rose" ]
c = a

print (a is c)
print (a is not c)
print (a is b)
print (a is not b)
print (a==b)
print (a!=b)

'''

#membership operators

x = [ "jack" , "rose" ]
print ( ' is value present ?' , "jack" in x )
print (' is value not  present ?' , "peter parker" not in x )

