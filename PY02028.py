import math
#
def isPrime(solve):
    if solve == 1 or solve == 0: return False
    if solve == 2: return True  
    for i in range(2, int(math.sqrt(solve) + 1)):
        if solve % i == 0: return False
    return True
#
if __name__ == "__main__":
    n = int(input())
    data = [int(x) for x in input().split()]
    prime = []
    location = []
    for i in range(n):
        if isPrime(data[i]):
            prime.append(data[i])
            location.append(i)
    prime.sort(reverse = True)
    for i in range(n):
        if i in location:
            x = prime.pop()
            data[i] = x
    print(*data)