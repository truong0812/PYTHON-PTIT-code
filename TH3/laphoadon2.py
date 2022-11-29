from datetime import datetime 

class hoadon:
    def __init__(self,id,name,room,timein,timeout,bonus):
        self.code = "KH%02d" %(id)
        self.name = name
        self.room = room
        self.bonus = bonus
        self.time = self.gettime(timein,timeout)
    def gettime(self,timein,timeout):
        return (datetime.strptime(timeout, "%d/%m/%Y") - datetime.strptime(timein, "%d/%m/%Y")).days + 1
    def thanhtien(self):
        arr = [25,34,50,80]
        x = arr[int(self.room[0]) - 1]
        return x * self.time + self.bonus
    def __str__(self):
        return "%s %s %s %s %s" % (self.code,self.name,self.room,self.time,self.thanhtien())
    
arr = []
for i in range(int(input())):
    arr.append(hoadon(i+1,input().strip(),input().strip(),input().strip(),input().strip(),int(input().strip())))
arr.sort(key=lambda x: - x.thanhtien())
for i in arr:
    print(i)
    
