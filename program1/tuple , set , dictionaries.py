#tuple
'''
t = 12345 , 6789 , 'tuple'
print (t[1])
'''

#print all
'''

t = 1234 , 5678 , 'amazon'

print (t)
'''

#tuple are immutable
'''
t [1] = 1234
print (t)
'''

'''
t = 1234 , 5678 , 'flipkart'
a = t , (12,23,34,45)
print(a)

'''

#tuples empty and single

'''

t = 1234 , 5678 , 9012 , 'tuples'
empty = ()
s = 'welcome',
print (len(empty))
print (len(s))
print (s)

'''

'''
t = 1234 , 5678 , 'single'
t = 123 , 456 , 'single'
a,b,c = t

print (t)
print (a)
print (b)
print (c)

'''


#set
'''
software = {"python" , "java" , "linux" , "javascript"}
'''

'''
bucket = {"vallyball" , "basketball" , "football" , "cricketball"}

print (bucket)
print ('ballcricket' in bucket)
print ('cricketball' in bucket)

'''

'''
x = set ('karthickiyan')
print (x)
y = set ('karthikayen')
print (y)

'''

'''
x = set ('karthickiyan')
y = set ('karthikayen')

print ("unique letters in x" , x)
'''

'''
x = set ('ascaf')
y = set ('ascafullah')
print ("letters in x but not in y" , x-y)
'''
'''
x = set ('karthickiyan')
y = set ('karthikayen')
print ("both x or y" , x|y)

'''

'''
x = set ('ascaf')
y = set ('askaf')
print ("letter in both x and y" , x-y)

'''

'''
x = set ('karthickiyan')
y = set ('karthikayen')
print ("letter in x or y but not both" , x^y)
'''

#set checking

'''
a = {x for x in 'ascafullah' if x in 'abcd'}
print (a)

'''


#dictionaries

'''
a = {'name' : "karthickeiyan" , 'age' : 20}
print (a)

'''

'''
a = {'name' : "ascafullah" , 'age' : 26}
a ['guide'] = 123
print (a)

'''

'''
a = {'name' : "anbu" , 'age' : 30}
del a['age']
print (a)
'''

'''
a = {'name' : "guna" , 'age' : 30 }
print (list(a))
'''

'''
a = {'name' : "velu" , 'age' : 40}
print (sorted (a))

'''

'''
a = {'name' : "nalathambi" , 'age' :50}
print ("rajan" in a)
print ("age" in a)

'''

'''
a = dict ([('parthiban' , 26) , ('rakesh' , 27 ) , ('aravindh' , 25)])
print (a)
           
'''

'''
a = {x:x**2 for x in (2,3,4,5,6,7,8,9,10)}
print (a)

'''

a = dict (a=20 , b=21 , c=22 , d=23)
print (a)
