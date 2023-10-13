# Q 46.) Write a Python program to combine values in python list of dictionaries. 
#        Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}] 
#        Expected Output:Counter ({'item1': 1150, 'item2': 300})


dict_1 = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

from collections import Counter

result = Counter()

for i in dict_1:
    result[i['item']] += i['amount']
print(result)