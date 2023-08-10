def dict_laptop():
    file = open("stock.txt","r")
    dictionary = {}
    key = 0

    for line in file:
        key = key+1
        line = line.replace("\n","")
        line = line.split(",")
        dictionary[key] = line
    
    file.close()
    return  dictionary

def display_table():
    dictionary = dict_laptop()
    with open ("stock.txt","r") as files:
        print("=============================================================================================================")
        print(f"S.N {'Laptop name':<18} {'Company':<16} {'Price':<10} {'Quantity':<10} {'Processor':<15} {'Graphics':<10}")
        print("=============================================================================================================")
        for sn_num, data_dic in dictionary.items():
            sn = str(sn_num).rjust(2, ' ')
            company = data_dic[1].ljust(15)
            product = data_dic[0].ljust(18)
            price = data_dic[2].ljust(10)
            quantity = data_dic[3].ljust(10)
            Processor = data_dic[4].ljust(15)
            Graphics = data_dic[5].ljust(10)
            print(f"{sn}. {product} {company} {price} {quantity} {Processor} {Graphics}")
