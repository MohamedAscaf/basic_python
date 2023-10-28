
""" from ipaddress import collapse_addresses


class newclass:
    def __init__ (self,a,b):
        self.firstvalue=a
        self.secondvalue=b
    def add (self):
        return self.firstvalue+self.secondvalue
    

senthil=newclass(1,2)
print(senthil.add())

karthik=newclass(4,5)
print(karthik.add()) """

'''
class CalculatorSub:
    def __init__(self,x,y):
        self.firstvalue=x
        self.secondvalue=y
    def sub (self):
        return self.firstvalue-self.secondvalue
    
jack=CalculatorSub(1,2)
print(jack.sub())

rose=CalculatorSub(3,4)
print(rose.sub())

'''
'''
class CalculatorMul:
    def __init__(self,a,b):
        self.multiplication1=a
        self.multiplication2=b
    def mul(self):
        return self.multiplication1*self.multiplication2
    
harry=CalculatorMul(1,2)
print(harry.mul())

potter=CalculatorMul(3,4)
print(potter.mul())

'''

'''
class CalculatorDiv:
    def __init__(self,x,y):
        self.division1=x
        self.division2=y
    def div(self):
        return self.division1/self.division2
sir=CalculatorDiv(7,8)
print(sir.div())

mam=CalculatorDiv(3,4)
print(mam.div())

'''

"""
class calculator:
    def __init__(self,a,b):
        self.firstvalue=a
        self.secondvalue=b
    def add(self):
        return self.firstvalue+self.secondvalue
    def sub(self):
        return self.firstvalue-self.secondvalue
    def mul(self):
        return self.firstvalue*self.secondvalue
    def div(self):
        return self.firstvalue/self.secondvalue
    
harry=calculator(1,2)
print(harry.add())
print(harry.sub())
print(harry.mul())
print(harry.div())

"""

'''
 potter=calculator(3,4)
print(potter.mul()) 
'''

""" class classmate:
    def __init__(self,a,b):
        self.FirstStudent=a
        self.SecondStudent=b
    def add(self):
        return self.FirstStudent+self.SecondStudent
a=int(input("Enter the First Student Value:"))
b=int(input("Enter the Second Student Value:"))
karthikeiyan=classmate(a,b)
print(karthikeiyan.add())
AnanthanRaman=classmate(a,b)
print(AnanthanRaman.add()) """

""" class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Name : ",self.name," \nAge : ",self.age) 

class student(person):
    pass
ascaf=student("Ascaf",26)
ascaf.show() """

#example of class

""" class student:
    def StudentMark(self,x,y):
        self.firstvalue=x
        self.secondvalue=y
        print(self.firstvalue,self.secondvalue)

karthikeiyan=student()
karthikeiyan.StudentMark(12,21)
anantharaman=student()
anantharaman.StudentMark(45,54) """

"""
class classmate:
    def __init__(self,m,n):
        self.FirstClassMate=m
        self.SecoundClassMate=n
    def div(self):
        return self.FirstClassMate/self.SecoundClassMate
    
anbu=classmate(12,34)
print(anbu.div())

guna=classmate(56,78)
print(guna.div())

"""

#instance method

""" class person():
    def __init__(self,Name,Age):
        self.name=Name
        self.age=Age
    def show(self):
        print("Name :" , self.name , " \n Age :" , self.age)

karthikeiyan=person("karthikeiyan" , 20)
karthikeiyan.show() """

#inheridance
#single inheridance

""" class person():
    def __init__(self,Name,Age):
        self.name=Name
        self.age=Age

class student(person):
    def __init__(self, Name, Age,department):
        person.__init__(self,Name,Age)
        self.department=department
    def show(self):
        print("Name : ",self.name,"\nAge : ",self.age,"\nDepartment : ",self.department)



karthikeiyan=student("karthikeiyan" , 20,"m.sc")
karthikeiyan.show()
 """
#Example Student IDCard

""" class single():
    def __init__(self,Male,Female):
        self.male=Male
        self.female=Female

class student(single):
    def __init__(self,Male,Female,Trans):
        single.__init__(self,Male,Female)
        self.trans=Trans

    def show(self):
        print("Male   : " , self.male , "\nFemale : " , self.female ,  "\ntrans  :" , self.trans)

ID=student("kumarakanan" ,"thenmoli"," kumarikanan")
ID.show() """

#hierarchical inheritance

""" class person():
    def __init__(self,Name,Age):
        self.name=Name
        self.age=Age

class student(person):
    def __init__(self,Name,Age,Place):
        person.__init__(self,Name,Age)
        self.place=Place

    def show(self):
        print("Name   : " , self.name , "\nAge    : " , self.age ,  "\nPlace  :" , self.place)

ID=student("karthikeiyan" ,20," madurai")
ID.show() """

""" #father
class students():
    def __init__(self,Name,Age):
        self.name=Name
        self.age=Age
        
#son
class  LiveWireStudent(students):
    def __init__(self,Name,Age,Mark,Grade,Department):
        students.__init__(self,Name,Age)
        self.mark=Mark
        self.grade=Grade
        self.department=Department

    def show(self):
        print("-------------------------------")
        print("Name       : " , self.name , "\nAge        : " , self.age , "\nMark       : " , self.mark , "\nGrade      : " , self.grade , "\nDepartment : " , self.department)



MarkSheet=LiveWireStudent("Anantharaman" , 21 , 80 , "B" , "BBA" )
MarkSheet.show()
MarkSheet=LiveWireStudent("karthikeiyan" , 20 , 100 , "A" , "Msc" )
MarkSheet.show()
MarkSheet=LiveWireStudent("Ascaf" , 26 , 90 , "A" , "BE,IT" )
MarkSheet.show()
MarkSheet=LiveWireStudent("awinas" , 21 , 70 , "C" , "BCom" )
MarkSheet.show()
MarkSheet=LiveWireStudent("depak" , 23 , 80 , "B" , "Bsc" )
MarkSheet.show() """

#multilevel inheridance

""" #father
class students():
    def __init__(self,Name,Age):
        self.name=Name
        self.age=Age
        
#son
class  LiveWireStudent(students):
    def __init__(self,Name,Age,Department):
        students.__init__(self,Name,Age)
        self.department=Department
#grandson
class collegeStudent(LiveWireStudent):
    def __init__(self, Name, Age, Department,mark,grade):
        LiveWireStudent.__init__(self , Name, Age, Department)
        self.mark=mark
        self.grade=grade

    def show(self):
        print("Name       : " , self.name , "\nAge        : " , self.age , "\nMark       : " , self.mark , "\nGrade      : " , self.grade , "\nDepartment : " , self.department)
MarkSheet=collegeStudent("karthikeiyan" , 20 , 100 , "A" , "Msc" )
MarkSheet.show() """

#Multiple inheritance
""" class father:
    def print1(self):
        print("This is father class")
class mother:
    def print2(self):
        print("This is mother class")
class son(father,mother):
    pass

b=son()
b.print1()
b.print2() """

#hierarchical inheritance

""" class father():
    def print1(self):
        print("this is father class")

class son1(father):
    pass
class son2(father):
    pass

a=son1()
b=son2()
a.print1()
b.print1() """

#example Multiple Inheritance

""" class DadyClass:
      def print1(self):
          print("this is DadyClass")
class MummyClass:
      def print2(self):
          print("this is MummyClass")
class DaughterClass(DadyClass,MummyClass):
      pass
b=DaughterClass()
b.print1()
b.print2() """

#example hierarchical inheritance

""" class PapaClass():
      def print1(self):
          print("this is PapaClass")
class Baby1(PapaClass):
      pass
class Baby2(PapaClass):
      pass
x=Baby1()
y=Baby2()
x.print1()
y.print1() """

#hierarchical inheritance

""" class father:
  def print1(self,a,b):
        self.firstvalue=a
        self.secondvalue=b
        print("this is father class")
  def add(self):
      return self.firstvalue+self.secondvalue
family1=father()
family1.print1(45,78)
print(family1.add())

family2=father()
family2.print1(78,12)
print(family2.add())

class son1(father):
    pass
class son2(father):
    pass

family3=son1()
family4=son2()

family3.print1(12,78) 
print(family3.add())

family4.print1(36,89)
print(family4.add()) """

#Example hierarchical inheritance pass

""" class  LiveWireStudent():
    def __init__(self,Name,Age):
        self.name=Name
        self.age=Age
        

class students(LiveWireStudent):
    def __init__(self,Name,Age,Department):
        LiveWireStudent.__init__(self,Name,Age)
        self.department=Department
    print("-------------------") 
   
    def show1(self):
       
        print("Name       : " , self.name , "\nAge        : " , self.age ,"\nDepartment : " , self.department)
       

    def show2(self):
        print("Name       : " , self.name , "\nAge        : " , self.age ,"\nDepartment : " , self.department)
    
class students1(students):
    pass
MarkSheet1=students1("Anantharaman" , 21 ,  "BBA" )
MarkSheet1.show1()
print("-------------------") 
class students2(students):
    pass
MarkSheet2=students2("karthikeiyan" , 20 ,  "Msc" )
MarkSheet2.show2()

print("-------------------") """

#multiple inheritance

""" class father:
    def print1(self):
        print("This is father class")
class mother:
    def print2(self,x,y):
        self.firstvalue=x
        self.secondvalue=y
        print("This is mother class")
        return self.firstvalue+self.secondvalue
        

family1=father()
family1.print1()
family2=mother()
print(family2.print2(56,78))

class son(father,mother):
    pass
joinfamily=son()
joinfamily.print1()
print(joinfamily.print2(45,78)) """


#example Normal compamy Multiple inheritance

""" class Company:
      def MNC(self):
          print("This Is MNC Company")

class StartUpCompany:
      def HR(self):
          print("This Is StartUpCompany Im HR")

class Employee(Company,StartUpCompany):
       pass
a=Employee()
a.MNC()
a.HR() """

#example Hard Compamy Multiple inheritance

""" class Company:
      def MNC(self):
          print("This Is MNC Company")

class StartUpCompany:
      def HR(self):
          print("This Is StartUpCompany Im HR")

class Employee(Company,StartUpCompany):
      def __init__(self,Name,Age,Experiance):
          self.name=Name
          self.age=Age
          self.experiance=Experiance



a=Employee()
a.MNC()
a.HR() """

#example Multilevel Inheritance pass
""" 
#father
class students():
    def __init__(self,Name,Age):
        self.name=Name
        self.age=Age
        
#mother
class  AVCcollage(students):
    def __init__(self,Name,Age,Department):
        students.__init__(self,Name,Age)
        self.department=Department
#grandson
class CollegeStudent(AVCcollage):
    def __init__(self, Name, Age, Department,Mark,Grade):
        AVCcollage.__init__(self , Name, Age, Department)
        self.mark=Mark
        self.grade=Grade


    def show1(self):
        print("Name       : " , self.name , "\nAge        : " , self.age , "\nMark       : " , self.mark , "\nGrade      : " , self.grade , "\nDepartment : " , self.department)

    def show2(self):
        print("Name       : " , self.name , "\nAge        : " , self.age , "\nMark       : " , self.mark , "\nGrade      : " , self.grade , "\nDepartment : " , self.department)

    def show3(self):
        print("Name       : " , self.name , "\nAge        : " , self.age , "\nMark       : " , self.mark , "\nGrade      : " , self.grade , "\nDepartment : " , self.department)

    def show4(self):
        print("Name       : " , self.name , "\nAge        : " , self.age , "\nMark       : " , self.mark , "\nGrade      : " , self.grade , "\nDepartment : " , self.department)

print("-----------------------") 
class students1(CollegeStudent):
    pass
MarkSheet1=students1("guna" , 20 , 70 , "b" , "BBA" )
MarkSheet1.show1()
print("-----------------------")
class students2(CollegeStudent):
    pass
MarkSheet2=students2("anbu" , 26 , 80 , "b" , "Bsc.IT" )
MarkSheet2.show2()
print("-----------------------")
class students3(CollegeStudent):
    pass
MarkSheet3=students3("velu" , 28 , 60 , "c" , "Bsc.cs" )
MarkSheet3.show3()
print("-----------------------")
class students4(CollegeStudent):
    pass
MarkSheet4=students4("rajan" ,30 , 90 , "A" , "Bcom" )
MarkSheet4.show4()
print("-----------------------")
"""

""" class Cat:
      def __init__(self,Name,age):
          self.name=Name
          self.age=age
      def info(self):
          print(f"I Am A Cat.My Name Is {self.name}.I Am {self.age} Years Old.")
      def make_sound(self):
          print("meoow")

class Mouse:
      def __init__(self,Name,Age):
          self.name=Name
          self.age=Age
      def info(self):
          print(f"I Am A Mouse. My Name Is {self.name}.I Am {self.age} Years old.")
      
      def make_sound(self):
          print("--------------------")
          print("queaking")
          
Cat1=Cat("TOM",3.2)
mouse1=Mouse("JERRY",3)

for animal in (Cat1,mouse1):
    animal.make_sound()
    animal.info()
    animal.make_sound() """



#example Hard Compamy Multiple inheritance

""" class Company:
      def MNC(self):
          print("This Is MNC Company")
      def salary(self,experience):
           if(experience==0):
                print("Your Salary is 15k")
           elif(experience>0 and experience<4):
                print("Your salary is 25k")
           elif(experience>3 and experience<6):
                print("Your Salary is 50k")
           else:
                print("you are not eligible this post") 
                                                        
class StartUpCompany:
      def HR(self,Age,Developer):
          self.age=Age
          self.developer=Developer
          print("This Is StartUpCompany Im HR")
      def check(self):
          if(self.age>20 and self.age<30):
                print("your age is valid")
                if(self.developer=="python"):
                    print("your qualification also valid")
                    
                else:
                    print("your qualification not valid")

          else:
               print("your age is not valid , sorry you are not selected") 
class Employee(Company,StartUpCompany):
      def __init__(self,Name,Age,Developer,Experience):
          self.name=Name
          self.age=Age
          self.developer=Developer
          self.experience=Experience
          print("-----------------------------------")
          StartUpCompany.HR(self,Age,Developer)
          StartUpCompany.check(self)
          Company.salary(self,Experience)
          print("-----------------------------------")


a=Employee("arjun",25,"python",3)
b=Employee("karthikeiyan",23,"fullstack",4)
c=Employee("anantharaman",24,"tally",5)
d=Employee("ascaf",26,"python",0) """



#polymorphism

class Cat:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

   def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound() 
