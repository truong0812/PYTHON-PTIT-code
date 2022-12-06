def Solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.insert(arr.index(max(arr)), m)
    neg, pos = [], []
    for x in arr:
        if x < 0:
            neg.append(x)
        else:
            pos.append(x)
    print(" ".join(map(str, neg)), end=" ")
    print(" ".join(map(str, pos)))


if __name__ == "__main__":
    for _ in range(int(input())):
        Solve() 