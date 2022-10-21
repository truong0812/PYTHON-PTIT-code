def Solve():
    n = int(input())
    matrix = [[int(x) for x in input().split()]for i in range(n)]
    if n == 2:
        print(1, matrix[0][1]-1)
        return
    sumOfArr, tmp = 0, 0
    for i in range(n):
        for j in range(i+1, n):
            sumOfArr += matrix[i][j]
        if i == 0:
            tmp = sumOfArr
    sumOfArr //= (n-1)
    arr0 = (tmp-sumOfArr)//(n-2)
    print(arr0, end=" ")
    for i in range(1, n):
        print(matrix[i][0]-arr0, end=" ")


Solve()