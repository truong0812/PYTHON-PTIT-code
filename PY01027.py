def solove(s):
    s = s.replace('688','')
    if(len(s) == 0):
        print("YES")
        return
    s = s.replace('68','')
    if(len(s) == 0):
        print("YES")
        return
    s = s.replace('6','')
    if(len(s) == 0):
        print("YES")
        return
    print('NO')
    return
s = input()
solove(s)