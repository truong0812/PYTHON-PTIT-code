def solove(s):
    s1 = s[::-1]
    for i in range(1,len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s1[i]) - ord(s1[i-1])): return False
    return True

for i in range(int(input())):
    if(solove(input())): print("YES")
    else: print("NO")