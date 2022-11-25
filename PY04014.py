import decimal

class Student:
    def __init__(self,stt,name,point) :
        self.code = "HS%02d" %(stt)
        self.name = name
        self.point = point
    def dtb(self):
        res = (self.point[0] + self.point[1]) * 2
        for i in range(2,10):
            res +=self.point[i]
        res /= 12
        return res.quantize(decimal.Decimal('0.1'),decimal.ROUND_HALF_UP)
    def xeploai(self):
        p = self.dtb()
        if p >= 9:
            return "XUAT SAC"
        if p >= 8:
            return "GIOI"
        if p >= 7:
            return "KHA"
        if p >= 5:
            return "TB"
        return "YEU"
    def __str__(self) :
        return "%s %s %s %s " %(self.code,self.name,self.dtb(),self.xeploai())

arr = []
for i in range(int(input())):
    arr.append(Student(i+1,input(),[decimal.Decimal(x) for x in input().split()]))
arr.sort(key=lambda x:(-x.dtb(),x.code))
for x in arr:
    print(x)
