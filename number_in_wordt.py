single = ['','one','two','three','four','five','six','seven','eight','nine','ten']
double = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen','twenty']
tens = ['','ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']

def crore(a):
    x1 = ""
    a = str(a)
    try:
        if(len(a)==8):
            six = int(a[0])
            six = str(single[six]) +" "+"Crore"
            a = a[1: :]
            x1 = x1 + str(six)
        elif(len(a)==9):
            if(int(a[0])==1):
                gets = int(a[1])
                six = str(double[gets]) + " Crore"
                a = a[2: :]
                x1 = x1 + str(six)
            else:
                gets = int(a[0])
                gets1 = int(a[1])
                six = str(tens[gets]) + " " + str(single[gets1]) + " Crore"
                a = a[2: :]
                x1 = x1 + str(six)
    except:
        pass
    return x1

# Counting values in range of lakh
def lakh(a):
    x1 = ""
    a = str(a)
    if(int(a[0])==0 and int(a[1])==0):
            a = a[2: :]
            x1 = x1 + ""
    else:
        try:
            if(len(a)==6):
                five = int(a[0])
                five = str(single[five])+" "+"Lakh"
                a = a[1: :]
                x1 = x1 + str(five)
            elif(len(a)==7):
                if(int(a[0])==1):
                    getl = int(a[1])
                    five = str(double[getl]) + "Lakh"
                    a = a[2: :]
                    x1 = x1 + str(five)
                else:
                    getl = int(a[0])
                    getl2 = int(a[1])
                    five = str(tens[getl]) + " " + str(single[getl2]) + " " + "Lakh"
                    a = a[2: :]
                    x1 = x1 + str(five)
        except:
            pass
        
    return x1

# Counting values in range of Thousand
def thousand(a):
    x1 = ""
    a = str(a)
    if(int(a[0])==0 and int(a[1])==0):
            a = a[2: :]
            x1.append("")
    else:
            try:
                if(len(a)==4):
                    four =  int(a[0])
                    four = str(single[four]) +" "+"Thousand"
                    a = a[1: :] 
                    x1 = x1 + str(four)
                elif(len(a)==5):
                    if(int(a[0])==1):
                        gett = int(a[1])
                        four = str(double[gett]) +" "+"Thousand"
                        a = a[2: :]
                        x1 = x1 + str(four)
                    else:
                        gett = int(a[0])
                        gett1 = int(a[1])
                        four = str(tens[gett]) +" "+ str(single[gett1]) + " Thousand"
                        a = a[2: :]
                        x1 = x1 + str(four)
            except:
                pass
    
    return x1

# Counting values in range of hundred
def hundred(a):
    #a = str(input())
    x1 = ""
    a = str(a)
    if(int(a[0])==0 and int(a[1])==0 and int(a[2])==0):
        pass
    else:
        try:
            three = int(a[0])
            three = str(single[three]) +" "+ "Hundred"
            c = int(a[1])
            #x1 = x1 + str(three)
            if(c == 1):
                getv = int(a[2])
                three = str(three) +" "+ double[getv]
                x1 = x1 + str(three)
            else:
                getv = tens[c]
                three = str(three)+" "+str(getv)+" "+ single[int(a[2])]
                x1 = x1 + str(three)
        except:
            pass
    return x1

# x1 = []
# a = str(input())
# n1 = False
# x2 = []
# if("." in a):
#     n1 = True
#     b = a.index(".")
#     strg = a[b+1: :]
#     a = a[0:b:]   
#     x2.append(strg) 

# if(len(a)<=9 or len(a)>=8):
#     a = crore(a)
# if(len(a)>=6 or len(a)<=7):
#     a = lakh(a)
# if(len(a)<=5 or len(a)>=4):
#     a = thousand(a)
# if(len(a)<=3 or len(a)>=0):
#     hundred(a)

# if(n1):
#     point1 = ("Amount in Words: ",*x1)
#     points = (*x2,"/100")
#     print(*point1,*points)
# else:
#     print("Amount in words: ",*x1)
