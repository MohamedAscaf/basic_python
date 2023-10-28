# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#
#   def printname(self):
#     print(self.firstname, self.lastname)
#
# class Student(Person):
#   pass
#
# x = Student("Mike", "Olsen")
# x.printname()




# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#
#   def printname(self):
#     print(self.firstname, self.lastname)
#
# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)
#
# x = Student("Mike", "Olsen")
# x.printname()



# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#
#   def printname(self):
#     print(self.firstname, self.lastname)
#
# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
#     self.graduationyear = 2019
#
# x = Student("Mike", "Olsen")
# print(x.graduationyear)



# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#
#   def printname(self):
#     print(self.firstname, self.lastname)
#
# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year
#
# x = Student("Mike", "Olsen", 2019)
# print(x.graduationyear)



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class College(Person):
  def __init__(self, fname, lname, college):
    super().__init__(fname, lname)
    self.college = college
  def printn(self):
    print(self.firstname,self.lastname,self.college)


class Student(College):
  def __init__(self,fname,lname,class1,degree):
    super().__init__(fname,lname,class1)
    self.Degree=degree

mani=Student("Mani","Kandan","abc","M.E")
mani.printname()
mani.printn()
print(mani.Degree)

