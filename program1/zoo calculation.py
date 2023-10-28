#VandalurZooCalculation     st date : 24 8 1985 | DSA : 1,265 | WS :1979 | PZ : 605 

def Basic():
    print("***Enter the Basic***")
    ZooName = (input("Enter the Zoo Name:"))
    StartingYear = int(input("Enter the Statring Year:"))
    DepartmentSetAside = int(input("Enter the Department Set Aside:"))
    Place = (input("Enter the Place:"))
    WorkStarting = int(input("Enter the Work Starting:"))
    ParkSize = int(input("Enter the Park Size:"))
    return ZooName,StartingYear,DepartmentSetAside,Place,WorkStarting,ParkSize
def Species():
    print("***Enter the Species***")
    Mammals = int(input("Enter No of Mammals : "))
    Birds = int(input("Enter No of Birds : "))
    Reptilles = int(input("Enter No of Reptilles : "))
    Amphibians = int(input("Enter No of Amphibians : "))
    Fish = int(input("Enter no of Fish : "))
    return Mammals,Birds,Reptilles,Amphibians,Fish
def animals():
    print("***Enter the Animals***") 
    Mammals1 = int(input("Enter No of Mammals : "))
    Birds1 = int(input("Enter No of Birds : "))
    Reptilles1 = int(input("Enter No of Reptilles : "))
    Amphibians1 = int(input("Enter No of Amphibians : "))
    Fish1 = int(input("Enter no of Fish : "))
    return Mammals1,Birds1,Reptilles1,Amphibians1,Fish1

def Zoo_Calculation():
    ZooName,StartingYear,DepartmentSetAside,Place,WorkStarting,ParkSize=Basic()
    Mammals,Birds,Reptilles,Amphibians,Fish=Species()
    Total_Species=Mammals+Birds+Reptilles+Amphibians+Fish
    Mammals1,Birds1,Reptilles1,Amphibians1,Fish1=animals()
    Total_Animals=Mammals1+Birds1+Reptilles1+Amphibians1+Fish1
    TotalYearCalculation=Total_Species+Total_Animals
    print(" \n basic : \n ZooName :",ZooName," \n StartingYear :",StartingYear," \n DepartmentSetAside:",DepartmentSetAside," \n Place:",Place," \n WorkStarting",WorkStarting," \n ParkSize:",ParkSize)
    print(" \n Species : \n Mammals:",Mammals," \n Birds : ",Birds," \n Reptilles:",Reptilles," \n Amphibians",Amphibians," \n Fish:",Fish)
    print(" \n Animal : \n Mammals:",Mammals1," \n Birds : ",Birds1,"\n Reptilles:",Reptilles1," \n Amphibians",Amphibians1," \n Fish:",Fish1)
    print("--------------------------------")
    print("Total Species",Total_Species)
    print("Total Animals",Total_Animals)
    print("Total Year Calculation",TotalYearCalculation)
    print("--------------------------------")

Zoo_Calculation()
    
    
'''
Mammals,Birds,Reptilles,Amphibians,Fish=Species()
print(Mammals,Birds,Reptilles,Amphibians,Fish)
'''

   
