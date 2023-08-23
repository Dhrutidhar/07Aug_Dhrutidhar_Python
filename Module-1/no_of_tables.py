n = int(input("Enter the number that you have to print: "))
if n != 0:
    for n  in  range(n):
        m = int(input("Which Number you have to print:"))
        for o in range(1, 11):
            print(f"{m} * {o} = {m*o}")

    
else:
    print("No Number")