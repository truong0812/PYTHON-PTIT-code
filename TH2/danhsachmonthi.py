n = int(input())
m = {}
for i in range(n) :
    ma = input()
    ten = input()
    ht = input()
    m[ma] = [ten, ht]
for i in sorted(m) :
    print(i, m[i][0], m[i][1])