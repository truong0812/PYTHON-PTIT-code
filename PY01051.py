def tongchuso(n):
    s = 0
    for i in n:
        s += int(i)

    return str(s)

for i in range(int(input())):
    s = tongchuso(input())
    if len(s) > 1 and s == s[::-1]: print("YES")
    else: print("NO")
        

