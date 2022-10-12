if __name__ == "__main__":
    t = int(input())
    data = []
    while t > 0:
        solve = input()
        x = ""
        for i in range(len(solve)):
            if solve[i] >= "0" and solve[i] <= "9":
                x += solve[i]
            else: continue
            if i + 1 == len(solve) or solve[i + 1] < "0" or solve[i + 1] > "9":
                data.append(int(x))
                x = ""
        t -= 1
    data.sort()
    for i in data: print(i)