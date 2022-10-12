if __name__ == "__main__":
    m, n = [int(x) for x in input().split()]
    solve_1 = set(list(int(x) for x in input().split()))
    solve_2 = set(list(int(x) for x in input().split()))
    res_1 = list(solve_1.intersection(solve_2))
    res_1.sort()
    res_2 = list(solve_1.difference(solve_2))
    res_2.sort()
    res_3 = list(solve_2.difference(solve_1))
    res_3.sort()
    print(" ".join(str(x) for x in res_1))
    print(" ".join(str(x) for x in res_2))
    print(" ".join(str(x) for x in res_3))