import math
import sys


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def isTriangle(self):
        return self.x1 * (self.y2 - self.y3) + self.x2 * (self.y3 - self.y1) + self.x3 * (self.y1 - self.y2) != 0.0

    def perimeter(self):
        p1, p2, p3 = [self.x1, self.y1], [self.x2, self.y2], [self.x3, self.y3]
        return math.dist(p1, p2) + math.dist(p2, p3) + math.dist(p1, p3)

    def area(self):
        p1, p2, p3 = [self.x1, self.y1], [self.x2, self.y2], [self.x3, self.y3]
        e1, e2, e3 = math.dist(p1, p2), math.dist(p2, p3), math.dist(p1, p3)
        halfPerimeter = self.perimeter() / 2
        return math.sqrt(halfPerimeter * (halfPerimeter - e1) * (halfPerimeter - e2) * (halfPerimeter - e3))


if __name__ == "__main__":
    arr = []
    for line in sys.stdin:
        for x in line.split():
            arr.append(x)
    t = int(arr[0])
    i = 1
    while t > 0:
        x1, y1, x2, y2, x3, y3 = float(arr[i]), float(
            arr[i+1]), float(arr[i+2]), float(arr[i+3]), float(arr[i+4]), float(arr[i+5])
        tr = Triangle(x1, y1, x2, y2, x3, y3)
        if tr.isTriangle():
            print("%.2f" % (tr.area()))
        else:
            print("INVALID")
        t -= 1
        i += 6