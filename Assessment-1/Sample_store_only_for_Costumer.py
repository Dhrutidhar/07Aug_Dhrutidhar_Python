store = {} 

data = "Fruit_stock.txt"


def Costumer_role():

    
    print(" ")
    print("\t\t\t Costumers Market")
    print(" ")
    print("\t\t\t1.) View Product.")
    print("\t\t\t2.) Buy Fruit.")
    print("\t\t\t4.) Exit.")
    
    choice_Cus = int(input("Enter the Choice: "))

    if choice_Cus == 1:
        file = open(data, 'r')
        print(file.read())
    elif choice_Cus == 2:
        file = open(data, 'r+')
        d = (file.read())
        fruit= {}
        # product_name = input("Enter the product name you want to buy: ")
        # qty = int(input("Enter the quantity to buy: "))

        for line in d:
            (key, val) = line.split()
            fruit[(key)] = val
        

        print(fruit)
        # if product_name in d:
        #     lis = []
        #     for i in range(len(d)):
            
                # lis.append(product_name)
            # print
            # print("ok")
            # # x = []
            # for product_name, qty in d.items():
            #     x.append(i)
            # print(x)
     
    """if product_name in file:
            quantity = int(input("Enter the quantity you want to buy: "))
            if quantity in data[quantity]:

        
                total_cost = store[product_name]['price'] * quantity
                store[product_name]['stock'] -= quantity
                print(f"You bought {quantity} {product_name}(s) for ${total_cost:.2f}.")
            else:
                print("Sorry, not enough stock available.")
        else:
            print("Product not found or out of stock.")
"""
   
   
   
    # elif choice_Cus == 4:
    #     #print(f"You bought {quantity} {product_name}(s) for ${total_cost:.2f}.")
    #     exit()
