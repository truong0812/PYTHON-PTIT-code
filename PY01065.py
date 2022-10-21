def isMatched(target, predict):
    for i in range(len(target)):
        if target[i] != "?":
            if target[i] != predict[i]:
                return False
    return True


def Solve():
    s = input()
    if s[3] == "*" or s[3] == "/":
        print("WRONG PROBLEM!")
        return
    for i in range(10, 100):
        for j in range(10, 100):
            add = i+j
            if add < 100:
                tmp = str(i) + " + " + str(j) + " = " + str(add)
                if (isMatched(s, tmp)):
                    print(tmp)
                    return
            subtract = i-j
            if subtract >= 10:
                tmp = str(i) + " - " + str(j) + " = " + str(subtract)
                if (isMatched(s, tmp)):
                    print(tmp)
                    return
    print("WRONG PROBLEM!")


for _ in range(int(input())):
    Solve()