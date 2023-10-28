#MYSQL JOIN PY
#
# import pymysql as mysql1
# connection = mysql1.connect(host="localhost",user="root",password="livewire")
# print(connection)
# cursor=connection.cursor()

#CREATE DATABASE
# cursor.execute("create database mysqljoinpy")

#PRINT DATABASES
# cursor.execute("show databases")
# for x in cursor:
#     print(x)

#IMPORTANT
import pymysql as mysql1
connection = mysql1.connect(host="localhost",user="root",password="livewire",database="mysqljoinpy")
cursor=connection.cursor()

#CREATE TABLE

# cursor.execute("create table python(id int not null auto_increment primary key,name varchar(255))")
# cursor.execute("show tables")
# print("Number of tables in database :")
# for x in cursor:
#     print("\t",x)

#SINGLE INSERT
# s="insert into python(name) values(%s)"
# t=("ramayanam")
# cursor.execute(s,t)
# connection.commit()

#MULTIPLE INSERT
# s="insert into python(name) values(%s)"
# t=[("rama"),("sita")]
# cursor.executemany(s,t)
# connection.commit()
# print(cursor.rowcount," new row inserted")

# #PRINT DATAS
# cursor.execute("select * from python")
# result=cursor.fetchall()
# print("Content In The python :")
# for x in result:
#     print("\t",x)

# cursor.execute("DELETE FROM python WHERE id=3")
# connection.commit()
# print(cursor.rowcount, "record(s) deleted")

# sql = "DROP TABLE python"
# cursor.execute(sql)
# connection.commit()


# cursor.execute("drop database mysqljoinpy")
# connection.commit()
