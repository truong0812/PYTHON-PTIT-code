def ktranto(n):
    if(n < 2): return False
    i = 2
    while(i * i < n):
    
        if(n % i == 0): return False
        i +=1
    
    return True

for i in range(int(input())):
    s = input()
    if(ktranto(int(s[-4::]))): print("YES")
    else: print("NO")