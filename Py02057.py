from pickle import TRUE


n, m = map(int, input().split())
matrix = [[int(x) for x in input().split()]for i in range(n)]
minElement, maxElement = 1000000, -1
for x in matrix:
    minElement = min(minElement, min(x))
    maxElement = max(maxElement, max(x))
check = False
for i in range(n):
    for j in range(m):
        if matrix[i][j] == maxElement-minElement:
            if(not check): print(maxElement - minElement)
            print('Vi tri [%d][%d]'%(i,j))
            check = True
if(not check): print('NOT FOUND')
            

