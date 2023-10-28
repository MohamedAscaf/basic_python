#factorial
'''

def factorial (x):
    if x==1 :
        return 1
    else:
        return (x*factorial (x-1))
num = 6
print ("the factorial of " , num , "is" , factorial (num))

'''

#lambda function
'''

x = lambda a : a + 12
print (x(6))
x = lambda a,b : a*b
print (x(8,9))
def my_function (n):
    return lambda a : a*n
my_doubler = my_function (1)
print (my_doubler (20))
print (my_doubler (3))
print (my_doubler (6))
print (my_doubler (8))

'''

#maping and filtering

'''

data = [1,2,3,4,5,6,7,8,9,10]
result1 = map(lambda x : x*8 , data)
print (list(result1))
result2 = filter (lambda x : x%5==0 , data)
print (list(result2))

'''

#work
#EMPLOYEE FUNCTION
'''

def salary_calculation (sal , distance):
    HouseRentAllowance = sal*0.20
    TranceportAllowance = float(distance)*100
    FlexibleBenefitPlan = sal*0.15
    Bonus = sal*0.5
    Profund = sal*0.05
    IncomeTax = sal*0.5
    Insurance = sal*0.3
    Total = float(salary) + float(HouseRentAllowance) + float(TranceportAllowance) + float(FlexibleBenefitPlan) + float(Bonus) - float(Profund) - float(IncomeTax) - float(Insurance)
    
    print ("basic salary \t\t:" ,sal)
    print ("HouseRentAllowance  \t:" , HouseRentAllowance)
    print ("TranceportAllowance \t:" , TranceportAllowance)
    print ("FlexibleBenefitPlan \t:" , FlexibleBenefitPlan)
    print ("Bonus \t\t\t:" , Bonus)
    print ("Profund \t\t:" , Profund)
    print ("IncomeTax \t\t:" , IncomeTax)
    print ("Insurance \t\t:" , Insurance)
    print("****************************************************")
    print ("your salary is \t\t:" ,Total)



EmployeeName = input("Enter the Employee Name:")
EmployeeID = int(input("Enter the Employee ID:"))
distance = input("Enter the distance:")
print ("select your disignation , 1.manager , 2.developer , 3.tester")
x=int(input())
if (x==1):
          designation ="Manager"
          salary = 50000
elif (x==2):
            designation = "Developer"
            salary = 20000
elif (x==3):
            designation = "Tester"
            salary = 15000
else:
    print ("you enter wrong value")
    
print("****************************************************")
print("\t\t Employee salary Calculation")
print("Employee ID   \t\t:",EmployeeID)
print("Employee Name \t\t:",EmployeeName)
print("Designation   \t\t:",designation)
salary_calculation(salary,distance)
print("****************************************************")
     
'''

#student mark calculation

def student_mark_calculation (sub1,sub2,sub3,sub4,sub5):
    total = sub1+sub2+sub3+sub4+sub5 
    avarage = total/5
    if (avarage>80):
         grade = "A"
    elif (avarage>70):
          grade = "B"
    elif (avarage>60):
          grade = "C"
    elif (avarage>50):
          grade = "D"
    else:
       grade="not qualify"
    if(sub1>50 and sub2>50 and sub3>50 and sub4>50 and sub5>50):
        result = "All Clear"
    else:
      result = "reappear"

    print("Total   : ",total)
    print("avarage : ",avarage)
    print("Grade   : ",grade)
    print("Result  : ",result)

Name = input("Enter the Name:")
RegNo = int(input("Enter the Reg.No:"))
Dept = input("Enter the Dept:")
Specific = input("Enter the Specific:")
Subject1 = float(input("Enter the Subject1:"))
Subject2 = float(input("Enter the Subject2:"))
Subject3 = float(input("Enter the Subject3:"))
Subject4 = float(input("Enter the Subject4:"))
Subject5 = float(input("Enter the Subject5:"))

print ("-----------------------------------------")
print ("student mark calculation")
print ("Name : ",Name)
print ("Reg.No: ",RegNo)
print ("Dept: ",Dept)
print ("Specific: ",Specific)
print ("Subject1: ",Subject1)
print ("Subject2: ",Subject2)
print ("Subject3: ",Subject3)
print ("Subject4: ",Subject4)
print ("Subject5: ",Subject5)
student_mark_calculation (Subject1,Subject2,Subject3,Subject4,Subject5)
print ("-----------------------------------------")
