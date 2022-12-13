n = int(input())
c,l,vt = [],[],[]
while len(vt) < n:
    arr = map(int, input().split())
    for i in arr:
        if i % 2 == 0:
            c.append(i)
            vt.append(0)
        else:
            l.append(i)
            vt.append(1)
c.sort(reverse=True)
l.sort()
for i in vt:
    if(i == 0):
        print(c[-1], end= ' ')
        c.pop()
    else:
        print(l[-1],end = ' ')
        l.pop()