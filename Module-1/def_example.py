def getdata(*data):
    print("Student Id is: ", data[0])
    print("Student Name is: ", data[1])
    print("Student Subject is: ", data[2])
    print("Student City is: ", data[3])

n = int(input("Enter the number of student you have to make list: "))

for i in range(n):
    id = input("Enter Student Id: ")
    nm = input("Enter Studnet Name: ")
    sub = input("Enter Student Subject: ")
    ct = input("Enter Student City: ")
    
    getdata(id, nm, sub, ct)