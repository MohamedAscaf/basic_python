from tkinter import*
from tkinter import ttk, messagebox,font


def insert(n1,n2,n3,n4,n5,n6,n7,n8,n9):
    if(n4==1):
        a="Male"
    elif(n4==2):
        a="Female"
    else:
        a="Other"
    import pymysql as mysql
    connection = mysql.connect(host="localhost",user="root",password="livewire",database="student")
    cursor=connection.cursor()
    s="insert into stud1(studentname,fathername,mothername,gender,dateofbirth,email,level1,department,telmobile) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    t=(n1,n2,n3,a,n5,n6,n7,n8,n9)
    cursor.execute(s,t)
    connection.commit()
    messagebox.showinfo( "Success", "User Insert Successfully")


a=Tk()
a.geometry("500x500")

label_font = font.Font(weight="bold", family="Times New Roman", size=30)

m1=Label(a,text="STUDENT REGISTRATION")
m1.grid(row=0 , column=1)
m2=Label(a,text="Student Name :")
m2.grid(row=1 , column=1)
m3=Label(a,text="Father's Name :")
m3.grid(row=2 , column=1)
m4=Label(a,text="Mother's Name :")
m4.grid(row=3 , column=1)
m5=Label(a,text="Gender :")
m5.grid(row=4 , column=1)
m6=Label(a,text="Date Of Birth :")
m6.grid(row=5 , column=1)
m7=Label(a,text="E-Mail :")
m7.grid(row=6 , column=1)
m8=Label(a,text="Level :")
m8.grid(row=7 , column=1)
m9=Label(a,text="Department :")
m9.grid(row=8 , column=1)
m10=Label(a,text="Tel/Mobile :")
m10.grid(row=9 , column=1)

n1= Entry(a)
n1.grid(row=1 , column=2)
n2= Entry(a)
n2.grid(row=2 , column=2)
n3= Entry(a)
n3.grid(row=3 , column=2)
a1=IntVar()
n40= Radiobutton(a , text=" Male",variable=a1,value=1)
n40.grid(row=4 , column=2)
n41= Radiobutton(a , text="Female",variable=a1,value=2)
n41.grid(row=4 , column=3)
n42= Radiobutton(a , text="other",variable=a1,value=3)
n42.grid(row=4 , column=4)
n5= Entry(a)
n5.grid(row=5 , column=2)
n6= Entry(a)
n6.grid(row=6 , column=2)
n7= ttk.Combobox(a,values=["high School","Under Graduate","Post Graduate"])
n7.grid(row=7 , column=2)
n8= ttk.Combobox(a,values=["Secondary School","Bachelor's of Engineering","Master's of Engineering"])
n8.grid(row=8 , column=2)
n9= Entry(a)
n9.grid(row=9 , column=2)
n10=Button(a,text="save",activebackground="blue",command=lambda :insert(n1.get(),n2.get(),n3.get(),a1.get(),n5.get(),n6.get(),n7.get(),n8.get(),n9.get()))
n10.grid(row=10 , column=2)
a.mainloop()
