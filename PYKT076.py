from datetime import datetime
n,m = list(int(i) for i in input().split())
theloai = {}
for i in range(n):
    x = "TL%03d" %(i+1)
    y = input()
    theloai[x] = y
phim = []
class Movie:
    global theloai
    def __init__(self,id,tl,time,name,slg):
        self.id = "P%03d" % (id)
        self.theloai = theloai[tl]
        self.name = name 
        self.time = time
        self.slg = slg
    def __str__(self) -> str:
        return "%s %s %s %s %s" %(self.id, self.theloai, self.time, self.name, self.slg)

for i in range(m):
    phim.append(Movie(i+1,input().strip(), input().strip(), input().strip(), input().strip()))
phim.sort(key=lambda x: datetime.strptime(x.time,"%d/%m/%Y"), reverse=False)
print(*phim,sep='\n')

