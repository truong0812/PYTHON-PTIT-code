phong = {}
class luong:
    global phong
    def __init__(self,code,name,time,lcb) :
        self.code = code
        self.name = name
        self.time = time
        self.lcb = lcb
    def phongban(self):
        return phong[self.code[-2::]]
    def tinhluong(self):
        x = ord(self.code[0]) - ord('A')
        y = int(self.code[1:3])
        if(y <= 3): y = 0
        if(4<= y <= 8): y = 1
        if(9<= y <= 15): y = 2
        if(16<= y): y = 3
        arr = [[10,12,14,20],[10,11,13,16],[9,10,12,14],[8,9,11,13]]
        z = arr[x][y]
        return self.time * self.lcb * z
    def __str__(self):
        return "%s %s %s %s000" % (self.code,self.name,self.phongban(),self.tinhluong())
    
for i in range(int(input())):
    x = input().split()
    y = ""
    for i in range(1,len(x)):
        y += x[i] + " "
    phong[x[0]] = y.strip()
arr = []
for i in range(int(input())):
    arr.append(luong(input().strip(),input().strip(),int(input().strip()),int(input().strip())))
for i in arr:
    print(i)
    
