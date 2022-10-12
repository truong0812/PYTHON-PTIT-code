def odd(n):
    if n % 2 == 0: return False
    else: return True
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        solve = [int(x) for x in input().split()]
        res = {}
        for i in range(n):
            if solve[i] in res:
                res[solve[i]] += 1
            else: res[solve[i]] = 1
        for i in res:
            if odd(res[i]): print(i)
        t -= 1