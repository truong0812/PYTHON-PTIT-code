def ktra(str):
    pc = 0
    sl = 0
    for i in range(len(str)):
        if(i % 2 == 1): sl+= int(str[i])
        elif(pc == 0): pc = int(str[i])
        elif(pc != 0 and int(str[i]) != 0): pc *= int(str[i])
        
    print( pc,sl )
    
for i in range(int(input())):
    str = input()
    ktra(str)