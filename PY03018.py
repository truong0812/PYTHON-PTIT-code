def ngannhat(a,n,m,check):
    vt = []
    vt.append([0,0,0])
    while len(vt) == 0:
        x = vt.pop(0)
        if(check[x[0]][x[1]] = True ):
            check[x[0]][x[1]] = False
            
    

for _ in range(int(input())):
    n,m = map(int,input().split())
    check = [[True for i in range(m)] for i in range(n)]
    a = []
    for i in range(n):
        arr = map(int,input().split())
        a.append(arr)
    print(ngannhat(a,n,m,check))