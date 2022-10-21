import itertools
n, k = map(int, input().split())
arr = sorted(set(input().split()))
comb = itertools.combinations(arr, k)
for x in comb:
    print(" ".join(x))