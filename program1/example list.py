#list
'''
student = ['jack' , 'rose' , 'yemi']
student1 = ['harry potter' , 'petter parker' , 'john wick' , 'harry potter']
print(student)
'''
print"------------------------------------")
'''
student = ['jack' , 'rose' , 'yemi']
student.append ('roja')
print(student)
'''
print"------------------------------------")
'''
student = ['jack' , 'rose' , 'yemi']
student1 = ['harry potter' , 'petter parker' , 'john wick' , 'harry potter']
student.extend (student1)
print (student)
'''
print"------------------------------------")
'''
student = ['jack' , 'rose' , 'yemi']
student.insert(4 , "jonathan")
print (student)
'''
print"------------------------------------")
'''
student = ['jack' , 'rose' , 'yemi' , 'jonathan']
student.remove("jonathan")
print(student)
'''
print"------------------------------------")
'''
student = ['jack' , 'rose' , 'yemi' , 'jonathan']
student.pop()
print(student)
'''
print"------------------------------------")
'''
student = ['jack' , 'rose' , 'yemi' , 'rose' , 'jonathan']

print ("which place have a rose after the 2 index :" , student.index("rose",1))

'''
print"------------------------------------")
'''
student = ['jack' , 'rose' , 'yemi' , 'rose' , 'yemi']
print ("how many number of yemi in the list :" , student.count("yemi"))

'''
print"------------------------------------")
'''
student = ['jack' , 'rose' , 'yemi' , 'rose']

student.sort()
print ("sorted : " , student)

'''
print"------------------------------------")
'''
student = ['jack' , 'rose' , 'yemi' , 'rose' , 'jonathan']

student.reverse()

print ("reverse list :" , student)

'''
print"------------------------------------")
'''
student = ['jack' , 'rose' , 'yemi' , 'rose' , 'jonathan']

student2 = student.copy()
student2.reverse()

print ("original list " , student2)
print ("copied list " , student2)

'''
print"------------------------------------")
'''
student = ['jack' , 'rose' , 'yemi' , 'rose' , 'jonathan']

student2 = student.copy()
student2.reverse()

print ("original list " , student)
print ("copied list " , student2)

'''
print"------------------------------------")
'''
student = ['jack' , 'rose' , 'yemi' , 'rose' , 'jonathan']

student2 = student.copy()
student2.reverse()

print(" clear function :" , student2)
for x in student :
    print(x)

'''
print"------------------------------------")
'''
student = ['jack' , 'rose' , 'yemi' , 'rose' , 'jonathan']

student2 = student.copy()
student2.reverse()

student2.clear()

print(" clear function :" , student2)
for x in student :
    print(x)
'''
print"-------------list end---------------")
print"------------------------------------")

#list stack
'''

liststack = [3,2,1]
print (liststack)

'''
print"------------------------------------")

'''

liststack = [3,2,1,]
liststack.append (5)
print(liststack)

'''
print"------------------------------------")
'''

liststack = [4,3,2,1]
liststack.pop()
print (liststack)

'''
print"-----------list stack end-----------")
print"------------------------------------")

#list queue

'''

from collections import deque
a = deque(["jack" , "rose" , "yemi"])
print(a)

'''
print"------------------------------------")

'''

from collections import deque
b = deque (["jack" , "rose" , "yemi"])

b.append ("jonathan")
print(b)

'''
print"------------------------------------")

'''

from collections import deque
c = deque (["jack" , "rose" , "yemi" , "jonathan"])

c.popleft()
print(c)

'''
print"------------------------------------")
'''

from collections import deque
c = deque (["jack" , "rose" , "yemi" , "jonathan"])

c.popleft()
print(c)

'''
print"----------list queue end------------")
print"------------------------------------")

#del

'''
a = [1,2,3,4,5,6,7,8,9,10]
print(a)

'''

print"------------------------------------")

'''
a = [1,2,3,4,5,6,7,8,9,10]
del a [0]
print (a)

'''
print"------------------------------------")

'''

a = [1,2,3,4,5,6,7,8,9,10]
del a [1:6]
print(a)

'''
print"------------------------------------")

'''

a = [1,2,3,4,5,6,7,8,9,10]
del a [:]
print(a)

'''
print"------------------------------------")
'''

a = [1,2,3,4,5,6,7,8,9,10]
del a
print (a)

'''

print"-------------del end----------------")
print"------------------------------------")
