def solove(s,n):
    dem = 0
    i = s.find(n)
    while(i != -1):
        dem += 1
        i = s.find(n,i+len(n))
    return dem

for i in range(int(input())):
    print(solove(input(),input()))