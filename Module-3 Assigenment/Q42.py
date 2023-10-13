# Q 42.) Write a Python program to print all unique values in a dictionary.


dic_list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

print("The original dictionary is : " ,dic_list)

result = set( value for dic in dic_list for value in dic.values())

print("The unique values is : " , result) 