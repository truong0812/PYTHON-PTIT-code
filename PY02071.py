ans = []
tmp = [0]*15


def Try(k, start, sum, n):
    if sum > n:
        return
    for i in range(start, 0, -1):
        tmp[k] = i
        newSum = sum+i
        if newSum == n:
            ans.append(tmp[0:k+1:1])
        Try(k + 1, i, newSum, n)


def Solve():
    ans.clear()
    n = int(input())
    Try(0, n, 0, n)
    print(len(ans))
    for x in ans:
        print("(%s)" % (" ".join(map(str, x))), end=" ")
    print()


for _ in range(int(input())):
    Solve()