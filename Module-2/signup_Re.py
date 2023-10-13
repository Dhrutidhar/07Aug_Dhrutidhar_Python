import re

class signup :

    def Firstname(self):

        nm = input("Enter the Firstname: ")
        nm_pattern = "^[A-Za-z]+[A-z|a-z]$"

        a = re.findall(nm_pattern, nm)
        if a:
            print("Name is Valid:")
            print("\t Firstname: ", nm)
            self.Lastname()
        else:
            print("Name is InValid")
            self.Firstname()

    def Lastname(self):
        
        lnm = input("Enter the Lastname: ")
        lnm_pattern = "^[A-Za-z]+[A-Z|a-z]$"
        
        b = re.findall(lnm_pattern, lnm)
        if b:
            print("Lastname is Valid")
            print("\t Lastname: ", lnm)
            self.Email()
        else:
            print("Name is InValid")
            self.Lastname()

    def Email(self):

        email = input("Enter the Email: ")
        email_pattern = "^[a-z0-9]+[@]+[a-z]+[\.]+[a-z]{2,4}$"
        
        c = re.findall(email_pattern,email)
        if c:
            print("Email is Valid")
            print("\t Email: ", email)
            self.Password()
        else:
            print("Email is InValid")
            self.Email()

    def Password(self):

        pwd = input("Enter the Password [8-12]: ")
        pwd_pattern = "[A-Za-z0-9@#$!_]+[A-Za-z0-9@#$!_]+[A-Za-z0-9@#$!_]+[A-Za-z0-9@#$!_]"
        
        d = re.findall(pwd_pattern, pwd)
        if d:
            if 8<= len(pwd) <= 12:
                print("Password is valid")
                cpwd = input("Enter the Confirm Password: ")
                if cpwd == pwd:
                    print("Password is Same")
                    self.Mobile_number()
                else:
                    print("Password is not same")
                    self.Password()
            else:
                print("Error!! len is short!")
                self.Password()
        else:
            print("Password is not valid")
            self.Password()

    def Mobile_number(self):

        no = input("Enter the Mobile Number: ")
        no_pattern = "[0-9]"
        
        e = re.findall(no_pattern, no)
        if e:
            if len(no) == 10:
                print("Mobile Number is Valid")
                print("\t Mobile Number: ", no)
                self.Success()
            else:
                print("Mobile Number is Invalid")
                self.Mobile_number()
        else:
            print("Mobile Number is Invalid")
            self.Mobile_number()

    def Success(self):
        print("\tSignup Successfull.....")


sign = signup()
sign.Firstname()

      