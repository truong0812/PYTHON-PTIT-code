


def solove(s,n):
    a = [int(i) for i in s.split()]
    min1 = a[0] 
    min2 = a[0]
    min3 = a[0]
    for i in range(1,n):
        if(a[i] < min1):
            min3 = min2
            min2 = min1
            min1 = a[i]
            continue
        if(a[i] < min2):
            min3 = min2
            min2 = a[i]
            continue
        if(a[i] < min3):
            min3 = a[i]
            
    return min1 + min2 + min3 

for i in range(int(input())):
    n = int(input())
    s = input()
    print(solove(s,n))
    
    