n = int(input())
tmp = []
for i in range(n):
    a = [int(i) for i in input().split()]
    tmp.append(a)
k = int(input())
sum1 = 0
sum2 = 0
for i in range(n):
    for j in range(n):
        if j < n - 1 - i: sum1 += tmp[i][j]
        elif n - 1 - i < j: sum2 += tmp[i][j]
if(abs(sum1 - sum2) <= k): print("YES")
else: print('NO')
print(abs(sum1 - sum2))
