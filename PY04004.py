import math

class pso:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def rutgon(self):
        z = math.gcd(self.x,self.y)
        self.x //= z
        self.y //= z
        return "{}/{}" .format(int(self.x), int(self.y))
    def cong(self, other):
        mau = (self.y * other.y) // math.gcd(self.y,other.y)
        tu = self.x * (mau // self.y) + other.x * (mau // other.y)
        a = pso(tu,mau)
        return a.rutgon()
    
arr = input().split()
a = pso(int(arr[0]),int(arr[1]))
b = pso(int(arr[2]),int(arr[3]))
print(a.cong(b))