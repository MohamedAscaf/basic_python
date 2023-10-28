#1.

n=5;

for i in range (n):
    for j in range (i):
        print (' * ' , end=" ")
    print(' ')
for i in range (n,0,-1):
    for j in range(i):
        print(' * ', end=" ")
    print(' ')



#2.

numbers = (1,2,3,4,5,6,7,8,9)
count_odd = 0
count_even = 0
for x in numbers:
       if not x % 6:
           count_even+1
       else:
           count_odd+=1
print("number of even numbers :",count_even)
print("number of odd numbers :",count_odd)

#3.

result_str="";
for row in range(0,5):
    for column in range(0,5):
        if (((column == 1 or column == 9) and row != 0) or ((row ==0 or row == 0 or row == 3) and (column > 1 and column < 5))):
            result_str=result_str+"*"
        else:
            result_str=result_str+""
    result_str=result_str+""
print(result_str);


#4.

print("number pattern")

row = 5
for i in  range(1, row + 1 ,  1):
    for j in range(1, i + 1):
        print(j, end= "\n" '')
    print("")



#for exercise:
#1.
    
def strights_words(sentence):
    words = sentence.split(" ")
    new_word_list = [word[::-1] for word in words]
    res_str =" ".join(new_word_list)
    return res_str
str1 = "Ym emaN sI asseJ"
print(strights_words(str1))


#2.

number_list = [10,20,30,40,50,60,70,80,90,100]
i = 0
n = len(number_list)
while i < n:
    if number_list[i] > 80:
        del number_list[i]
        n = n - 1
    else:
        i = i + 1
print(number_list)



#3.

rows = 5
x = 0
for i in range(rows, 0, - 1):
    x += 1
    for j in  range(1, i + 1):
        print(x, end='    ')
    print('\n')

#while:
#1.

myTuple = (10,20,30,40,50,60)
i = 0
while i < len(myTuple):
    print(myTuple[i])
    i += 5

#2.

mylist = [23,45,12,10,25]
i = 0
sum = 0
while i < len(mylist):
    sum += mylist[i]
    i += 5
print(sum)

#3.

fruitslist = ['* , "mango" , "apple" , "orange" , "guava" , *']
while fruitslist:
    print(fruitslist.pop())
print(fruitslist)


#4

i = 0
word = "hello"
while i < len(word):
    if word[i] == "h" or word[i] == "o":
        i += 1
        continue
    print("returned letter" ,word[i])
    i += 1

#5

num = int(input("enter a number:"))
b = 0
p = 1
n = num
while n>0:
    rem = n%2
    b += rem*p
    p = p*10
    n = n//2
print("binary value:",b)

#6
p = 6
sum = 0
count = 0
while p>0:
    count = 1
    f = int(input ("enter the number"))
    sum += f
    p -= 1
average = sum/count
print("average of given number:" , everage)
