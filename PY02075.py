def Solve():
    n = int(input())
    segment = []
    for i in range(n):
        segment.append(tuple(map(int, input().split())))
    segment.sort(key=lambda x: x[0])
    cnt, last = 1, segment[0][1]
    for i in range(1, n):
        if segment[i][0] >= last:
            cnt += 1
            last = segment[i][1]
        elif segment[i][1] < last:
            last = segment[i][1]
    print(cnt)


for _ in range(int(input())):
    Solve()