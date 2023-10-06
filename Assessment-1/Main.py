from Sample_store_only_for_Manager import Manager_role
from Sample_store_only_for_Costumer import Costumer_role

Y_or_N='Y'
print("\t\t\tWelcome to your market !!!")
print("  ")
print("\t\t\t1) Manager. ") 
print("\t\t\t2) Customer. ")
print(" ")

while Y_or_N != 'N':

    main_choice =int(input(" Enter your Choice : "))
    print(" ")

    if main_choice == 1:
        Manager_role()

    else:
        print("This Feature is coming soon!!!")
        Costumer_role()
        



    Y_or_N = (input("Do you want to perform more operation: press y for yes and n for no : ")).capitalize()
    if Y_or_N == 'Y':
        print("\t\t\tWelcome to your market !!!")
        print("  ")
        print("\t\t\t1) Manager.") 
        print("\t\t\t2) Customer")
        print(" ")
    else:
        exit()



