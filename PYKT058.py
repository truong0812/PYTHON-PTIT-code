kq = {}
test = []
vis = [False] * 1005

def dfs(a,b):
    global kq
    global test
    if(a == b):
        kq = kq.intersection(test)
        return
    for i in canh[a]:
        if( not vis[i]):
            test.append(i)
            vis[i] = True
            dfs(i,b)
            test.pop()
            vis[i] = False
    
for i in range(int(input())):
    n,m,u,v = map(int, input().split())
    canh = [[]for i in range(n + 5)]
    for _ in range(m):
        a,b = map(int, input().split())
        canh[a].append(b)
    kq = {i for i in range(1,n+1)}
    test.clear()
    dfs(u,v)
    print(len(kq) - 1)



