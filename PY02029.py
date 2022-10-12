if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    data = [int(x) for x in input().split()]
    data.sort()
    count = {}
    for i in data:
        if i in count:
            count[i] += 1
        else: count[i] = 1
    a = sorted(set(count.values()), reverse = True)
    if len(a) == 1:
        print("NONE")
    else:
        a = list(a)
        for i in data:
            if count[i] == a[1]:
                print(i)
                break