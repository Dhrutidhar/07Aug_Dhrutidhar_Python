# Q 37.) Write a Python script to print a dictionary where the keys are numbers between 1 and 15.


dict_1 = {}

for key in range(1,16):
    value = input(f"Enter the {key} Value:")
    dict_1[key]=value

print(dict_1)  
    