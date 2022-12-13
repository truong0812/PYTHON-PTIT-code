from datetime import datetime
class Cathi:
    def __init__(self,id,time,room) -> None:
        self.id = "C%03d" % (id)
        self.time = time
        self.timess = datetime.strptime(time, '%d/%m/%Y %H:%M')
        self.room = room
    def __str__(self) -> str:
        return "%s %s %s" %(self.id, self.time, self.room)

file = open('CATHI.in' , 'r')
n = int(file.readline())
cathi = []
for i in range(n):
    id = i + 1
    time = file.readline().strip() + ' ' + file.readline().strip()
    room = file.readline().strip()
    cathi.append(Cathi(id,time,room))
cathi.sort(key= lambda x:x.timess)
print(*cathi,sep='\n')


