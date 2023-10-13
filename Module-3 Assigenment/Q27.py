# Q 27.) Write a Python program to find the repeated items of a tuple.



my_tuple = (1, 2, 2, 3, 4, 4, 5, 6, 6)

repeat = []
unique = []

for i in my_tuple:
    if i in unique:
        repeat.append(i)
    else:
        unique.append(i)

repeat_1 = tuple(repeat)
unique_1 = tuple(unique)

print("Original Tuple:", my_tuple)
print("Unique Tuple: ", unique_1 )
print("Repeated Items:", repeat_1)