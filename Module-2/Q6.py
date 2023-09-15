# Q 6.) Write python program that swap two number with temp variable and without temp variable.


#-----------Swapping with a Temporary Variable:-------------------
a = 5
b = 10

temp = a
a = b
b = temp

print("After swapping with a temp variable:")
print("A =", a)
print("B =", b)

#---------------Swapping without a Temporary Variable:------------------
a = 15
b = 20

a = a + b
b = a - b
a = a - b

print("After swapping without a temp variable:")
print("A =", a)
print("B =", b)
