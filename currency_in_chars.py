import os
import csv

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



def conv_hindi(num):
    dic_hindi = {0:"",1:"एक",2:"दो",3:"तीन",4:"चार",5:"पांच",6:"छह",7:"सात",8:"आठ",9:"नौ",10:"दस",
    11:"ग्यारह",12:"बारह",13:"तेरह",14:"चौदह",15:"पंद्रह",16:"सोलह",17:"सत्रह",18:"अठारह",19:"उन्नीस",20:"बीस",21:"इकीस",22:"बाईस",23:"तेइस",
    24:"चौबीस",25:"पच्चीस",26:"छब्बीस",27:"सताइस",28:"अट्ठाइस",29:"उनतीस",30:"तीस",31:"इकतीस",32:"बतीस",33:"तैंतीस",34:"चौंतीस",35:"पैंतीस",36:"छतीस",
    37:"सैंतीस",38:"अड़तीस",39:"उनतालीस",40:"चालीस",41:"इकतालीस",42:"बयालीस",43:"तैतालीस",44:"चवालीस",45:"पैंतालीस",46:"छयालिस",47:"सैंतालीस",
    48:"अड़तालीस",49:"उनचास",50:"पचास",51:"इक्यावन",52:"बावन",53:"तिरपन",54:"चौवन",55:"पचपन",56:"छप्पन",57:"सतावन",58:"अठावन",59:"उनसठ",
    60:"साठ",61:"इकसठ",62:"बासठ",63:"तिरसठ",64:"चौंसठ",65:"पैंसठ",66:"छियासठ",67:"सड़सठ",68:"अड़सठ",69:"उनहतर",70:"सत्तर",71:"इकहतर",
    72:"बहतर",73:"तिहतर",74:"चौहतर",75:"पचहतर",76:"छिहतर",77:"सतहतर",78:"अठहतर",79:"उन्नासी",80:"अस्सी",81:"इक्यासी",82:"बयासी",83:"तिरासी",
    84:"चौरासी",85:"पचासी",86:"छियासी",87:"सतासी",88:"अट्ठासी",89:"नवासी",90:"नब्बे",91:"इक्यानवे",92:"बानवे",93:"तिरानवे",94:"चौरानवे",95:"पचानवे",
    96:"छियानवे",97:"सतानवे",98:"अट्ठानवे",99:"निन्यानवे",100:"एक सौ"}
    
    a = str(num)
    l1 = []
    list_hindi = ["हज़ार","लाख","करोड़"]
    strg = ""
    number = ""
    l2 = ""
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
            number += l1[0][1] + l1[0][2]
            strg += dic_hindi[int(number)]
        else:
            number += l1[0][1] + l1[0][2]
            strg += dic_hindi[int(l1[0][0])] + "सौ" +" "+ dic_hindi[int(number)] + ","
        l1.pop(0)

    for k in range(0,len(l1)):
        strg += dic_hindi[int(str(l1[0][0])+str(l1[0][1]))] +" "+str(list_hindi[0]) + ","
        list_hindi.pop(0)
        l1.pop(0)

    strg1 = strg.split(',')
    strg1.reverse()
    for i in strg1:
        l2 = l2 +" "+i 

    return l2 +" "+dotop


def conv_marathi(num):
    dic_marathi = {0:"शून्य",1:"एक",2:"दोन",3:"तीन",4:"चार",5:"पाच",6:"सहा",7:"सात",8:"आठ",9:"नऊ",10:"दहा",11:"अकरा",
    12:"बारा",13:"तेरा",14:"चौदा",15:"पंधरा",16:"सोळा",17:"सतरा",18:"अठरा",19:"एकोणीस",20:"वीस",21:"एकवीस",22:"बावीस",
    23:"तेवीस",24:"चोवीस",25:"पंचवीस",26:"सव्वीस",27:"सत्तावीस",28:"अठ्ठावीस",29:"एकोणतीस",
    30:"तीस",31:"एकतीस",32:"बत्तीस",33:"तेहेतीस",34:"चौतीस",35:"पस्तीस",36:"छत्तीस",37:"सदतीस",38:"अडतीस",39:"एकोणचाळीस",
    40:"चाळीस",41:"एक्केचाळीस",42:"बेचाळीस",43:"त्रेचाळीस",44:"चव्वेचाळीस",45:"पंचेचाळीस",46:"सेहेचाळीस",47:"सत्तेचाळीस",
    48:"अठ्ठेचाळीस",49:"एकोणपन्नास",50:"पन्नास",51:"एक्कावन्न",52:"बावन्न",53:"त्रेपन्न",54:"चोपन्न",55:"पंचावन्न",56:"छप्पन्न",57:"सत्तावन्न",
    58:"अठ्ठावन्न",59:"एकोणसाठ",60:"साठ",61:"एकसष्ठ",62:"बासष्ठ",63:"त्रेसष्ठ",64:"चौसष्ठ",65:"पासष्ठ",66:"सहासष्ठ",67:"सदुसष्ठ",68:"अडुसष्ठ",
    69:"एकोणसत्तर",70:"सत्तर",71:"एक्काहत्तर",72:"बाहत्तर",73:"त्र्याहत्तर",74:"चौर्‍याहत्तर",75:"पंच्याहत्तर",76:"शहात्तर",77:"सत्याहत्तर",78:"अठ्ठ्याहत्तर",
    79:"एकोण ऐंशी",80:"ऐंशी",81:"एक्क्याऐंशी",82:"ब्याऐंशी",83:"त्र्याऐंशी",84:"चौऱ्याऐंशी",85:"पंच्याऐंशी",
    86:"शहाऐंशी",87:"सत्त्याऐंशी",88:"अठ्ठ्याऐंशी",89:"एकोणनव्वद",90:"नव्वद",91:"एक्क्याण्णव",92:"ब्याण्णव",93:"त्र्याण्णव",
    94:"चौऱ्याण्णव",95:"पंच्याण्णव",96:"शहाण्णव",97:"सत्त्याण्णव",98:"अठ्ठ्याण्णव",99:"नव्व्याण्णव",100:"शंभर"}
    l1 = []
    list_hindi = ["हज़ार","लाख","करोड़"]
    strg = ""
    number = ""
    l2 = ""

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
            number += l1[0][1] + l1[0][2]
            strg += dic_marathi[int(number)]
        else:
            number += l1[0][1] + l1[0][2]
            strg += dic_marathi[int(l1[0][0])] + "शे" +" "+ dic_marathi[int(number)] + ","
        l1.pop(0)

    for k in range(0,len(l1)):
        strg += dic_marathi[int(str(l1[0][0])+str(l1[0][1]))] +" "+str(list_hindi[0]) + ","
        list_hindi.pop(0)
        l1.pop(0)

    strg1 = strg.split(',')
    strg1.reverse()
    for i in strg1:
        l2 = l2 +" "+i 

    return l2 +" "+dotop




def main():
    print("\n\n1 - Enter number of your amount")
    print("2 - Add a file")
    print("3 - Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        number = input("Amount: ")
        print("\n\n1 - English\n2 - Hindi\n3 - Marathi")
        lang = int(input("Select your Language: "))
        if(lang == 1):
            print("Aomunt in Characters: "+conversion(number))
        elif(lang == 2):
            print("Aomunt in Characters: "+conv_hindi(number))
        elif(lang == 3):
            print("Aomunt in Characters: "+conv_marathi(number))
        else:
            print("Invalid Choice")
        main()
    elif(choice == 2):
        try:
            file_name = str(input("Input Your File Name: "))

            file1 = open(file_name,'r')
            data = file1.readlines()
            data_list = []
            row_data = []
            file1.close()
            column = int(input("Select Column number to Process: "))-1
            print("\n\n1 - English\n2 - Hindi\n3 - Marathi")
            lang = int(input("Select your Language: "))

            for i in data:
                try:
                    i = i.split(',')        # Use try except to handle index out of range
                    val = str(i[column].split("\n")[0])
                    data_list.append(float(val))
                except:
                    val = ""
                    data_list.append(val)
                i.insert(column,val)
                i.pop(-1)
                row_data.append(i)
            print(row_data)
            c = 0
            file_name1 = file_name.split('.')[0]
            for j in data_list:
                # output = "Amount in Characters:{}\n".format(conversion(j))
                if(j == ""):
                    output = ""
                else:
                    if(lang == 1):
                        output = conversion(j)
                    elif(lang == 2):
                        output = conv_hindi(j)
                    elif(lang == 3):
                        output = conv_marathi(j)
                record_file = open(file_name1+'-converted.txt','a', encoding='utf8')
                row_data[c].insert(len(row_data[c]),output)
                string = ','.join(row_data[c])
                record_file.write(string+"\n")
                record_file.close()
                c += 1
            print("File Created Successfully") 
            main()      
        except FileNotFoundError:
            print("\nFile Name you Have Entered do not Exist!")
            main()
        except PermissionError:
            print("Can't Perform the Operation because the file is Already Opened in Another Program")
            main()
            
    if(choice == 3):
        print("Goodbye!")
        exit(0)

main()