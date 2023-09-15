# Q 3.) Write a Python program to get the Fibonacci series of given range.


a = 1  
b = 0  
print (b, a, end=" ")
for i in range(0,10):  
 c = b  
 b = a  
 a = c + b  
 print(a, end=" ")