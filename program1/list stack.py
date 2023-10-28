#list stack
'''
liststack = [3,2,1]
print (liststack)


liststack = [3,2,1]
liststack.append(5)
print(liststack)


liststack = [4,3,2,1]
liststack.pop()
print(liststack)
'''

#list queue
'''
from collections import deque
queue=deque(["apple" , "orange" , "kiwi"])
print(queue)

from collections import deque
queue = deque(["apple" , "orange" , "kiwi"])
queue.append("banana")
print(queue)


from collections import deque
queue = deque(["apple" , "orange" , "kiwi"])
queue.popleft()
print(queue)
'''

#del
'''
a = [1,2,3,4,5,6,7,8,9]
print(a)
'''

'''
a = [1,2,3,4,5,6,7,8,9]
del a[0]
print(a)
'''

'''
a = [1,2,3,4,5,6,7,8,9]
del a[2:4]
print(a)
'''

'''
a = [1,2,3,4,5,6,7,8,9]
del a
print(a)
'''

a = [1,2,3,4,5,6,7,8,9]
del a[:]
print(a)
