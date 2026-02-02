st=input("enter your text :")
data=""
for i in st:
    if i=="a" or i=="A":
        data+='4'
    elif  i=="b" or i=='B':
        data+="8"
    elif  i=="c" or i=='C':
        data+="G"
    elif  i=="d" or i=='D':
        data+="B"
    elif  i=="e" or i=='E':
        data+="3"
    elif  i=="f" or i=='F':
        data+="P"
    elif  i=="g" or i=='G':
        data+="C"
    elif  i=="h" or i=='H':
        data+="I"
    elif  i=="i" or i=='I':
        data+="1"
    elif  i=="j" or i=='J':
        data+="2"
    elif  i=="k" or i=='K':
        data+=i
    elif  i=="l" or i=='L':
        data+=i
    elif  i=="m" or i=='M':
        data+="W"
    elif  i=="n" or i=='N':
        data+="Z"
    elif  i=="o" or i=='O':
        data+="0"
    elif  i=="p" or i=='P':
        data+="9"
    elif  i=="q" or i=='Q':
        data+=i
    elif  i=="r" or i=='R':
        data+=i
    elif  i=="s" or i=='S':
        data+="5"
    elif  i=="t" or i=='T':
        data+="7"
    elif  i=="u" or i=='U':
        data+="n"
    elif  i=="v" or i=='V':
        data+="A"
    elif  i=="w" or i=='W':
        data+="M"
    elif  i=="x" or i=='X':
        data+=i
    elif  i=="y" or i=='Y':
        data+="h"
    elif  i=="z" or i=='Z':
        data+="N"
    else:
        data+=i
print()
print(data)
