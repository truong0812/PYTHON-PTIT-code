t = int(input())
for j in range (0,t):
    s:str = input()
    kq = 10 ** 20
    x = ""
    for i  in range(len(s)):
        if (s[i] >= '0') and (s[i] <= '9'):
            x+=s[i]
        elif x != "":
            kq = min(kq,int(x))
            x=""
    print(kq)
