import math
n, k = map(int, input().split())
start, end = pow(10, k-1), pow(10, k)
res = []
for i in range(start, end):
    if (math.gcd(n, i) == 1):
        res.append(i)
for i in range(0, len(res)):
    print(res[i], end="")
    print("\n" if (i+1) % 10 == 0 else " ", end="")