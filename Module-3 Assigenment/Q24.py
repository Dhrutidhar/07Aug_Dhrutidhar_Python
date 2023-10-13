# Q 24.) Write a Python program to convert a list to a tuple. 



list_1 = []

n = int(input("Enter number of inputs you want to make a list:"))
for i in range(n):
    i = input("Enter the values:")
    list_1.append(i)
print("List is:",list_1)    
    
tuple_1 = tuple(list_1)
print("Tuple is:",tuple_1)


