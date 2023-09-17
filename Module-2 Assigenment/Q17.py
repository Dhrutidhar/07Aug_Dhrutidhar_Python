# Q 17.) Write a Python program to get a single string from two given strings, 
#        separated by a space and swap the first two characters of each string.

str1 = input("Enter the one word: ")
str2 = input("Enter the second word: ")
print("String before swaping is: ",str1 +" " +str2 )
swapped_string1 = str2[:2] + str1[2:]
swapped_string2 = str1[:2] + str2[2:]
    
result_string = swapped_string1 + ' ' + swapped_string2
    
print("Result after swaping 2 character of String:", result_string)




