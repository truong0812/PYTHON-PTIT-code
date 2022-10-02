
def chanle():
    x = int(input())
    k1 = x%10
    s = k1
    x //= 10
    k2 = 0
    check = True
    while(x > 0):
        k2 = x%10
        if(k1 - k2 != 2 and k2 - k1 != 2 ): check = False
        x//= 10
        s += k2
        k1 = k2
        
    if(s % 10 == 0 and check): print("YES")
    else: print ("NO")
    
for i in range(int(input())):
    chanle()
    
