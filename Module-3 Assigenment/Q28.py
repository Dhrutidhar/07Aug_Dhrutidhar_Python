# Q 28.) Write a Python program to remove an empty tuple(s) from a list of tuples. 


tuple_1 = ('Dhrutidhar', '', 'Jay', '', 'Varun', '', 'Suresh', '', 'Manish')

lis = []

for i in tuple_1:
    lis.append(i)
    
    if(len(i) == 0):
        lis.remove(i)    
        
t = tuple(lis)
print(t)