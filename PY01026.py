t = int(input())
for i in range(1, t + 1):
        a = ''.join(sorted(input()))
        b = ''.join(sorted(input()))
        if a == b: print(f"Test {i}: YES")
        else: print(f"Test {i}: NO")