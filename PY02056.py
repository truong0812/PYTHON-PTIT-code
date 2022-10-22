def isPalindrome(s):
    return s == s[::-1] and len(s) >= 2


n, m = map(int, input().split())
matrix = [[int(x) for x in input().split()]for i in range(n)]
maxPalindrome = -1
for i in range(n):
    for j in range(m):
        if isPalindrome(str(matrix[i][j])):
            maxPalindrome = max(maxPalindrome, matrix[i][j])
if maxPalindrome == -1:
    print("NOT FOUND")
else:
    print(maxPalindrome)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == maxPalindrome:
                print("Vi tri [%s][%s]" % (i, j))