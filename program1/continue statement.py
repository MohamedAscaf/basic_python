# continue statement
'''
fruits = ["apple" , "banana" , "cherry" ]
for x in fruits:
    if x=="banana":
        continue
    print(x)
'''

'''
for x in range (20):
    if x<10:
        continue
    print (x)
'''

#for else
'''

for x in range (10):
    print(x)
else:
    print('loop eneded')

'''

#for using string
'''
txt = "hello world"
for x in txt:
    print (x, end = "\n")
'''

#collections in for loop
'''
collection = ['HAI' , 5 , 'd']
print (collection [0])
print (collection [1])
print (collection [2])
for x in collection:
    print(x, end = "\n")

'''

'''
collection = ['HAI' , 5 , 'd']
for x in collection:
    print(x)

'''

#nested loops
'''

for x in range (1):
    for y in range (5):
        print (x,y)


for x in range (3):
    for y in range (3):
        print(x,y)
    else:
        print ("y statement finish")


add = ["white" , "heavy" , "sweety"]
fruits = ["apple" , "staberry" , "orange"]
for x in add:
    for y in fruits:
        print(x,y)
'''

#list in for loop

lists = [[1,2,3] , [4,5,6] , [7,8,9] , [10]]
for g in lists:
    for x in g:
        print(x)
