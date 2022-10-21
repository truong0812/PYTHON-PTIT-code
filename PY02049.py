def Solve():
    n, p = map(int, input().split())
    res = 0
    while n:
        n //= p
        res += n
    print(res)


for i in range(int(input())):
    Solve()