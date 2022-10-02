def solove(s):
    if s[-3::] != ".py" : return False
    for i in range(len(s) - 3):
        if not (s[i] >= 'a' and s[i] <= 'z') and s[i] != '.' and s[i] != '_' : return False
    return True
s = input()
s = s.lower()
if(len(s) >= 3 and solove(s)): print("yes")
else: print("no")