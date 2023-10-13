# Q 32.) Write a Python script to sort (ascending and descending) a dictionary by value. 


my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
 
print("The Ascending Order is:") 

for i in sorted(my_dict, key = my_dict.get):
    print(i, my_dict[i])

print("The Decending Order is:")

for j in sorted(my_dict, key=my_dict.get, reverse=True):
    print(j, my_dict[j])