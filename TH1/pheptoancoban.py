def check(s):
    n1 = int(s[0:2])
    n2 = int(s[5:7])
    ans = 0
    if(s[3] == '+'):
        ans = n1 + n2
    elif s[3] == '-':
        ans = n1 - n2
    tmp = str(ans)
    return tmp == s[10:12]


def Try(s,pos,n,a):
    if(pos == n):
        if(check(s)):
            a.append(s)
        return
    if(s[pos] != '?'):
        Try(s,pos+1,n,a)
        return
    if(pos == 3):
        for i in ['+','-']:
            str = s[:pos] + i + s[pos:]
            Try(str,pos+1,n,a)
    elif pos == 0 or pos == 5 or pos == 10:
        for i in '123456789':
            str = s[:pos] + i + s[pos:]
            Try(str,pos+1,n,a)
    else:
        for i in '0123456789':
            str = s[:pos] + i + s[pos:]
            Try(str,pos+1,n,a)  
def solove():
    a = []
    s = input()
    n = len(s)
    if(s[3] == '*' or s[3] == '/'):
        print("WRONG PROBLEM!")
        return
    Try(s, 0,n,a)
    if(len(a) == 0):
        print("WRONG PROBLEM!")
    else:
        sorted(a)
        print(a[0])
        
for i in range(int(input())):
    solove()