n = int(input())
a = [int(i) for i in input().split()]
st: int = []
st.append(a[0])
for i in range(1,n):
    if len(st) > 0 and (st[len(st)-1] + a[i]) %2 == 0:
        st.pop()
    else: st.append(a[i])

print(len(st))