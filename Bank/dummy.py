import sqlite3
connect =  sqlite3.connect("Bank.db")
cursor = connect.cursor()
# cursor.execute("create table Accounts (acc_num number primary key , name varchar(100) not null  ,phone number unique ,email varchar(50) not null , dob date not null  , aadhar number unique , address varchar(100) not null , acc_type  varchar(20) not null , gender varchar(10) not null , nomine_name varchar(50) not null , nomine_relation varchar(100) not null,pin default('0000'), balance number default(1000)) ;")
# print("table created")

# cursor.execute("insert into Accounts (acc_num,name,phone,email,aadhar,address,dob,gender,nomine_name,nomine_relation,acc_type) values(1234567890,'Sagar',9848326612,'raiden.sagar6066@gmail.com',987123456098,'bangalore','16-07-2010','Male','junnu','sweety','Saving Accounts') ")
# connect.commit()