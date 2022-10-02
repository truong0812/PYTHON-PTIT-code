def doit():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    res = "YES"
    for i in range(n):
        if a[i] > b[i] :
            res = "NO"
            break
        
    print(res)
    
for i in range( int(input()) ): doit()

