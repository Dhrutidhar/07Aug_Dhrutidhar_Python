# Q 57.) How will you randomizes the items of a list in place?


import random

list_1 = [1, 2, 3, 4, 5, 6]

i = sorted(list_1, key=lambda x: random.random())

print(i)