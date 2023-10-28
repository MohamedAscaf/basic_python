
# continue statement
'''
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x== "banana":
        continue
    print(x)
    
for x in range (50):
    if x >10:
        continue
    print(x)

'''

#for else:
'''
for x in range (50):
    print (x)
else:
    print('loop ended')

'''

# for using string
'''
txt = "hello world"
for x in txt:
    print(x)

txt = "hello world"
for x in txt:
    print(x, end= " ")

txt = "hello world"
for x in txt:
    print(x, end="\t")
    
'''
    
#collection inn for loop
'''
collection = ['hai' ,5, 'd']
print (collection[0])
print (collection[1])
print (collection[2])
for x in collection:
    print (x)


collection =['hai' , 5 , 'd']
for x in collection:
    print(x)
    
'''

#nested loops

'''
for x in range (5):
    for y in range (5):
        print(x,y)
        

for x in range (5):
    for y in range (5):
        print (x,y)
    else:
        print ("y statement finish")


add = ["red" , "big" , "tasty"]
fruits = ["apple" , "banana" , "cherry"]
for x in add:
    for y in fruits:
        print (x,y)

'''

# list in for loop
'''
lists = [[1,2,3] , [4,5,6] , [7,8,9] , [10,11,12] , [13,14,15]]
for g in lists:
         for x in g:
             print (x)
'''

#increase value 3
'''
for x in range ( 1 , 20 , 4):
    print (x)


for x in range (6):
    pass

'''

#while loop
'''

i = 1
while i<10:
    print(i)
    i +=1

'''

#while using break
'''

i =1
while i<8:
    if i==10:
        break
    print(i)
    i+=1
'''

#while else
'''

i = 1
while i<10:
    print(i)
    i+=(1)
else:
    print (" i is no longer less than 10")
'''

#fibonacci    
'''
i=1
x=0
y=1
while (i<10):
    z=x+y
    print(z)
    x=y
    y=z
    i+=1

a=int(input("fibbonacii limit : "))
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
    print ( "z statement finish")

'''
#reverse string

'''

a=input("enter the string : ")
b=a[::-1]
print (b)
if(a==b):
    print("palintron")
else:
    print("not palintron")
'''

#double lists reverse for loop
'''
a=[[1,2,3,] , [4,5,6,] , [7,8,9]]
b=[]
for g in a:
    g=g[::-1]
    b+=[g]
    print(b)

c=b[::-1]
print(c)

'''
#palintron in for loop
'''
a= ("madam")
for g in a:
    for x in g:
        print(x)
b=a[::-1]
print(b)
if(a==b):
    print("palintron")
else:
    print("not palintron")
'''

#for loop
a=int(input("Enter the value"))
i=1
x=0
y=1
for i in range(a):
    z=x+y
    print(z)
    x=y
    y=z
    i+=1
