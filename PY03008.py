n = int(input())
adj = [[]for i in range(n+1)]
for i in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
cnt = 0
for i in range(1, n+1):
    cnt += 1 if len(adj[i]) > 1 else 0
print("Yes" if cnt == 1 else "No")