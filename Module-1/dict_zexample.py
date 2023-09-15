n= int(input("Enter the student of number you have to make dictonary: "))
dic = {}
keys = ['id', 'name', 'subject']
if n > 0:
    for j in range(n):    
            st_dict1 = {}
            for i in range(len(keys)):
                v = input(f"Enter the value of '{keys[i]}' for student no {j+1}:")
                st_dic1[keys[i]] = v
            print(f"Dict of Student. {j+1}", st_dict1)
            dict[j+1] = st_dict1
    print(dic)
else:
    print("error input!!!")
        


no_of_st = int(input("Enter no. of students:")) 
main_dict = {}
keys = ['id', 'name', 'sub']
if no_of_st>0:
    for student in range(no_of_st): 
            st_dict = {}
            for value in range(len(keys)):
                v = input(f"enter the value of keys '{keys[value]}' for student no {student+1}:") 
                st_dict[keys[value]] = v
            print(f"Dict of student no. {student+1}",st_dict) 
            main_dict[student+1]=st_dict 
    print(main_dict) 
else:
    print("wrong input!!!")

        