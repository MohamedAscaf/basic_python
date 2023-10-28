'''An iterator is an object that contains a countable number of values.
'''

#iterator

""" mytuple=("computer","keyboard","mouse")
myiter=iter(mytuple)
print(next(myiter))
print(next(myiter))
print(next(myiter)) """



'''
mytuple = ("karthikeiyan" , "AnanthRaman" , "Ascaf" , "AbdulRahuman")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
'''



""" mytuple=("python" , "java" , "digital marketing")
myiter=iter(mytuple)
print(next(myiter))
print(next(myiter))
print(next(myiter)) """



""" mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit)) """

""" mystr = "python"
myiter = iter(mystr)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter)) """

""" mystr = ("AnanthaRamananRavanananRamaianam")
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
 """



#Generateor

""" def demo():
     n=1
     while n<10:
         val=n*n
         yield val
         n+=1

a=demo()
for i in a:
     print(i) """



""" def coma():
    x=1
    while x<20:
        val=x*x
        yield val
        x+= 1

a = coma()
for i in a:
    print(i) """



""" def demo():
   a=1
   while a<15:
       val=a*a
       yield val
       a+=1

x=demo()
for i in x:
    print(i) """



#closure
#Nested Function
#Store inner function to the outer function

""" def greet(name):
    # inner function
    def display_name():
        print("Hi", name)
    # call inner function
    display_name()
# call outer function
greet("Raja") """



""" def greater(name):
  def display_name():
      print("Hi Karthikeiyan" , name)
  display_name()
greater("EnAppanNallavan")
 """


""" def great(name):
    def display_name():
        print("hellow" , name)
    display_name()
great("karthikeiyan") """


#Decorator
 
""" def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)
print(result) """



""" def outer(a):
  def inner(b):
      return a+b
  return inner

add_one = outer(9)
result = add_one(8)
print(result)
 """


""" def outer(x):
 def inner(y):
    return x*y
 return inner

add_solution = outer(3)
result = add_solution(5)
print(result) """