data = "Fruit_stock.txt"

def Manager_role():

    print(" ")
    print("\t\t\tFruit Market Manager")
    print(" ")
    print("\t\t\t1) Add fruit stock.")
    print("\t\t\t2) View fruit stock.")
    print("\t\t\t3) Update fruit stock.")
    print(" ")   

    choice = int(input("Enter the Choice You have to Perform : "))

    if choice ==1:
                print("\t\tAdd Fruit Stock:")
                fruit_name=input("Enter your fruit name : ")
                fruit_qty=int(input("Enter fruit qty (in kg.) : "))
                fruit_price=int(input("Enter fruit price : "))
                fruit_dic = {fruit_name : {'Qty': fruit_qty, 'Price': fruit_price}}    
                print(fruit_dic)


                file = open(data, 'a')
                file.write(f"{fruit_dic} \n========================\n,")


    elif choice==2:
            f = open(data, 'r')
            print(f.read())

    else:
        print("Update Feature is currently Not available!!!!")


