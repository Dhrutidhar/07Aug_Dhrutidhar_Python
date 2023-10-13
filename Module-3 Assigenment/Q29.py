# Q 29.) Write a Python program to unzip a list of tuples into individual lists.



list_1 = [('Have', 15), ('A', 50), ('Nice', 25), ('Day', 95)]

list_2 = []
list_3 = []
for i in list_1:
    list_2.append(i[0])
    list_3.append(i[1])
print("Original List of Tuple is: ", list_1)
print(f"List 1 is:  {list_2}")
print("List 2 is: ", list_3)