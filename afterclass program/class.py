# class person:
#     def __init__(self,name,fathername):
#         self.name=name
#         self.fathername=fathername
#     def details(self):
#         print(f"my name is{self.name},my fathername is{self.fathername}")
#     def personstate(self):
#         print("tamilnadu")
# class person1:
#     def __init__(self,name,fathername):
#         self.name=name
#         self.fathername=fathername
#     def details(self):
#         print(f"my name is{self.name},my father name is{self.fathername}")
#     def personstate(self):
#         print("kerla")
#
# name=input("enter the name:")
# aksh=input("enter the fathername:")
# ram=person(name,aksh)
# a=input("enter the name:")
# b=input("enter the fathername:")
# akash=person1(a,b)
#
# for person in(ram,akash):
#     person.details()
#     person.personstate()

class Bank:
    def __init__(self,customername):
        self.customername=customername
    def fact(self):
        return self.customername
class SBI(Bank):
    def __init__(self,place):
        super().__init__("mayiladuthurai")
        self.place=place
    def fact1(self):
        return " place ",self.place
class RBI(Bank):
    def __init__(self,customername1):
        super().__init__(customername1)
        self.customername1=customername1
    def fact2(self):
        return "customer name:",self.customername1
# class got(animal):
#     def fact3(self):
#         return "i am a got"
# class lion(animal):
#     def fact4(self):
#         return "i am a lion"

a=RBI("akash")
print(a.fact())
print(a.fact2())
