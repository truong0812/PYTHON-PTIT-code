if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    a = set(list(x for x in input().split()))
    b = set(list(x for x in input().split()))
    if len(a) != len(b): print("NO")
    else: 
        if(a.difference_update(b) == None):
            print("YES")
        else:
            print("NO")