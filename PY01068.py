l = []
res = []
def genToHop(l, n, k, vt, s, pre):
    # print(s)
    if vt == n: return
    if len(s.split()) == k:
        res.append(s)
    for i in range(pre+1, n):
        genToHop(l, n, k, vt+1, s+" "+ str(l[i]), i)
n,k = map(int, input().split())
l = list(set(input().split()))
genToHop(sorted(l, key= lambda x: x[0]), len(l), k, 0, '', -1)
res =sorted(res)
for i in res:
    print(i[1:])