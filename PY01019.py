def Solve():
    str = input()
    rev = str[::-1]
    for i in range(1, len(str)):
        if abs(ord(str[i])-ord(str[i-1])) != abs(ord(rev[i])-ord(rev[i-1])):
            print("NO")
            return
    print("YES")


for i in range(0, int(input())):
    Solve()