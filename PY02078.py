def Solve():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(tuple(map(float, input().split())))
    dp = [-1]*n
    for i in range(n):
        dp[i] = 1
        for j in range(i-1, -1, -1):
            if arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]:
                dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))


for _ in range(int(input())):
    Solve()