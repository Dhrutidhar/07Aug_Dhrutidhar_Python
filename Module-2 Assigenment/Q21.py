# Q 21.) Write a Python function to reverses a string if its length is a multiple of 4.


string = input("Enter the long string : ")

if len(string)%4==0:
    print(string[::-1])
else:
    print("Not a Muliple of 4")
    
