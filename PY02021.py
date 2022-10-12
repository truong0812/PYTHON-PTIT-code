if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, m, k = [int(x) for x in input().split()]
        data_1 = [int(x) for x in input().split()]
        data_2 = [int(x) for x in input().split()]
        data_3 = [int(x) for x in input().split()]
        i1, i2, i3, check = 0, 0, 0, 0
        while i1 < n and i2 < m and i3 < k:
            if data_1[i1] == data_2[i2] == data_3[i3]:
                print(data_1[i1], end = " ")
                i1 += 1
                i2 += 1
                i3 += 1
                check = 1
            elif data_1[i1] < data_2[i2]: 
                i1 += 1
            elif data_2[i2] < data_3[i3]:
                i2 += 1
            else: 
                i3 += 1
        if check == 0: print("NO")
        else: print()
        t -= 1