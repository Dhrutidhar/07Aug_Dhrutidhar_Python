import datetime
import random

file = open("Student_Data.txt",'w')
n = int(input("Enter ths number of student you have to make data: "))

for i in range(n):
    stname = input("Enter the name: ")
    stsub = input("Enter the subject: ")
    stdateandtime = datetime.datetime.now()
    stid = random.randrange(1000, 9999)

    file.write(f"Current Date and Time is: {stdateandtime}\n")
    file.write(f"Id is: {stid}\n")
    file.write(f"Name is: {stname}\n")
    file.write(f"Subject is: {stsub}\n------------------------\n")

