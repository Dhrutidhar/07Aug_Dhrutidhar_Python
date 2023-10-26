# Q 11.) Write a Python program to write a list to a file.


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('color.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

cont = open('color.txt')
print(cont.read())
