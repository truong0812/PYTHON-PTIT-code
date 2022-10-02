from tokenize import Double
import math

def laisuat():
    
    n,x,m = [float(i) for i in input().split()]
    year = math.log(m/n,1+x/100)
    if(year == int(year)): print(year)
    else: print(int(year) + 1)
    
for i in range(int(input())):
    laisuat()
    
