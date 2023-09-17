    # Q 18.) Write a Python program to add 'ing' at the end of a given string (length 
    #       should be at least 3). If the given string already ends with 'ing' then add 
    #       'ly' instead if the string length of the given string is less than 3, leave it unchanged.


str = input("Enter word of Minimum length 3:")

if len(str)>=3:
    if str.endswith('ing'):
        result = str + 'ly'
    else:
        result = str + 'ing'
    print(result)
else:
    print("Minimum length of string is not present!!!")

