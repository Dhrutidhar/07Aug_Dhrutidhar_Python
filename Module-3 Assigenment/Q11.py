# Q 11.) Write a Python function that takes a list and returns a new list with unique elements of the first list.


list_1 = []
n = int(input("Enter the Number You have to make list: "))

for i in range(n):
    x = int(input("Enter Unique Number: "))
    if i not in list_1:
        list_1.append(x)
print(list_1)

