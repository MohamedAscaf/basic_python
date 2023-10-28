'''
class newclass:
 A=7
 def add(self,a,b):
     self.firstvalue=a
     self.secondvalue=b
 def add1(self):
     return self.firstvalue+self.secondvalue

senthilkumar = newclass()
senthilkumar.add(1,2)
print(senthilkumar.add1())

karthikeiyan = newclass()
karthikeiyan.add(3,4)
print(karthikeiyan.add1())

'''

class a:
    def question(self,a,b):
        self.first=a
        self.second=b
        print(self.first,self.second)
        
ascaf=a()
ascaf.question(12,34)

ananth=a()
ascaf.question(34,12)