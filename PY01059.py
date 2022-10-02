import string


def ktra(str):
    sc = 0
    pl = 0
    for i in range(len(str)):
        if(i % 2 == 0): sc+= int(str[i])
        elif(pl == 0): pl = int(str[i])
        elif(pl != 0 and int(str[i]) != 0): pl *= int(str[i])
        
    print(sc,pl )
    
for i in range(int(input())):
    str = input()
    ktra(str)