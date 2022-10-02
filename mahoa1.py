def doit():
    s = input()
    dem = 1
    res = ''
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            dem+=1
        else:
            res += (str(dem) + s[i])
            dem = 1
    res += str(dem) + s[len(s) - 1] ;       
    print(res)
    
for i in range( int(input()) ): doit()

 