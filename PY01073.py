
from itertools import permutations

s = input()
kq = permutations(s)
for i in list(kq):
    print(*i,sep='')