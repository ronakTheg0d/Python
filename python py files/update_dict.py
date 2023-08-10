

def laptop_update(dictionary):
    file = open("stock.txt","w")
    for i in dictionary.values():
        file.write(i[0]+","+i[1]+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5]))
        file.write("\n")
    file.close()
    