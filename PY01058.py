def nto(s):
    if(s < 2): return False
    if(s == 2): return True
    for i in range(2,int(s**0.5) + 1):    
        if(s % i == 0): return False
    return True

for i in range(int(input())):
    str = input()
    if(nto(int(str[-4::]))): print("YES")
    else: print("NO")