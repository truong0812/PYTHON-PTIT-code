def check(str):

    for i in range(0,len(str) - 1,2):
        if(str[i] != str[i+2]):
            return False
    return True


for i in range(int(input())):
    str = input()
    if(len(str) % 2 == 1 and str[0] != str[1] and check(str)):
        print("YES")
    else: print("NO")
