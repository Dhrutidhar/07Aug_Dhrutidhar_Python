# Q 15.) Write a Python program to get unique values from a list.


list_1 = []

no = int(input("Enter no. of elements to make list:"))

for i in range(no):
    x = input("Enter unique values:") 
    list_1.append(x)

print(list_1)
print(set(list_1))