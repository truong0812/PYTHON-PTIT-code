import math
f = "0123456789ABCDEF"
test = int(input())
for t in range(test):
    b = int(input())
    s = str(input())
    k = int(math.log(b)/math.log(2))
    x = 0
    res = ""
    if b == 2: print(s)
    else:
        if len(s)%k == 0:
            x = len(s)//k
        else: x= len(s)//k +1
        for i in range(x):
            kq = 0
            lt = 1
            for j in range(len(s)-(k*i)-1 ,max(len(s)-(k*(i+1))-1,-1),-1):
                kq = kq + int(s[j])*lt
                lt *= 2
            res+=f[kq]

        print(res[::-1]);