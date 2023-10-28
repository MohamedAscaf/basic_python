
fruits = ['orange', 'apple', 'pear','apple']

fruits2=fruits.copy()
fruits2.reverse()
print("Original list",fruits)
print("copied list",fruits2)


fruits2.clear()
print("clear function : ",fruits2)

for x in fruits:
    print(x)
