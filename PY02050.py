for i in range (int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    kq = []
    for j in range(n):
        while len(kq) > 0 and a[j] >= a[kq[-1]]: kq.pop()
        if len(kq) == 0: print(j+1, end = ' ')
        else: print(j - kq[-1], end= ' ')
        kq.append(j)
    print()
    
    