# Q 5.) How will you compare two lists?

# ------------- By Sort Method -------------- #
l1 = [10, 20, 30, 40, 50]
l2 = [50, 10, 30, 20, 40]

l1.sort()
l2.sort()

if l1 == l2:
    print("Both list are same!!!")
else:
    print("List are not same!!!")

# -------------- By Sorted Method ----------- #

l3 = [5, 10, 15, 20, 25]
l4 = [15, 25, 5, 10, 20]

l1_sorted = sorted(l3)
l2_sorted = sorted(l4)

if l1_sorted == l2_sorted:
    print("Both list are same!!!")
else:
    print("List are not same!!!")

# ------------- By Set Method -------------- #
a = [1, 2, 3, 4, 5]
b = [5, 1, 4, 3, 1]

list1 = set(a)
list2 = set(b)

if list1 == list2:
    print("Both list are same!!!!")
else:
    print("List are not same!!!!")

