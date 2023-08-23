fnm = input("Enter the Firstname:")
lnm = input("Enter the Lastname:")

if fnm.isupper() and lnm.isupper():
    print("Good work")
    email = input("Enter Your Email:")
    if email.islower():
        print("Fine")
        pwd = input("Enter the Password:")
        cpwd = input("Confirm The Password:")
        if pwd == cpwd:
            print("Good work")
            no = input("Enter the Mobile Number:")
            if no.isdigit() and len(no) == 12:
                print("You Have Submitted the data.")
            else:
                print("Mobile Number is wrong.")
        else:
            print("Password doesn't match.")
    else:
        print("Email is not in lower case.")
else:
    print("Name And Lastname in not in upper case")


