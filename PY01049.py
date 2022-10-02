def ktranto(n):
    if n < 2: return False
    if n == 2 or n == 3 or n == 5 or n == 7: return True
    i = 2
    while(i * i <= n):
        if n % i == 0: return False
        i += 1
    
    
    return True

for i in range(int(input())):
    s = input()
    dem1 = 0
    dem2 = 0
    for i in s:
        if ktranto(int(i)): dem1 +=1
        else: dem2 += 1
    if(ktranto(int(len(s))) and dem1 > dem2): print("YES")
    else : print("NO")
         