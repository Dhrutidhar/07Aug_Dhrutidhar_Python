# Q 13.) Write a Python program to count the number of characters (character frequency) in a string.



input_string = input("Enter a string: ")

cha = {}

for char in input_string:
    if char in cha:
        cha[char] += 1
    else:
        cha[char] = 1

print("Character frequency in the string is :")
for char, frequency in cha.items():
    print(f"'{char}': {frequency}")
