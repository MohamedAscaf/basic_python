def name(**na):
    print("Welcome",na["name1"])

name(name1="Senthil",name2="karthi")

def fname(*na):
    print("Vanakkam",na[1])
fname("Senthil","karthi")

def X(k1,k2):
    print("hello",k2)
X(k2="senthil",k1="haiiii")


def country(c="india"):
    print(c)

country("Austria")
country()

fruit=["apple","orange","pinapple"]

def fru(fruits):
    for x in fruits:
        print(x)
fru(fruit)
