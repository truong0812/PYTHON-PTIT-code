if __name__ == "__main__":
    n = int(input())
    solve = [int(x) for x in input().split()]
    step, num = sum(abs(x - solve[0]) for x in solve), solve[0]
    for i in solve:
        if i != num:
            k = sum(abs(x - i) for x in solve)
            if step > k:
                step = k
                num = i
    print(step, num)
    
    