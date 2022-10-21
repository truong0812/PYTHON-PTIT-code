isPrime = [True for i in range(500005)]


def Sieve():
    isPrime[0] = isPrime[1] = False
    for i in range(2, 250005):
        if isPrime[i]:
            isPrime[2*i:500005:i] = [False for j in range(2*i, 500005, i)]


Sieve()


def Solve():
    n = int(input())
    tmp = list(map(int, input().split()))
    arr = []
    for x in tmp:
        if x not in arr:
            arr.append(x)
    cur, total = 0, sum(arr)
    for i in range(0, len(arr)-1):
        cur += arr[i]
        if isPrime[cur] and isPrime[total-cur]:
            print(i)
            return
    print("NOT FOUND")


Solve()