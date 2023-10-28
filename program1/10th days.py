'''
def jack (fname , lname):
    print (fname+ " " +lname)
a = input("Enter the a:")
b = input("Enter the b:")
jack (a,b)

'''
'''
def my_function (child3 , child2 , child1):
    print ("the youngest child is " + child2)
my_function ("jack" , "rose" , "edvin")
my_function (child1 = "titanic" , child2 = "sea" , child3 = "dead")
my_function (child3 = "rose" , child2 = "david" , child1 = "jessi")

'''
'''
def my_function (**kid):
    print ("his last name is " + kid ["lname"])
my_function (fname = "jack" , lname = "rose")

'''

'''
def my_function (**kid):
    print ("his last name is " + kid ["fname"])
my_function (fname = "jack" , lname = "rose")

'''
'''
def my_function (*kids):
    print ("the youngest child is " + kids [2])
my_function ("email" , "gmail" , "yahoo")

'''
'''
def my_function (country = "england"):
    print ("i am from " + country)
my_function ("india")
my_function ("dubai")
my_function ()
my_function ("france")

'''
'''
def my_function (food):
    for y in food:
        print ("\t",y,"\n" )
fruits = ["apple" , "banana" , "cherry"]
fru = ["apple" , "orange" , "kiwi" , "mango"]

my_function (fruits)
my_function (fru)
'''
'''
def country1(c="india"):
    return c
country=country1()
print(country)

'''

#user form

firstname = (input("Enter the first name :"))
lastname = (input("Enter the last name :"))
dateofbirth = input("Enter the Date of Birth :")
Age = int(input("Enter the Age :"))
Place = (input("Enter the Place :"))
def function (fname , lname):
    print (fname + " " + lname)
print("Name :", end=" " )
function (firstname , lastname)
print("date of birth :",dateofbirth)
print("Age :",Age)
print("vote", end=" ")
if (Age >18 and Place =="hogwarts"):
    print ("your eligble to vote")
else:
    print("not eligble to vote")
print("Place :",Place)
print("country :",end=" ")


def my_country (c="britain north of london"):
    return c
country=my_country()
print(country)
