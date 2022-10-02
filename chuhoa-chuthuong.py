s = input()
hoa = thuong = 0
for i in s:
    if(i >= 'a' and i <= 'z'): thuong += 1
    else: hoa += 1
if (thuong >= hoa): print(s.lower())
else: print (s.upper())