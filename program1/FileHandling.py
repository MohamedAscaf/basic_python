#open the file and append

f=open("my file.text" , "a")
f.write("python start new sofware")
f.close()

#open and read the file after the appending

f = open ("myfile.txt" , "r")
print(f.read())

#create a new file

f=open ("myfile.txt" , "x")

#remove the file

if os.path.exists("myfile.txt"):
   os.remove("myfile.txt")
else:
    print("the file does not exist")

#remove the folder

import os
os.rmdir("MyFile")
