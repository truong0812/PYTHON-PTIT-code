def dfs(x):
    vis[x] = True
    for i in canh[x]:
        if(not vis[i]):
            vis[i] = True
            dfs(i)

n,m,x = map(int, input().split())
canh = [[] for i in range(n + 5)]
for i in range(m):
    a,b = map(int, input().split())
    canh[a].append(b)
    canh[b].append(a)
vis = [False] * (n+5)
dfs(x)
for i in range(1,n+1):
    if( not vis[i]): print(i)
    

    
