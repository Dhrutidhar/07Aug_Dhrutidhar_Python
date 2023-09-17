# Q 11.) Write a python program to sum of the first n positive integers.


num = int(input("Enter the number of values you want to sum:"))
sum = 0

if num<1:
    print("The entered value is not a Natural number!!!!")
else:
    for i in range (num+1):
        sum += i
        
print(f"The sum is: ",sum)