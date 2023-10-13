# Q 9.) Write a Python function that takes two lists and returns true if they have at least one common member. 


list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

flag = 0
 
for elem in list2:
    if elem in list1:
        flag = 1
 
if flag == 1:
    print("True")
else :
    print("False")
