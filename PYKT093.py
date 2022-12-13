from decimal import *


class Student:
    def __init__(self, orderNumber, name, p1, p2, p3):
        self.code = "SV%02d" % (orderNumber)
        self.name = name
        self.p1 = int(p1)
        self.p2 = int(p2)
        self.p3 = int(p3)

    def getAverage(self):
        res = (Decimal(self.p1)*3 + Decimal(self.p2)
               * 3 + Decimal(self.p3)*2) / 8
        return res.quantize(Decimal('1.00'), ROUND_HALF_UP)

    def getFormattedName(self):
        w = self.name.strip().lower().split()
        return " ".join(w).title()

    def print(self, rank):
        print("%s %s %s %s" %
              (self.code, self.getFormattedName(), self.getAverage(), rank))


if __name__ == "__main__":
    n = int(input())
    students = []
    for i in range(n):
        name, p1, p2, p3 = input(), input(), input(), input()
        students.append(Student(i+1, name, p1, p2, p3))
    students.sort(key=lambda x: (-x.getAverage(), x.code))
    curRank, curPoint = 1, -1
    for i in range(n):
        if students[i].getAverage() != curPoint:
            curPoint = students[i].getAverage()
            curRank = i+1
        students[i].print(curRank)