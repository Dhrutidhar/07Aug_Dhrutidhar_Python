# Q 2.) Write a Python program to read an entire text file.


'''with open('global_warming.txt', 'r') as f:
    print(f.read())'''

def file_read(name):
        txt = open(name)
        print(txt.read())

file_read('global_warming.txt')