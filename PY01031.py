data = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def doicoso(n,b):
    res = []
    while n > 0:
        res.append(data[n % b])
        n //= b
    return ''.join(res[::-1])
for i in range(int(input())):
    n, k = [int(x) for x in input().split()]
    print(doicoso(n, k))
    
        