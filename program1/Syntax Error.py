
#Syntax Error
'''
x = 10
if x==10
print (x)
'''
#Runtime Error
'''
#Name Error

print (x)

'''


#type Error

'''

x = "100"
y = 5
z = x+y

'''

#index Error

'''

x = ['kumar' , 'annanth' , 'sakthi']
print (x[6])

'''


#attribute Error

'''

x = "abinaiya"
x.reverse()

'''

#Logical Error
'''

def fact (n):
    r=1
    for x in range (1,n):
        r=r*x
    return r
print (fact(5))



'''
#correct ans not Error

def fact (n):
    r=1
    for x in range (1,n+1):
        r=r*x
    return r
print (fact(5))


'''

try:
    x=int(input("Enter a number:"))
    y=10/x
    print ("the result is:",y)
except valueError:
    print ("you must enter a valid integer")
except zerodivisionError:
    print ("you cannot divide by zero")

'''

#Assertion , Attribute , Floating poing , import , index , memory , name , overflow , typeError
