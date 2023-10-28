#set in python
'''
freezer = {"apple" , "orange" , "banana" , "pinapple" , "papaiya" , "staberry"}

print(freezer)
'''

'''
print ('papaiya' in freezer)
print ('staberry' in freezer)
print ('mango' in freezer)
print ('kiwi' in freezer)
'''

'''
x = set ('karthiceiyan')
print (x)
y = set ('karthikaiyan')
print (y)
'''


x = set ('karthiceiyan')
y = set ('karthikaiyan')


'''
print ("unique letter in x" , x)
print ("unique letter in y" , y)
'''

'''
print ("letters in x but in y" , x-y)
'''

'''
print ("both x or y" , x|y)
'''

'''
print ("letters in  both x and y" , x&y)
'''

'''
print ("letters in x or y but not both" ,x^y)
'''

#set Checking

a = {x for x in 'karthickeiyan' if x in 'abcdef'}
print (a)
