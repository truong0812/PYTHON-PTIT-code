t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    dem = 0
    for i in range(0, n-2):
        x = a[i]
        l = i+1
        r = len(a)-1
        while(l<r):
            if(x + a[l] + a[r] == 0):
                dem=dem+1; l=l+1;
            elif x + a[l] + a[r] < 0:
                l=l+1
            else: r=r-1
    print(dem)