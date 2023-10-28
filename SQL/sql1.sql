show databases;
create database car;
use car;
create table car1(id int,name varchar(255),model varchar(255));
insert into car1(name,model) values("honda","2015");
select * from car1;


create table car2 (id int not null auto_increment,primary key(id),name varchar(255),model varchar(255));
insert into car2(name,model) values("nam2","2016");
select * from car2;