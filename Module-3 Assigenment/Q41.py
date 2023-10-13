# Q 41.) Write a Python program to combine two dictionary adding values for common keys. 
#       d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} 
#       Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).


dict_1 = {'a' : 100, 'b' : 200, 'c' : 300}
dict_2 = {'a' : 300, 'b' : 200, 'd' : 400}

from collections import Counter

dict_3 = Counter(dict_1) + Counter(dict_2)

print(dict_3)