# Q 45.) Write a Python program to find the highest 3 values in a dictionary.



my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5254, 'f': 20, 'g': 5962}

list_1 = []

for values in my_dict.values():
    list_1.append(values)
    list_1.sort()
    list_1.reverse()

print(list_1)
print("This is the 3 highest values in dictinory: ",list_1[:3])