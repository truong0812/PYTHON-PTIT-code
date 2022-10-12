if __name__ == "__main__":
    n = int(input())
    a = []
    while len(a) < n: 
        a.append(int(i) for i in input().split())
    c = []
    l = []
    for i in a:
        if(i % 2 == 0): c.append(i)
        else: l.append(i)
    c.sort()
    l.sort()
    i = 0
    j = len(l) - 1
    for x in a:
        if(x % 2 == 0): 
            print(c[i], end = ' ')
            i+=1
        else: 
            print(l[j],end = ' ')
            j-=1
    print()