 
# list
'''
program = ['python' , 'java' , 'idle']
program1 = ['dot' , 'html' , 'css' , 'cc+']
print (program)

'''

'''

program = ['python' , 'java' , 'idle']
program.append ("uiux")
print (program)

'''

'''
program = ['python' , 'java' , 'idle']
program1 = ['dot' , 'html' , 'css' , 'cc+']
program.extend(program1)
print (program)
'''

'''
program  = ['python' , 'java' , 'idle']
program.insert(2,"html")
print(program)

'''

'''
program = ['python' , 'java' , 'idle' , 'javascript']
program.remove("idle")
print (program)
'''

'''
program = ['python' , 'java' , 'uiux' , 'idle']
program.pop()
print (program)

'''

'''
program = ['python' , 'java' , 'idle' , 'java']
print (" which place have a apple after the 2 index :" , program.index("java" , 2))

'''

'''
program = ['python'  , 'java' , 'idle' , 'javascript']
print ("how many number of javascript in the list: " , program.count("javascript"))

'''

'''
program = ['python' , 'java' , 'idle' , 'javascript' , 'cc+' , 'android' , 'linux' , 'os']
program.sort()
print("sorted : " , program)
'''

'''
program = ['python' , 'java' , 'idle' ,  'liux' , 'javascript']
program.reverse()
print ("reverse list :" , program)
'''

'''
program = ['python' , 'java' , 'idle' , 'javascript' , 'uiux' , 'liux']
program2 = program.copy()
program2.reverse()
print ("orignal list" , program)
print ("copied list" , program2)

'''

'''
program = ['python' , 'java' , 'idle' , 'javascript' , 'uiux' , 'liux' , 'html']
program2 = program.copy()
program2.reverse()
program2.clear()
print ("clear function :" , program)
for x in program:
    print(x)

'''

#example full workout list
'''
program = ['python' , 'java' , 'idle' , 'javascript' , 'uiux' , 'liux' , 'html']
program.append ("fullstock")
print (program)
program1 = ['java fullstack' , 'python fullstack' , 'digital marketing']
program.extend(program1)
print(program)
program.insert (8, "computer")
print(program)
program.pop()
print(program)

'''

#list stack
'''
liststack = [10,9,8,7,6,5,4,3,2,1]
print (liststack)
'''

'''
liststack = [10,9,8,7,6,5,4,3,2,1]
liststack.append (11)
print (liststack)

'''

'''
liststack = [9,8,7,6,5,4,3,2,1]
liststack.pop()
print (liststack)

'''

#list Queue
'''

from collections import deque
x = deque (["python" , "java" , "liux"])
print (x)
'''

'''
from collections import deque
a = deque (["javascript" , "python" , "java"])
a.append ("linux")
print (a)

'''

'''
from collections import deque
b = deque (["python" , "java" , "uiux" , "javascript"])
b.popleft()
print(b)

'''

#list del
'''
a = [1,2,3,4,5,6,7,8,9,10]
print (a)
'''

'''
b = [1,2,3,4,5,6,7,8,9,10]
del b [5]
print (b)

'''

'''
c = [1,2,3,4,5,6,7,8,9,10]
del c [1:8]
print (c)
'''

'''
d = [1,2,3,4,5,6,7,8,9,10]
del d
print (d) # error

'''

e = [1,2,3,4,5,6,7,8,9,10]
del e [:]
print (e)
