# Q 20.) Write a Python program to create a tuple with numbers.



num = int(input("Enter no. of values: "))
list_1 = []



for i in range(num):
    i= input("Enter valid integer : ")
    if i.isnumeric():
        list_1.append(i)
    else:
        pass
print(tuple(list_1))