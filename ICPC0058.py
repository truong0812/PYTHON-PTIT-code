from collections import defaultdict
allPath, path = [], [-1]*1005
vis = [False]*1005


def DFS(adj, idx, cur, e):
    if cur == e:
        path[idx] = cur
        allPath.append(path[:idx+1])
        return
    path[idx] = cur
    for i in adj[cur]:
        if not vis[i]:
            vis[i] = True
            DFS(adj, idx+1, i, e)
            vis[i] = False


def Solve():
    allPath.clear()
    n, m, s, e = map(int, input().split())
    adj = [[]for _ in range(n+1)]
    for i in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
    vis = [False]*1005
    idx = 0
    DFS(adj, idx, s, e)
    cnt = defaultdict(int)
    res = 0
    for i in allPath:
        for x in i:
            cnt[x] += 1
    for i in range(1, n+1):
        if cnt[i] == len(allPath) and i != s and i != e:
            res += 1
    print(res)


if __name__ == '__main__':
    for _ in range(int(input())):
        Solve()