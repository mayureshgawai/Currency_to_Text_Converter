def conversion(num):
    single = ['','one','two','three','four','five','six','seven','eight','nine','ten']
    double = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen','twenty']
    tens = ['','ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']
    cur = ['Thousand','Lakh','Crore']
    # print(num)
    l1 = []
    l2 = ""
    strg = ""
    counter = 0
    i1 = 0
    a = str(num)
    dotop = ""
    if('.' in a):
        b = a.index('.')
        dotop = a[b+1: :] + "/100"
        a = a[0:b:]
    
    a = '0' + a[0: :] if(len(a)%2==0) else a
    for i in range(len(a),0,-1):
        if(i == len(a)-1):
            l1.append(str(a[i-2]) +str(a[i-1]) + str(a[i]))
    i1 = 0
    for j in range(len(a)-3,0,-1):
        if(i1 % 2 != 0):
            l1.append(str(a[j-1]) + str(a[j]))
        i1 += 1

    length = len(l1)
    if(len(l1[0])==3):
        geth = l1[0][0]
        if(geth == '0'):
            
            strg += " "+str(double[int(l1[0][2])])+ "," if l1[0][1]=='1' else " "+str(tens[int(l1[0][1])]) +" "+ str(single[int(l1[0][2])])+ ","
        else:
            strg += " "+str(single[int(l1[0][0])]) + " Hundred " + "and"
            strg += " "+str(double[int(l1[0][2])])+ "," if l1[0][1]=='1' else " "+str(tens[int(l1[0][1])]) +" "+ str(single[int(l1[0][2])])+ ","
        l1.pop(0)

    for k in range(0,len(l1)):
        getm = l1[0]
        strg += " "+str(double[int(l1[0][1])]) + " " + str(cur[0]) + "," if l1[0][0]=='1' else " "+str(tens[int(l1[0][0])]) + " " + str(single[int(l1[0][1])]) + " " + str(cur[0]) + ","    
        cur.pop(0)
        l1.pop(0)

    strg1 = strg.split(',')
    strg1.reverse()
    for i in strg1:
        counter += 1
        l2 = l2 + str(i)  
        if(counter > length):
            break

    return l2 + " "+dotop



def main():
    print("\n\n1 - Enter number of your amount")
    print("2 - Add a file")
    print("3 - Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        number = input("Amount: ")
        print("Converted amount: "+conversion(number))
        main()
    elif(choice == 2):
        try:
            file_name = str(input("Input Your File Name: "))

            file1 = open(file_name,'r')
            data = file1.readlines()
            data_list = []
        
            for i in data:
                i = i.split(', ')
                val = str(i[-1].split("\n")[0])
                data_list.append(float(val))

            for j in data_list:
                output = "Amount in Characters:{}\n".format(conversion(j))
                record_file = open('converted_currency.txt','a')
                record_file.write(output)
                record_file.close()
            print("File Created Successfully") 
            main()      
        except FileNotFoundError:
            print("File Name you Have Entered does not Exist!")
            main()
    if(choice == 3):
        print("Goodbye!")
        exit(0)

main()


# file_name = str(input("Input Your File Name: "))

# file1 = open(file_name,'r')
# data = file1.readlines()
# data_list = []
# # names = []

# # for name in data:
# #     name = name.split(',')
# #     names.append(name)
# # print(data_list)

# for i in data:
#     i = i.split(', ')
#     val = str(i[-1].split("\n")[0])
#     data_list.append(float(val))


# for j in data_list:
#     output = "Amount in Characters:{}\n".format(conversion(j))
#     record_file = open('converted_currency.txt','a')
#     record_file.write(output)
#     record_file.close()