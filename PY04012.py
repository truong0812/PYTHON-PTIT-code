class Student:
    def __init__(self,code,name,clas) :
        self.code = code
        self.name = name
        self.clas = clas
        
    def cc(self,s):
        self.point = s
    def danhgia(self):
        if(self.point <= 0): return "0 KDDK"
        return str(self.point)
    def __str__(self) :
        return "%s %s %s %s" %(self.code,self.name,self.clas,self.danhgia())
    
arr=[]
t = int(input())
for i in range(t):
    arr.append(Student(input(),input(),input()))
for i in range(t):
    ma,x = input().split()
    point = 10
    for j in arr:
        if(j.code == ma):
            for k in x:
                if(k == 'v'): point -= 2
                if(k == 'm'): point -= 1
            j.cc(point)
            break
for i in arr:
    print(i)
    

    