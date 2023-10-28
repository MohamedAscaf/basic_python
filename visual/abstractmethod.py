""" from abc import ABC, abstractmethod
#example
class HotelHakim(ABC):
    def bai_info(self):
        print("welcome to Hotel Hakim Bai Biriyani")
    @abstractmethod
    def Biriyani(self):
        "abstarct method"
        pass
class HotelDhawus(HotelHakim):
      def Biriyani(self):
          print("5 Bucket Biriyani")
class DindigulThalapakattuBiryani():
      def Biriyani(self):
          print("6 Bucket Biriyani")
class ssHyderabadBiryani():
      def Biriyani(self):
          print("8 Bucket Biriyani")
class BuhariHotel():
      def Biriyani(self):
          print("3 Bucket Biriyani")
class BismiBiryani():
      def Biriyani(self):
          print("9 Bucket Biriyani")
class YaMohideenBiryani():
      def Biriyani(self):
          print("10 Bucket Biriyani")

a=HotelDhawus()
b=DindigulThalapakattuBiryani()
c=ssHyderabadBiryani()
d=BuhariHotel()
e=BismiBiryani()
f=YaMohideenBiryani()

for x in (a,b,c,d,e,f):
     x.Biriyani() """



'''
from abc import ABC, abstractmethod

class Bank(ABC):
   def bank_info(self):
       print("Welcome to bank")
   @abstractmethod
   def interest(self):
       "Abstarct Method"
       pass
#Sub class/ child class of abstract class
class SBI(Bank):
      def interest(self):
          print("5 percentage")

s= SBI()
s.bank_info ()
s.interest()
'''



""" from abc import ABC, abstractmethod

class bank(ABC):
    def bank_info(self):
        print("welcome to bank")
    @abstractmethod
    def interest(self):
        pass
class SBI(bank):
    def interest(self):
        print("welcome to SBI bank")
    def balance(self):
        print("balance is 200")
    def GST(self):
        print("Goods and Services Tax")

s=SBI()
s.bank_info()
s.interest()
s.balance()
s.GST() """



""" from abc import ABC, abstractmethod

class bank(ABC):
    def bank_info(self):
        print("welcome to bank")
    @abstractmethod
    def interest(self):
        pass
class SBI(bank):
    def interest(self):
        print("welcome to SBI bank")
    
class IOB(bank):
    def interest(self):
        print("balance is 200")

class IB(bank):
    def interest(self):
        print("Goods and Services Tax")

class BOB(bank):
    def interest(self):
        print("service and personal")

class PNB(bank):
    def interest(self):
        print("Accounts and Deposits")

a=SBI()
b=IOB()
c=IB()
d=BOB()
e=PNB()
for x in (a,b,c,d,e):
     x.interest() """



""" from abc import ABC, abstractmethod

class Bank(ABC):
    def bank_info(self):
        print("Welcome To Bank")
    @abstractmethod
    def interest(self):
        "Abstract Method"
        pass

class SBI(Bank):
    def balance(self):
        print("balance is 50")
class sub1(SBI):
    def interest(self):
        print("In SBI Bank Interest is 3 Rupees")
s=sub1()
s.bank_info()
s.balance()
s.interest() """



""" from abc import ABC, abstractmethod

class One(ABC):
    @abstractmethod
    def calculate(self,a):
        pass
class square(One):
    def calculate(self,a):
        print("square:" , (a*a))
class Cube(One):
    def calculate(self, a):
        print("Cube: ",(a*a*a))
s=square()
c=Cube()
s.calculate(2)
c.calculate(2) """

