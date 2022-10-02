


def nto(s):
    if(s < 2): return False
    if(s == 2): return True
    for i in range(2,int(s**0.5) + 1):    
        if(s % i == 0): return False
    return True

def ktra(str):
    s = 0
    for i in range(len(str)):
        if(i % 2 == 0 and int(str[i]) % 2 != 0 ): return False
        if(i % 2 == 1 and int(str[i]) % 2 != 1 ): return False
        s += int(str[i])
        
    if(nto(s)): return True
    return False

for i in range(int(input())):
    str = input()
    if(ktra(str)): print("YES")
    else: print("NO")
    
2

2345678521

1212121212121212121212121