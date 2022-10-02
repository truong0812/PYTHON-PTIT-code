import math


def check(x):
    s = 0
    while(x>0):
        s += x%10
        x//=10
        
    if s < 2: return False
    for i in range(2,int(s**0.5) + 1):
        if s % i == 0: return False
    return True

def uocso():
    x,y = [int(i) for i in input().split()]
    if(check(math.gcd(x,y))): print ("YES")
    else: print("NO")
    
for i in range(int(input())):
    uocso()
    
