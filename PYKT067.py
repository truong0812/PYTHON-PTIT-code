kq = []
vis = [False] * 11
n = 0
def sinh(x,s):
    if(x == n): kq.append(s)
    for i in range(n,0,-1):
        if(not vis[i]):
            vis[i] =True
            sinh(x+1,s+ str(i))
            vis[i] = False
for _ in range(int(input())):
    n = int(input())
    kq.clear()
    sinh(0,'')
    print(len(kq))
    print(*kq, sep=" ") 