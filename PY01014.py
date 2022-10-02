s = input()
a,k,n = [int(i) for i in s.split()]
x = a // k
b = (x+1)*k -a
check = False
while(a + b <= n):
    print(b, end = " " )
    b += k
    check = True
if(check): print()
else: print("-1")
