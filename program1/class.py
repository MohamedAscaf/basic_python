class newclass:
 A=5
 def add(self,a,b):
    self.firstvalue=a
    self.secondvalue=b
 def add1(self):
    return self.firstvalue+self.secondvalue

senthil=newclass()
senthil.add(2,3)
print(senthil.add1())

karthik=newclass()
karthik.add(2,5)
print(karthik.add1())