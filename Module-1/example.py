'''number= int(input("Enter the number: "))

if number <0:
    print("Number is Negative")
elif number >0:
        print("Number is Positive")

else:
    print("This Number is Zero")'''



a = int(input("Enter the A:"))
b = int(input("Enter the B:"))
if a != 0 and b != 0:
    if a > b:
        print("Sum of the number: ", a+b)
    if a < b:
        print("Sub of the number: ", b-a)
else:
    print("Error")
