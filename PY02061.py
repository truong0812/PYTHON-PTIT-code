def Calc(imgMatrix, kernel, r, c):
    ans = 0
    for i in range(3):
        for j in range(3):
            ans += imgMatrix[r+i][c+j]*kernel[i][j]
    return ans


def Solve():
    n, m = map(int, input().split())
    imgMatrix = [[int(x) for x in input().split()]for y in range(n)]
    kernel = [[int(x) for x in input().split()]for y in range(3)]
    res = 0
    for i in range(n-2):
        for j in range(m-2):
            res += Calc(imgMatrix, kernel, i, j)
    print(res)


for i in range(int(input())):
    Solve()