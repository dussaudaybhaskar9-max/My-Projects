from exceptions import AccountNotFound , PhoneNumber ,AadharNotFound , PinMissMatch , InCorrectPin , InvalidAmount , InsuffiecntFunds
from encryption import encrypt
from decorator import delay
import time
import sqlite3
connect =  sqlite3.connect("Bank.db")
cursor = connect.cursor()

def new_acc_num():
    data = cursor.execute("select acc_num from Accounts").fetchall()
    data.sort(reverse=True)
    a =  data[0][0]+1
    return a


@delay
def acc_creation(name,phone,dob,email,address,gender,aadhar,nomine , relation,acc_type):
    acc = new_acc_num()
    cursor.execute(f"insert into Accounts (acc_num,name,phone,email,aadhar,address,dob,gender,nomine_name,nomine_relation,acc_type) values({acc},    '{name}',{phone},'{email}',{aadhar},'{address}','{dob}','{gender}','{nomine}','{relation}','{acc_type}') ")
    connect.commit()
    print("account created successfully")

@delay
def set_pin(acc,phone,aadhar):
    data = cursor.execute(f"select phone,aadhar from Accounts where acc_num = {acc}").fetchone()
    # print(data)
    if data:
        if data[0] == phone:
            if data[1] == aadhar:
                pin = int(input("enter the pin : "))
                c_pin = int(input("confirm the pin : "))
                if pin == c_pin:
                    cursor.execute(f"update Accounts set pin = '{encrypt(pin)}' where acc_num = {acc}")
                    connect.commit()
                    print("pin generated successfully")
                else:
                    raise PinMissMatch("enter same confirm pin as pin")
            else:
                raise AadharNotFound("enter the valid aadhar number")
        else:
            raise PhoneNumber("enter the registered mobile number")
    else:
        raise AccountNotFound("invalid acc number")

@delay
def check_balance(acc,pin):
    data = cursor.execute(f'select pin , balance from Accounts where acc_num = {acc}').fetchone()
    if data:
        if data[0] == encrypt(pin):
            print(f"The current Available Balance is {data[1]} ₹ ")
        else:
            raise InCorrectPin("pin is invalid")
    else:
        raise AccountNotFound("acc number is invalid")

@delay    
def deposit(acc,pin):
    data = cursor.execute(f"select pin , balance from Accounts where acc_num = {acc}").fetchone()
    if data:
        if data[0] == encrypt(pin):
            amt = int(input("ente the amt to depsoit : "))
            if amt>=100:
                if amt<=10000:
                    new_bal = data[1] + amt
                    cursor.execute(f"update Accounts set balance = {new_bal} where  acc_num = {acc} ")
                    connect.commit()
                    print("amt deposited successfully")
                else :
                    raise InvalidAmount("amount is huge please visit the branch ")
            else:
                raise InvalidAmount("amount must be more than 100")
        else:
            raise InCorrectPin("invalid pin")
    else:
        raise AccountNotFound("invalid acc number")
    
@delay
def withdrawl(acc,pin):
    data = cursor.execute(f"select pin , balance from Accounts where acc_num = {acc}").fetchone()
    if data:
        if data[0] == encrypt(pin):
            amt = int(input("enter the amt to withdraw "))
            if amt<=data[1]:
                if amt>=100:
                    new_bal = data[1]-amt
                    cursor.execute(f"update Accounts set balance = {new_bal}  where acc_num = {acc}")
                    connect.commit()
                    print("withdrawl done ")
                else:
                    raise InvalidAmount("amount must be greater than 100")
            else:
                raise InsuffiecntFunds("bichagadhu")
        else:
            raise InCorrectPin("invalid pin")
    else:
        raise AccountNotFound("invalid acc number")

@delay   
def account_transfer(f_acc,t_acc,pin):
    f_data = cursor.execute(f"select pin , balance from Accounts where acc_num = {f_acc}").fetchone()
    t_data = cursor.execute(f"select  balance from Accounts where acc_num = {t_acc}").fetchone()
    if f_data:
        if t_data:
            if f_data[0] == encrypt(pin):
                amt = int(input("enter the amount to transfer : "))
                if f_data[1] >= amt:
                    if amt>=1:
                        print("transaction started ... ")
                        time.sleep(3)
                        f_new_bal = f_data[1] -amt
                        cursor.execute(f"update Accounts set balance = {f_new_bal} where acc_num = {f_acc}")
                        connect.commit()
                        t_new_bal = t_data[0]+amt
                        cursor.execute(f"update Accounts set balance = {t_new_bal} where acc_num = {t_acc}")
                        connect.commit()
                        print("transaction completed")
                    else:
                        raise InvalidAmount("enter the valid amt")
                else:
                    raise InsuffiecntFunds("bichagahu")


            else:
                raise InCorrectPin("invalid pin ")
            
        else:
            raise AccountNotFound("receiver's acc is invalid ")
    else:
        raise AccountNotFound("sender acc is invalid")