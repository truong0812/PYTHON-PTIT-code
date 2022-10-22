def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


n, m = map(int, input().split())
matrix = [[int(x) for x in input().split()]for i in range(n)]
maxPrime = -1
for i in range(n):
    for j in range(m):
        if isPrime(matrix[i][j]):
            maxPrime = max(maxPrime, matrix[i][j])
if maxPrime == -1:
    print("NOT FOUND")
else:
    print(maxPrime)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == maxPrime:
                print("Vi tri [%s][%s]" % (i, j))