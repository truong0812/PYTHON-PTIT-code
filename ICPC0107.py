t = int(input())
for k in range(t):
    m,n = [x for x in input().split()]
    a = input().strip()
    if(a.count(" ")):
        a,b = a.split()
    else:
        b = input()

    p = min(m,n)
    q = max(m,n)
    sumMin = int(a.replace(q,p)) + int(b.replace(q,p))
    sumMax = int(a.replace(p,q)) + int(b.replace(p,q))
    print(sumMin,end=" ")
    print(sumMax)

