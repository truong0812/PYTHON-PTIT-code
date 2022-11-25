class Matrix:
    def __init__(self, r, c, mat):
        self.r = r
        self.c = c
        self.mat = mat

    def printMatrix(self):
        for x in self.mat:
            print(*x)

    def mul(self, other):
        res = Matrix(self.r, other.c, [
            [0 for i in range(other.c)] for j in range(self.r)])
        for i in range(res.r):
            for j in range(res.c):
                for k in range(self.c):
                    res.mat[i][j] += self.mat[i][k] * other.mat[k][j]
        return res

    def tranposition(self):
        trans = Matrix(self.c, self.r, [
            [0 for i in range(self.r)] for j in range(self.c)])
        for i in range(self.r):
            for j in range(self.c):
                trans.mat[j][i] = self.mat[i][j]
        return trans


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, m = map(int, input().split())
        matrix = Matrix(n, m, [[int(x) for x in input().split()]
                     for i in range(n)])
        res = matrix.mul(matrix.tranposition())
        res.printMatrix()
        t -= 1