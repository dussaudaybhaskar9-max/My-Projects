def acc_creation_inputs():
    name = input("mi peru chepachu kadha..📛 ")
    phone = int(input("number este break istaa ..☎️"))
    gen = int(input("Sir miru Madam aa \n1)Yes 👧\n2)No👦"))
    if gen == 1:
        gender = "Female"
    elif gen == 2:
        gender = "Male"
    else:
        gender = "All of the Above"
    address = input('address pettuu ..🛖')
    aadhar = int(input("bus free aa : 🚌 "))
    dob = input("ippatiki inka na vayasu ...🏥 ") 
    email = input("we will get back to u ... 📧: ")
    nomine = input("adigithey thantha...🦿")
    relation = input("sambandam yenti \n1)Akrama Sambandam \n2)Ex wife\n3)Ex girlfriend\n4)Aunty \n5)Ex Husband \n6)boyfriend \n7)Uncle")
    acc = int(input("enter your type \n1)Savings\n2)Current\n3)Joint"))
    if acc == 1:
        acc_type = "Savings Account"
    elif acc == 2:
        acc_type = "Current Account"
    else:
        acc_type = "Joint Account "
    details = {
        'name':name,
        'phone':phone,
        'aadhar':aadhar,
        'email':email,
        'dob':dob,
        'address':address,
        'gender':gender,
        'nomine':nomine,
        'relation':relation,
        "acc_type":acc_type
    }
    return details

def set_pin_inputs():
    acc_num = int(input("enter the acc number : "))
    phone = int(input("enter your mobile number : "))
    aadhar = int(input("enter the aadhar number : "))
    details = {
        'acc':acc_num,
        'phone':phone,'aadhar':aadhar
    }
    return details


def transaction_inputs():
    acc = int(input("enter the acc number : "))
    pin = int(input("enter the pin : "))

    details = {
        'acc': acc,
        'pin':pin
    }
    return details

def acc_transfer_inputs():
    f_acc = int(input("enter the Sender's acc number : "))
    t_acc = int(input("enter the Receiver's acc number : "))
    pin = int(input("enter the pin : "))

    details = {
        'f_acc': f_acc,
        'pin':pin,
        't_acc':t_acc,
    }
    return details