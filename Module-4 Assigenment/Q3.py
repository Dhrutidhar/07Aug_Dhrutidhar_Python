# Q 3.) Write a Python program to append text to a file and display the text. 


'''with open('global_warming.txt', 'a') as f:
    print(f.write("\nThis is python\n"))
'''
def file_read(name):
        from itertools import islice
        with open(name, "a") as myfile:
                myfile.write("\nThis is Dhrutidhar Kotadiya\n")
                myfile.write("Using Python..")
        txt = open(name)
        print(txt.read())
file_read('global_warming.txt')