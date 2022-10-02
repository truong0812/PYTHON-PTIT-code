def tongchuso(n):
    s = 0 
    for i in n:
        s += int(i)
    return s

for i in range(int(input())):
    s = tongchuso(input())
    if(s % 3 == 0): print("YES")
    else: print("NO") 
        