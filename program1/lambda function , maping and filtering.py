# lambda funtion
'''

x = lambda y : y + 5
print (x(3))
x = lambda y , z : y*z
print (x (1,2))

def my_function (n):
    return lambda y : y*n
my_doubler = my_function (1)
print (my_doubler (22))
print (my_doubler (8))
print (my_doubler (6))
print (my_doubler (3))

'''
#maping and filtering

data = [1,2,3,4,5]
result1 = map(lambda x : x*5 , data)
print (list(result1))

result2 = filter (lambda x: x%1 == 0 , data)
print (list(result2))
