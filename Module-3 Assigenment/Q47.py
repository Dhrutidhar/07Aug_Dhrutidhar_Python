# Q 47.) Write a Python program to create a dictionary from a string. 
#        Note: Track the count of the letters from the string. 
#        Sample string: 'w3resource' 
#        Expected output:{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}


string = 'w3resource'

dict_1 = {}

for letter in string:
    dict_1[letter] = dict_1.get(letter, 0) + 1
print(dict_1)