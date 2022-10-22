def Solve():
    n, m = map(int, input().split())
    matrix = [[int(x) for x in input().split()]for i in range(n)]
    if n == m:
        for x in matrix:
            print(*x)
        return
    if n > m:
        rowRetain = [True]*n
        rowRetain[0:2*(n-m-1)+1:2] = [False]*(n-m)
        for i in range(n):
            if rowRetain[i]:
                for j in range(m):
                    print(matrix[i][j], end=" ")
                print()
    else:
        colRetain = [True]*m
        colRetain[1:2*(m-n):2] = [False]*(m-n)
        for i in range(n):
            for j in range(m):
                if colRetain[j]:
                    print(matrix[i][j], end=" ")
            print()


Solve()