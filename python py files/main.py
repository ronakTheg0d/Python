#Importing files
import laptop_read
import messages
import update_dict
import functions

#prints the welcome message  
messages.welcome_message()

#displays the given choices
choice = True
while choice == True:
   #displays choices
    messages.choices()
    a = False
    while a == False:
        try:
            # taking an input
            choice = int(input("Enter a choice: "))
            a = True
        except ValueError:
            print("Invalid input, Please choose among the given choices.")

    #choice to sell a laptop
    if choice == 1:
        messages.choice_one()
        laptop_read.display_table()
        dict_update = laptop_read.dict_laptop()
       
        laptop_Id = functions.checking_laptop_Id(dict_update)
    #creating list
        laptop_list = []
        laptop_brand = []

        if int(dict_update[laptop_Id][3])>0: #checking if the input item is >0
            quantity = functions.correct_quantity(dict_update,laptop_Id) # validating quantity
            dict_update[laptop_Id][3]= int(dict_update[laptop_Id][3]) - quantity #updating dict

            update_dict.laptop_update(dict_update)              
       
           # adding value to the list
            laptop_list.append(dict_update[laptop_Id][0]) 
            laptop_brand.append(dict_update[laptop_Id][1])
           
            totalPrice = functions.dollar_renewed(dict_update[laptop_Id][2],quantity)

            while(True):
                name = input("Enter the name of the seller: ")
                if 1==1: #checking if the entered value only consists of alphabet
                    break
                print("Invalid input. Please input alphabets only.")

            print("\n Do you want to sell more laptops?")
            Loop = input("Type ""yes"" if you want to else type ""no"":")
            
            Loop_extension = True
            while Loop_extension == True:
               
                if Loop.lower() == "yes":
                    print()
                    laptop_read.display_table()
       
                    laptop_Id = functions.checking_laptop_Id(dict_update)
                    if int(dict_update[laptop_Id][3])>0:
                        quantity = functions.correct_quantity(dict_update,laptop_Id)
                        dict_update[laptop_Id][3]= int(dict_update[laptop_Id][3]) - quantity

                        update_dict.laptop_update(dict_update)

                        
                        for i in laptop_list:

                            if i != dict_update[laptop_Id][0]:
                                laptop_list.append(dict_update[laptop_Id][0])
                        for  j in laptop_brand: 
                            if j != dict_update[laptop_Id][1]:
                                laptop_brand.append(dict_update[laptop_Id][1])
           
                        updateSum = functions.dollar_renewed(dict_update[laptop_Id][2],quantity)

                        totalPrice = totalPrice + updateSum
                       
                        print("\nDo you want to sell another laptop?")
                        Loop = input("Type ""yes"" if you want to else type ""no"": ")

                        Loop_extension = True
                    else:
                         print(" laptop is not cursellly available ")
                         print("\n Do you want to sell another laptop?")
                         Loop = input("Type ""yes"" if you want to else type ""no"":")
                         Loop_extension = True
                         
                else:
                    Loop_extension = False
           
            functions.sell_bill(name,laptop_brand,laptop_list,totalPrice)
               
                     

    #choice to buy a laptop        
    elif choice == 2:
        messages.choice_two()
        laptop_read.display_table()
        dict_update = laptop_read.dict_laptop()
       
        laptop_Id = functions.checking_laptop_Id(dict_update)
    #creating list
        laptop_list = []
        laptop_brand = []

        if int(dict_update[laptop_Id][3])>=0: #checking if the input item is >0
            quantity = functions.quantity_validation(dict_update,laptop_Id) # validating quantity
            dict_update[laptop_Id][3]= int(dict_update[laptop_Id][3]) + quantity #updating dict

            update_dict.laptop_update(dict_update)              
       
           # adding value to the list
            laptop_list.append(dict_update[laptop_Id][0]) 
            laptop_brand.append(dict_update[laptop_Id][1])
           
            totalPrice = functions.dollar_renewed(dict_update[laptop_Id][2],quantity)

            while(True):
                name = input("Enter the name of the buyer: ")
                if 1==1: #checking if the entered value only consists of alphabet
                    break
                print("Invalid input. Please input alphabets only.")

            print("\n Do you want to buy more laptops?")
            Loop = input("Type ""yes"" if you want to else type ""no"":")
            
            Loop_extension = True
            while Loop_extension == True:
               
                if Loop.lower() == "yes":
                    print()
                    laptop_read.display_table()
       
                    laptop_Id = functions.checking_laptop_Id(dict_update)
                    if int(dict_update[laptop_Id][3])>=0:
                        quantity = functions.quantity_validation(dict_update,laptop_Id)
                        dict_update[laptop_Id][3]= int(dict_update[laptop_Id][3]) + quantity

                        update_dict.laptop_update(dict_update)

                        
                        for i in laptop_list:

                            if i != dict_update[laptop_Id][0]:
                                laptop_list.append(dict_update[laptop_Id][0])
                        for  j in laptop_brand: 
                            if j != dict_update[laptop_Id][1]:
                                laptop_brand.append(dict_update[laptop_Id][1])
           
                        updateSum = functions.dollar_renewed(dict_update[laptop_Id][2],quantity)

                        totalPrice = totalPrice + updateSum
                       
                        print("\nDo you want to buy another laptop?")
                        Loop = input("Type ""yes"" if you want to else type ""no"": ")

                        Loop_extension = True
                    else:
                         print(" laptop is not cursellly available ")
                         print("\n Do you want to buy another laptop?")
                         Loop = input("Type ""yes"" if you want to else type ""no"":")
                         Loop_extension = True
                         
                else:
                    Loop_extension = False
           
            functions.buy_bill(name,laptop_brand,laptop_list,totalPrice)
            choice = True
        else:
             print("laptop is not available")

    
    elif choice == 3:
        messages.choice_three()
        choice = False

    else: 
        messages.invalid()
        choice = True


