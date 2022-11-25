import math
from decimal import Decimal
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self, other):
        p1 = [self.x, self.y]
        p2 = [other.x, other.y]
        return "%.4f" % (math.dist(p1,p2))
    
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1