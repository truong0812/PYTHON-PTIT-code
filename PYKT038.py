def calculator(solve):
    solve = solve[::-1]
    count = 0
    res = ""
    val = 0
    for i in range(0, len(solve)):
        val += (2 ** count) * int(solve[i])
        count += 1
        if (i + 1) % 3 == 0 or i == len(solve) - 1:
            res += str(val)
            count = 0
            val = 0
    return res[::-1]

solve = input()
print(calculator(solve))