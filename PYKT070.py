from datetime import datetime

class Monthi:
    def __init__(self,ma,ten,hinhthuc) -> None:
        self.ma = ma
        self.ten = ten
        self.hinhthuc = hinhthuc
        
        
class Cathi:
    def __init__(self,id,ngay,gio,phong) -> None:
        self.id = "C%03d" %(id)
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
        self.time = datetime.strptime('%d/%m/%Y %H:%M', self.ngay + ' ' + self.gio)
        
class Lichthi:
    def __init__(self,monthi,cathi,nhom,slg) -> None:
        self.monthi = monthi
        self.cathi = cathi
        self.nhom = nhom
        self.slg = slg
    def __str__(self) -> str:
        return '%s %s %s %s %s %s' %(self.cathi.ngay, self.cathi.gio, self.cathi.phong, self.monthi.ten, self.nhom, self.slg)

mon = []
ca = []
thi = []

f = open('MONTHI.in', 'r')
for i in range(int(f.readline())):
    ma = f.readline().strip()
    ten = f.readline().strip()
    hinhthuc = f.readline().strip()
    mon.append(Monthi(ma,ten,hinhthuc))

f = open('CATHI.in','r')
for i in range(int(f.readline())):
    ngay = f.readline().strip()
    gio = f.readline().strip()
    phong = f.readline().strip()
    ca.append(Cathi(i+1,ngay,gio,phong))
    
f = open('LICHTHI.in','r')
for i in range(int(f.readline())):
    arr = f.readline().strip().split()
    monthi 
    cathi
    for j in mon:
        if(arr[1] is j.ma): 
            monthi = j
            break
    for j in ca:
        if(arr[0] is j.id):
            cathi = j
            break
    thi.append(Lichthi(monthi,cathi,arr[2],arr[3]))
thi.sort(key= lambda x: (x.cathi.time,x.cathi.id))
print(*thi,sep='\n')