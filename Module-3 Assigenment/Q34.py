# Q 34.) Write a Python script to check if a given key already exists in a dictionary.


dict_1={'ID':'1', 'Sub':'Python', 'City':'Rajkot', 'Name':'Dhrutidhar'}

key = input("Enter the Key you want to check: ")

if key in dict_1.keys():
    value = input("Enter the Value: ")
    print("Key already Exists...")   
    
    if value in dict_1.values():
        print("Value already Exists...")   
    else:
        dict_1[key]=value
        print(f"Value is not Present in {dict_1}")
else:
    print("Key is not Prsent!!!")