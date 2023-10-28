#leap year not leap year
"""
year = int(input("enter the year"))
if ((year % 4==0) and ( year % 100 != 0) or (year % 400==0)):
    print ("leap year")
else:
    print ("not leap year")
"""

#basic funtion
'''
def function ():
    print ("welcome to python")
    print ("the python is best coding software")
    print ("the function is define the coding")

function()
function()
function()

'''

#funtion passing parameters
'''
def my_function (passing):
    print (passing + " to parameters")

my_function ("difine")
my_function ("passing")
my_function ("linus")
'''
#example:
'''
def python_coding():
    a = 10
    b = 10
    print (a+b)
    
python_coding()

'''

'''
def addition (a,b):
    print (a+b)
    
def subtraction (a,b):
    print (a-b)
    
def multiplication (a,b):
    print(a*b) 

def division(a,b):
    print (a%b)

addition (12,45)
subtraction (23,56)
multiplication (45,67)
division (67,89)

'''

"""
def addition (a,b):
    print (a+b)
    
def subtraction (a,b):
    print (a-b)
    
def multiplication (a,b):
    print(a*b) 

def division(a,b):
    print (a/b)
ch=1
while(ch==1):
    a = int(input(' enter a First value : '))
    b = int(input(' enter a Second Value : '))
    print("Choices : \n 1.add \n 2.subtration \n 3.multiplication \n 4.division ")
    x=int(input("Enter Your Choice  : "))
    if(x==1):
        addition(a,b)
    elif (x==2):
        subtraction (a,b)
    elif (x==3):
        multiplication (a,b)
    elif (x==4):
        division (a,b)
    else:
        print("You enter wrong One ")
    ch=int(input("if you want continue please enter 1 : "))

"""

'''
def function (y,z):
    print ("the function passing parameter")
ch=5
while(ch==5):
    a = int(input(' enter a first value : '))
    b = int(input(' enter a second value : '))
    print("choose : \n 1.add ")
    x=int(input("enter your choose :"))
    if(x==1):
     print ("you enter : 1")
    elif (x==2):
        function (y,z)
    else:
        print (" you enter right value ")
    ch=int(input("if you want continue please enter 1 : "))
'''

ch=1
while(ch==1 or ch==2):
    x = int(input(' enter your choose : '))
    if (x==1):
      print ("you enter : 1")
    elif (x==2):
      print ("you enter : 2")
    elif (x==3):
      print ("you enter : 3")
    else:
        print ("worng")
    ch=int(input("you enter right"))
    
