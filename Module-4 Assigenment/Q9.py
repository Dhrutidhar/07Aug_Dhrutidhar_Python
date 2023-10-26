# Q 9.) Write a Python program to count the number of lines in a text file. 


with open('global_warming.txt', 'r') as f:
    line= len(f.readlines())
print("The Number of lines in file is: ",line)