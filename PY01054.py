def tichchuso(s):
    p = 1
    for i in s:
        if(int(i) != 0): p *= int(i)
        
    return p

for i in range(int(input())):
    print(tichchuso(input()))