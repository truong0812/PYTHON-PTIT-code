import decimal


class Tiennuoc:
    def __init__(self,stt,name,csc,csm):
        self.code = "KH%02d" %(stt)
        self.name = name
        self.chiso = csm - csc
    def getSurcharge(self):
        if (self.chiso > 100):
            return 5
        if (self.chiso > 50):
            return 3
        return 2

    def getTotal(self):
        cost, tmpUsed = 0, self.chiso
        if tmpUsed > 100:
            tmp = tmpUsed - 100
            cost += 200 * tmp
            tmpUsed -= tmp
        if tmpUsed > 50:
            tmp = tmpUsed - 50
            cost += 150 * tmp
            tmpUsed -= tmp
        if tmpUsed > 0:
            cost += 100 * tmpUsed
        return round(cost + (cost * self.getSurcharge() / 100))

    def __str__(self):
        return "%s %s %s" %(self.code,self.name,self.getTotal())
    
arr = []
for i in range(int(input())):
    arr.append(Tiennuoc(i+1,input(),int(input()),int(input())))
arr.sort(key=lambda x:(-x.getTotal(),x.code))
for i in arr:
    print(i)
    
