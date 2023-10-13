# Q 6.) Write a Python program to count the number of strings where the string 
#       length is 2 or more and the first and last character are same from a given 
#       list of strings.


string_list = input("Enter a list of strings: ").split()

count = 0

for string in string_list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1

print(f"The count of same first and last character is: {count}")

