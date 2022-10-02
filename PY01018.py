p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while(True):
    k = input()
    if(k == "0"): break
    s = [i  for i in k.split()]
    res = ''
    s[0] = int(s[0])
    for i in s[1]:
        res += p[(p.find(i) + s[0])%28]
    res = res[::-1]
    print(res)

    
    