import math

class pso:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def rutgon(self):
        z = math.gcd(self.x,self.y)
        self.x /= z
        self.y /= z
        return "{}/{}" .format(int(self.x), int(self.y))
    
arr = input().split()
a = pso(int(arr[0]),int(arr[1]))
print(a.rutgon())