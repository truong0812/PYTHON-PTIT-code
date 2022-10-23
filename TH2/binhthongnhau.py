MAX = int(1e5)+5
parent, sz = [i for i in range(MAX)], [1 for i in range(MAX)]


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    if sz[x] < sz[y]:
        x, y = y, x
    parent[y] = x
    sz[x] += sz[y]


if __name__ == '__main__':
    q = int(input())
    while q:
        u, v, type = map(int, input().split())
        if type == 1:
            union(u, v)
        else:
            print(1 if find(u) == find(v) else 0)
        q -= 1