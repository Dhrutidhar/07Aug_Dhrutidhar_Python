# Q 12.) Write a Python program to copy the contents of a file to another file.


with open('global_warming.txt', 'r') as f:
    line= f.read()

with open("Copy_of_global_warming.txt", 'w') as f2:
    f2.write(line)