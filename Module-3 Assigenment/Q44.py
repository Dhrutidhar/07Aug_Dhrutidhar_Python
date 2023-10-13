# Q 44.) Write a Python program to create and display all combinations of letters, 
#        selecting each letter from a different key in a dictionary. 
#        Sample data: {'1': ['a','b'], '2': ['c','d']} 
#        Expected Output: ac ad bc bd 


import itertools      
dict_1 ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[dict_1[k] for k in sorted(dict_1.keys())]):
    print(''.join(combo))