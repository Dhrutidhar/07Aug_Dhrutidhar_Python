# Q 38.) Write a Python program to check multiple keys exists in a dictionary.


dict_1={'id':'1', 'sub':'python', 'city':'rajkot', 'name':'dhrutidhar'}

for key in dict_1:
    key1 = input("Enter the key to find in keyword 1: ")
    key2 = input("Enter the key to find in keyword 2: ")


    if key1 in dict_1.keys() and key2 in dict_1.keys():
        print("Both keys are Present.")
    elif key1 in dict_1.keys() or key2 in dict_1.keys():
        print("Any One Key is Present.")
    else:
        print("NONE is Present!!")
    break