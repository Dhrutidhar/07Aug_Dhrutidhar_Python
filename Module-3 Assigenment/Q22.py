# Q 22.) Write a Python program to check whether an element exists within a tuple. 


n = int(input("Enter no. of length you want to make tuple: "))
list1 = []



for i in range(n):
    i= input("Enter the word to make tuple: ")
    list1.append(i)
print(tuple(list1))


ele = input("Enter elements to search: ")
if ele in list1:
    print("True")
else:
    print("False")

print(ele in list1)