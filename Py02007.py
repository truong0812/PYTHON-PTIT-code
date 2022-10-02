r = []
count = 0
x = 0
while (x < 10):
    a = list(int(i) for i in input().split())
    x += len(a)
    for i in a:
        so = int(i) % 42
        if (so in r) == False:
            r.append(so)
print(len(r))