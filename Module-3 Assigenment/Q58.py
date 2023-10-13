# Q 58.) Write a Python program to read a random line from a file.


import random

def random_line(nm):

    line = open(nm).read().splitlines()
    return random.choice(line)

print(random_line('TEST.txt'))