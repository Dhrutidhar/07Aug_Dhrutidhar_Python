# Q 7.) Write a Python program to remove duplicates from a list.


list_1 = [28, 42, 28, 16, 90, 42, 42, 28]
list1 = []
list2 = []

for i in list_1:
    if i not in list1:
        list1.append(i)
    else:
        list2.append(i)

print("List without duplicate values: ",list1)
print("List of duplicates values: ",list2)
