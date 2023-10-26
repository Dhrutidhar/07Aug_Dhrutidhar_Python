# Q 4.) Write a Python program to read first n lines of a file.



n = int(input("Enter N value: "))

with open( "global_warming.txt", 'r') as filedata:

    linesList= filedata.readlines()
print("\nThe following are the first",n,"lines of a text file:\n")

for textline in (linesList[:n]):

    print(textline,"\n", end ='')

filedata.close()