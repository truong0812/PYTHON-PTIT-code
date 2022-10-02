from queue import Queue


def isPalindrome(str):
    return str == str[::-1]


def Solve():
    digit = ["0", "2", "4", "6", "8"]
    n = int(input())
    q = Queue()
    for i in range(1, 5):
        q.put(digit[i])
    ans = []
    while (not q.empty()):
        number = q.get()
        if int(number) < n and isPalindrome(number) and len(number) % 2 == 0:
            ans.append(number)
        if int(number) > n:
            break
        for x in digit:
            q.put(number+x)
    print(" ".join(ans))


for i in range(0, int(input())):
    Solve()