def tongchuso(n):
    s = 0
    for i in n:
        s += int(i)

    return s

def ktranto(s):
    if(s < 2): return False
    i = 2
    while(i * i <= s):
        if(s % i == 0) : return False
        i +=1
    return True

for i in range(int(input())):
    s = tongchuso(input())
    if(ktranto(s)): print("YES")
    else: print("NO")
    
        

