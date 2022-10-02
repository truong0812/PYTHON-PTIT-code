def doit():
    s = str(input())
    for i in range(0,len(s)-1,2):
        for j in range(0,int(s[i+1])):
            print(s[i],end = '')
    print ()
    
for i in range(0,wint(input())):
    doit()