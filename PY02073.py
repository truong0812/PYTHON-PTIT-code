def Solve():
    n = int(input())
    x, y, z = map(int, input().split())
    dp = [0]*(n+1)
    dp[1] = x
    for i in range(2, n+1):
        dp[i] = min(dp[i - 1] + x, dp[(i + 1) // 2] + z + y) if i & 1 else min(dp[i - 1] + x, dp[i // 2] + z)
    print(dp[n])


for _ in range(int(input())):
    Solve()