# Q 17.) Write a Python program to split a list into different variables.


list_1 = ['d', 'r', 'u', 't', 'i', 'd', 'h', 'a', 'r']

str1 = ""
for i in list_1:
   v = i
   v = input(f"Enter value of variable of {i}:")
   print(f"{i}=",v)
