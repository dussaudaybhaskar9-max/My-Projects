from inputs import acc_creation_inputs , set_pin_inputs , transaction_inputs , acc_transfer_inputs
from functions import acc_creation , set_pin , check_balance , deposit , withdrawl , account_transfer

while True:
    print("WELCOME TO Dochey Bank \n all dongana sons as well as daughter are weclome ")
    op = int(input("Select The Below Options \n1)Account Creation \n2)Pin Generation \n3)Check Balance \n4)Deposit\n5)WithDraw\n6)Account To Account Transfer\n--------->"))
    if op == 1:
        details = acc_creation_inputs()
        acc_creation(name = details['name'],phone=details['phone'],dob = details['dob'],email=details['email'],address= details['address'],gender=details['gender'],aadhar=details['aadhar'],nomine=details['nomine'],relation=details['relation'],acc_type=details['acc_type'])
    elif op == 2:
        details = set_pin_inputs()
        set_pin(acc= details['acc'],phone= details['phone'],aadhar=details['aadhar'])
    elif op == 3:
        details = transaction_inputs()
        check_balance(acc=details['acc'],pin = details['pin'])
    elif op == 4:
        details = transaction_inputs()
        deposit(acc=details['acc'],pin = details['pin'])
    elif op==5:
        details = transaction_inputs()
        withdrawl(acc=details['acc'],pin = details['pin'])
    elif op ==6:
        details = acc_transfer_inputs()
        account_transfer(f_acc=details['f_acc'],t_acc=details['t_acc'],pin = details['pin'])
        
    else:
        exit()

