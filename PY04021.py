from datetime import datetime
class Gamer:
    def __init__(self,code,name,timein,timeout) :
        self.code = code
        self.name = name
        self.time = (datetime.strptime(timeout,"%H:%M") - datetime.strptime(timein,"%H:%M")).seconds // 60
    def __str__(self) :
        return "%s %s %s gio %s phut" %(self.code,self.name,self.time//60,self.time%60)

arr = []
for i in range(int(input())):
    arr.append(Gamer(input(),input(),input(),input()))
arr.sort(key= lambda x : -x.time)
for i in arr:
    print(i)
    

        