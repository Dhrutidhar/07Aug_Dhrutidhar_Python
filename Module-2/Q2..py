# Q2.) Write a Python program to get the Factorial number of given number.

num = int(input("Enter the Number: "))

factor = 1

if num < 0:
   print("Sorry, Factorial does not exist for Negative Numbers")
elif num == 0:
   print("The Factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factor = factor*i
print("The Factorial of",num,"is",factor)
