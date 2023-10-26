# Q 5.) Write a Python program to read last n lines of a file.


n = int(input("Enter the value: "))

with open("global_warming.txt", 'r') as filecontent: 
    lines_lst= filecontent.readlines()

    print("\nThe last",n,"lines of a given file are:\n")

    for fline in (lines_lst[-n:]):
        print(fline,"\n", end ='')