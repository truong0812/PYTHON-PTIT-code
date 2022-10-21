def doit(s):
    n = len(s)
    i = n-2
    while i >= 0 and s[i] <= s[i+1]:
        i -= 1
    if i < 0:
        return "-1"
    j, tmp = -1, "."
    for _ in range(i+1, n):
        if s[_] < s[i]:
            if s[_] > tmp:
                j, tmp = _, s[_]
    s[i], s[j] = s[j], s[i]
    res = "".join(s)
    return res if res[0] != "0" else "-1"

for i in range(int(input())):
    print(doit(list(input())))