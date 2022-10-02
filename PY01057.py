def nto(s):
    if(s < 2): return False
    if(s == 2): return True
    for i in range(2,int(s**0.5) + 1):    
        if(s % i == 0): return False
    return True

def check(str):
    for i in range(len(str)):
        if((nto(i) and  not nto(int(str[i]) )) or ( not nto(i) and nto(int(str[i])))): return False
        
    return True

for i in range(int(input())):
    str = input()
    if(check(str)): print("YES")
    else: print("NO")