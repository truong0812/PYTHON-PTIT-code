n = int(input())
a = [0] * 2000000
for i in range(2,2000):
    for j in range(i*i,2000000,i):
        if(a[j] == 0): a[j] = i
        
for i in range(1,2000000):
    if(a[i] == 0): a[i] = i
    
sum = 0
for i in  range(n):
    x = int(input())
    while(x!=1 and a[x] != 0):
        sum += a[x]
        x = x//a[x]
        
print(sum)