# Q 30.) Write a Python program to convert a list of tuples into a dictionary. 


list_1 = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]

dict_1 = {}

for key , value in list_1:
    dict_1.setdefault(key, []).append(value)
print(dict_1)