class Teacher:
    def __init__(self,id,name,code,d1,d2):
        self.id = "GV%02d" %(id)
        self.name = name
        self.code = code
        self.diem = d1 * 2 + d2
    def mon(self):
        x = self.code[0]
        if(x == 'A'): return "TOAN"
        if(x == 'C'): return "HOA"
        return "LY"
    def tongdiem(self):
        arr = [2.0,1.5,1.0,0.0]
        x = arr[int(self.code[1]) - 1]
        return self.diem + x
    def danhgia(self):
        if(self.tongdiem() >= 18): return "TRUNG TUYEN"
        return "LOAI"
    def __str__(self) -> str:
        return "%s %s %s %.1f %s" % (self.id,self.name,self.mon(),self.tongdiem(),self.danhgia())
    
teachers = []
for i in range(int(input())):
    teachers.append(Teacher(i+1,input().strip(),input().strip(),float(input().strip()),float(input().strip())))
    
teachers.sort(key=lambda x: -x.tongdiem())
print(*teachers,sep='\n')

