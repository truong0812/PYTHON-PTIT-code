import math
n = int(input())
l = sorted(list(int(x) for x in input().split()))

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if math.gcd(l[i], l[j]) == 1:
            print(l[i], l[j])