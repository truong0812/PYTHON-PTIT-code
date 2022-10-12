if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0: break
        data = []
        while n > 0:
            data.append(int(input()))
            n -= 1
        k = list(dict.fromkeys(data))
        k.sort()
        if len(k) == 1:
            print("BANG NHAU")
        else: 
            print(f"{k[0]} {k[len(k) - 1]}") 