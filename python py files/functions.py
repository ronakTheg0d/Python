
import datetime
#price for sell 
def dollar_renewed(dollar_sign,quantity): 
    price = float(dollar_sign.replace("$",""))
    total = price * quantity
    return total

def checking_laptop_Id(dictionary):
    success = False
    while success == False:
        try:
    
            laptop_Id = int(input("Enter the desired laptop ID: "))
            
            while laptop_Id<=0 or laptop_Id>len(dictionary):
                print("Invalid laptop ID, Please enter a valid ID")
                
                laptop_Id = int(input("Enter laptop ID: "))          

            print("\n")
            print("-------------------------------------------")
            print("      The selected laptop is available    ")
            print("-------------------------------------------")
            print("\n")

            success = True
        except ValueError:
            print("Invalid input, Please enter a valid input")

    return laptop_Id


def correct_quantity(dictionary,laptop_Id):
    success = False
    while success == False: 
        try:
            quantity = int(input("Enter the  required quantity: "))

            while quantity<=0 or quantity>int(dictionary[laptop_Id][3]):
                if quantity <=0:
                    print("Invalid input for quantity")
                else:
                    print("Quantity entered exceeds the available stock!!!")
                quantity = int(input("Enter the quantity:"))
            success = True
    
        except ValueError:
            print("Invalid input, Please input the correct data")
    
    return quantity

def quantity_validation(dict_update, laptop_ID):
    success = False
    while success == False:
        try:
            quantity = int(input("Enter the required quantity:"))
                
            while quantity<=0:
                print("Invalid input for quantity")
                
                quantity = int(input("Enter the quantity:"))
            
            success = True
        except:
            print("Invalid input, Please input the correct data")
            
    return quantity




#creating a sell invoice
def sell_bill(name,list_brand,list_laptop,total_price):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    
    
    unique = str(hour)+str(minute)+str(second)
    dateAndTime = str(year)+"/"+str(month)+"/"+str(day)+" "+str(hour)+":"+str(minute)+":"+str(second)
    # creating a sell text file
    file = open(f"{name} {unique}.txt","w")
    file.write("Name of the customer is: "+name+"\n")
    file.write("Date and Time : "+dateAndTime+"\n")
    file.write("Total Price:"+str(total_price)+"\n")


    for i in range(len(list_brand)):
        file.write(list_laptop[i]+": "+list_brand[i]+"\n")
            
    file.close()

    # printing the sell invoice in the terminal
    print("------------------------------------------------------")
    print("\t\t\t","Invoice for sell ")
    print("------------------------------------------------------")
    print("Date and Time:",dateAndTime)
    print("Name of the customer:",name)
    print("Brand Name:",list_brand)
    print("laptop Name :",list_laptop)
    print("Total cost:",total_price)
   
    
#creating a buy invoice

def buy_bill(name,list_brand,list_laptop,total_fine):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    
    unique = str(hour)+str(minute)+str(second)
    dateAndTime = str(year)+"/"+str(month)+"/"+str(day)+" "+str(hour)+":"+str(minute)+":"+str(second)
   
   #creating a buy text file
    fileName = name+unique+"-return.txt"
    file = open(fileName,"w")
    file.write("Name of customer is: "+name+"\n")
    file.write("Date and Time details: "+dateAndTime+"\n")
    
    file.write("Total price:"+str(total_fine)+"\n")

    for i in range(len(list_brand)):
        file.write(list_laptop[i]+": "+list_brand[i]+"\n")
            
    file.close()
        
    # printing the buy invoice in the terminal
    print("------------------------------------------------------")
    print("\t\t\t","Invoice for buy ")
    print("------------------------------------------------------")
    print("Date and Time:",dateAndTime)
    print("Name of the customer:",name)
    print("Brand is:",list_brand)
    print("laptop is:",list_laptop)
    print("Total price:",total_fine)

