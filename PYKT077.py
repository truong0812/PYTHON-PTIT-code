from datetime import datetime
n,m = list(int(i) for i in input().split())
mon ={}
for i in range(n):
    x = input().strip()
    y = input().strip()
    mon[x] = y
cathi = []
class Cathi:
    global mon
    def __init__(self,id,code,time,ca) -> None:
        self.id = "T%03d" %(id)
        self.code = code
        self.mon = mon[code]
        self.time = time
        self.timess = datetime.strptime(time, "%d/%m/%Y %H:%M")
        self.ca = ca
    def __str__(self) -> str:
        return "%s %s %s %s %s" %(self.id,self.code, self.mon, self.time, self.ca)
    
for i in range(m):
    arr = input().split()
    id = i+1
    code = arr[0]
    time = arr[1] + ' ' + arr[2]
    ca = arr[3]
    cathi.append(Cathi(id,code,time,ca))
    
cathi.sort(key=lambda x:x.timess)
print(*cathi,sep='\n')


