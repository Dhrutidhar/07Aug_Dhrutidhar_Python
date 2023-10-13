# q 49.) Write a Python function to check whether a number is in a given range.


def range():
    i = int(input("Enter the Number in range 1 to 10:"))
    if i > 11 or i < 0:
        print("Not in Valid range")
    else:
        print(f"The Input {i} is in Valid range")
range()