if __name__ == "__main__":
    solve = input()
    n = len(solve)
    res = set()
    if n % 2 != 0: n -= 1
    for i in range(0, n, 2):
        res.add(int(solve[i:i + 2]))
    res = list(res)
    res.sort()
    print(*res)