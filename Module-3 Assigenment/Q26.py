# Q 26.) Write a Python program to replace last value of tuples in a list. 



list_tuples = [(1, 2), (3, 4), (5, 6)]

replace = 9

print([t[:-1] + (replace,) for t in list_tuples])