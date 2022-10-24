import re
from collections import defaultdict
from functools import cmp_to_key


def compare(x, y):
    if x[1] != y[1]:
        return y[1]-x[1]
    if x[0] > y[0]:
        return 1
    return -1


n, k = map(int, input().split())
cnt = defaultdict(int)
for i in range(n):
    arr = re.split(r'\W', input().lower())
    for word in arr:
        if len(word) > 0:
            cnt[word] += 1
nmc = list(cnt.items())
nmc.sort(key=cmp_to_key(compare))
for x in nmc:
    if x[1] >= k:
        print(x[0], x[1])