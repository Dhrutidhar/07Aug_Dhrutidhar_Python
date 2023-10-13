# Q 33.)  Write a Python script to concatenate following dictionaries to create a new one.


dict_1 = {10: 100, 20: 200}
dict_2 = {30: 300, 40: 400}
dict_3 = {50: 500, 60: 600}
dict_4 = {70: 700, 80: 800}
dict_5 = {90: 900, 100: 1000}

dicti = {}

for dic in (dict_1,dict_2,dict_3,dict_4,dict_5): 
    dicti.update(dic)
print(dicti)