n = int(input())
arr = list(map(int, input().split()))
mx, res = max(arr), 1
i = 0
while i < n:
    if arr[i] == mx:
        j = i
        while j < n and arr[j] == mx:
            j += 1
        res = max(res, j-i)
        i = j
    else:
        i += 1
print(res)