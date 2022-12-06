for i in range (int(input())):
    s = input()
    idx,res,stk = 1,'',[]
    for x in s:
        if x == '(':
            res += str(idx) + ' '
            stk.append(idx)
            idx+=1
        if x == ')':
            res += str(stk.pop()) + ' '
    print(res)
    
