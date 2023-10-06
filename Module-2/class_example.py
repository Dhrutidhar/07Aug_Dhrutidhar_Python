class studinfo:
        stid = 0
        stname = ''
        def getdata(self):
            self.stid = input("Enter the Id: ")
            self.stname = input("Enter the Name: ")
        def printdata(self):
            print("Id: ", self.stid)
            print("Name: ", self.stname)

st1 = studinfo()
st1.getdata()
st1.printdata()
