def tichchuso(n):
    s = 1
    for i in n:
        s *= int(i)
    return s

for i in range(int(input())):
    n = int(input())
    arr = input().split()
    a ={}
    for j in  arr:
        a[int(j)] = tichchuso(j)
    kq = sorted(a.items(), key = lambda x:(x[1],x[0]))
    for j in kq:
        print(j[0] , end = ' ' )
    print()