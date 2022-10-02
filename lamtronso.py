def Solve():
    n = int(input())
    if n < 10:
        print(n)
        return
    digit = []
    while (n):
        digit.append(n % 10)
        n //= 10
    digit.reverse()
    add = 0
    for i in range(len(digit)-1, -1, -1):
        if (i == 0):
            digit[i] += add
        else:
            digit[i] = (digit[i]+add) % 10
            add = 1 if digit[i] >= 5 else 0
            digit[i] = 0
    print("".join(map(str, digit)))


t = int(input())
while t > 0:
    Solve()
    t-=1