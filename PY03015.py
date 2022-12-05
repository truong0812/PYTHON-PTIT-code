n = 0
vis = []
canh = []
def dfs(i,x):
    vis[i] = True
    for j in canh[i]:
        if(not vis[j] and j != x):
            dfs(j,x)
def slglienthong(x):
    dem = 0
    for i in range(1,n):
        if(i != x and not vis[i]):
            dem+=1
            dfs(i,x)
    return dem

for _ in range(int(input())):
    n,m = map(int,input().split())
    vis = [False] * (n + 5)
    canh = [[] for i in range(n+5)]
    for x in range(m):
        a,b = map(int,input().split())
        canh[a].append(b)
        canh[b].append(a)
    kq = 0
    test = slglienthong(0)
    for x in range(1,n+1):
        vis = [False] * (n + 5)
        res = slglienthong(x)
        if(res > test): 
            test = res
            kq =x
    print(kq)   
    

