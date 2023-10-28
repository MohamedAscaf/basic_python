#strings are arrays

a = "hello , world!"
#print
print(a[3])

#lenth function

a = "hello , world!"
print(len(a))

#check function

txt = "hello , world!"
print("hello , world" in txt)


#slicing string

b = "hello , world"
print(b[2:5])

b = "hello , world"
print(b[:5])

b = "hello , world"
print(b[2:])

b = "hello , world"
print(b[-5:-2])

#modeify the string

a = "hello , world"
print(a.upper())

a = "hello , world"
print(a.lower())

a = "HELLO , WORLD"
print(a.lower())

#replace string

a = "hello , world"
print(a.replace("h" , "A"))

#sring concatenation

a = "hello"
b = "world"
c = a+b
print(c)

a = "hello"
b = "world"
c = a+ " " +b
print(c)
a = "hello"
b = "world"
c = a+ "   " +b
print(c)
