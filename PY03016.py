from collections import defaultdict
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
cnt = defaultdict(int)
res, stk = 0, []
for i in range(n):
    while len(stk) > 0 and arr[stk[-1]] < arr[i]:
        cnt[arr[stk.pop()]] -= 1
        res += 1
    if len(stk) > 0:
        if arr[stk[-1]] == arr[i]:
            res += cnt[arr[i]] + (1 if len(stk) > cnt[arr[i]] else 0)
        else:
            res += 1
    stk.append(i)
    cnt[arr[i]] += 1
print(res)