def nto(s):
    if(s < 2): return False
    if(s == 2): return True
    for i in range(2,int(s**0.5) + 1):    
        if(s % i == 0): return False
    return True

def check(str):
    if(not nto(len(str))): return False
    dem = 0
    for i in range(len(str)):
        if(nto(int(str[i]))): dem +=1
        else: dem -= 1
    if(dem < 0): return False
    return True

for i in range(int(input())):
    str = input()
    if(check(str)): print("YES")
    else: print ("NO") 