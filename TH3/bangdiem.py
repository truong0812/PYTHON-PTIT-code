id = 0
class Point:
    maHS = "HS"
    diemTB = 0
    xepLoai = ""
    def __init__(self, name, value):
        global id 
        id += 1
        self.maHS += "{:02d}".format(id)
        self.name = name
        x = value[0] * 2 + value[1] * 2
        for i in range(2, len(value)):
            self.diemTB += value[i]
        self.diemTB  += x
        self.diemTB = round(self.diemTB/ 10/ 1.2, 1)
        if self.diemTB >= 9: self.xepLoai += "XUAT SAC"
        elif self.diemTB >= 8 and self.diemTB <= 8.9: self.xepLoai += "GIOI"
        elif self.diemTB >= 7 and self.diemTB <= 7.9: self.xepLoai += "KHA"
        elif self.diemTB >= 5 and self.diemTB <= 6.9: self.xepLoai += "TB"
        else: self.xepLoai += "YEU"

    def __str__(self) -> str:
        return f"{self.maHS} {self.name} {self.diemTB} {self.xepLoai}"
        
if __name__ == "__main__":
    t = int(input())
    solve = []
    while t > 0:
        name = input()
        value = [float(x) for x in input().split()]
        solve.append(Point(name, value))
        t -= 1
    solve = sorted(solve, key = lambda x: (-x.diemTB, x.maHS))
    for i in solve:
        print(i)