def tongchuso(n):
    s = 0
    for i in n:
        s += int(i)
    return s

n = input()
count = 0
if n[0] == '-' : 
    n = str(tongchuso(n[1:]) - 3)
    count += 1
while( len(n) > 1):
    n = str(tongchuso(n))
    count += 1
print(count)