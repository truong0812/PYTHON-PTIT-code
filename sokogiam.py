def sokogiam():
    x = input()
    for i in range(0,len(x) - 1):
        if x[i] > x[i+1]: return False
    return True

for i in range(0, int(input())):
    if(sokogiam()): print("YES")
    else: print("NO")
    
