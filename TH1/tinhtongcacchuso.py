def solove(str):
    s = 0
    a =[]
    for i in str:
        if( i >= '0' and i <= '9'): s += int(i)
        else: a.append(i)
    a.sort()
    for i in a:
        print(i,end = "")
    print(s)
    
for i in range(int(input())):
    solove(input())