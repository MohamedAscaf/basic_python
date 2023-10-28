class Students:
   def __init__(self, name, rank, points):
      self.name = name
      self.rank = rank
      self.points = points

   # custom function
   def demofunc(self):
      print("I am "+self.name)
      print("I got Rank ",+self.rank)

# create 4 objects
st1 = Students("Steve", 1, 100)
st2 = Students("Chris", 2, 90)
st3 = Students("Mark", 3, 76)
st4 = Students("Kate", 4, 60)

# call the functions using the objects created above
st1.demofunc()
st2.demofunc()
st3.demofunc()
st4.demofunc()


class Employee:
    # constructor
    def __init__(self, name, id, salary, project):
        # data members
        self.name = name
        self.id = id
        self.salary = salary
        self.project = project
 
    # method to print employee's details
    def show_sal(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)
 
 
    def proj(self):
        print(self.name, 'is working on', self.project)
 
# creating object of a class
emp = Employee('James', 102, 100000, 'Python')
 
# calling public method of the class
emp.show_sal()
emp.proj()

