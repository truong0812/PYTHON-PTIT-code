x = input()
if len(x) == 1: print(x)
else:
    while(len(x) != 1):
        x = str(int(x[:len(x)//2]) + int(x[len(x)//2:]))
        print(x)
    