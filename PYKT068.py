class Monthi:
    def __init__(self,ma,ten,ht) -> None:
        self.ma = ma
        self.ten = ten
        self.ht = ht
    def __str__(self) -> str:
        return "%s %s %s" % (self.ma,self.ten,self.ht)
    
arr = []
for i in range(int(input())):
    arr.append(Monthi(input().strip(),input().strip(),input().strip()))
arr.sort(key=lambda x:x.ma)
print(*arr,sep='\n')

