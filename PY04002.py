class Rectangle:
    def __init__ (self,h,w,clr):
        self.x = h
        self.y = w
        self.clr = clr
    def perimeter(self):
        return (self.x + self.y) * 2
    def area(self):
        return self.x * self.y
    def color(self):
        return self.clr.capitalize()

arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if r.x <= 0 or r.y <= 0:
    print("INVALID")
else:
    print(r.perimeter(), r.area(), r.color())