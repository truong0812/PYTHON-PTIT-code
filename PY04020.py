class Hoadon:
    def __init__(self,code,name,slg,dongia,chietkhau):
        self.code = code
        self.name = name
        self.slg = slg
        self.dongia = dongia
        self.chietkhau = chietkhau
    def thanhtien(self):
        return self.dongia * self.slg - self.chietkhau
    def __str__(self) -> str:
        return "%s %s %s %s %s %s" % (self.code,self.name,self.slg,self.dongia,self.chietkhau,self.thanhtien())
    
bill = []
for i in range(int(input())):
    bill.append(Hoadon( input().strip(), input().strip(), int(input().strip()), int(input().strip()) ,int(input().strip())))
bill.sort(key=lambda x: -x.thanhtien())
print(*bill,sep='\n')
