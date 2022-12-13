class Candidate:
    def __init__(self, orderNumber, name, point, ethnic, region):
        self.code = "TS%02d" % (orderNumber)
        self.name = name
        self.point = float(point)
        self.ethnic = ethnic
        self.region = int(region)

    def getFormattedName(self):
        w = self.name.strip().lower().split()
        return " ".join(w).title()

    def getTotalPoint(self):
        pri = [1.5, 1.0, 0.0]
        return pri[self.region-1] + (0.0 if self.ethnic == "Kinh" else 1.5) + self.point

    def getStatus(self):
        return "Do" if self.getTotalPoint() >= 20.5 else "Truot"

    def __str__(self):
        return "%s %s %.1f %s" % (self.code, self.getFormattedName(), self.getTotalPoint(), self.getStatus())


if __name__ == "__main__":
    n = int(input())
    candidates = []
    for i in range(n):
        name, point, ethic, region = input(), input(), input(), input()
        candidates.append(Candidate(i+1, name, point, ethic, region))
    candidates.sort(key=lambda x: (-x.getTotalPoint(), x.code))
    for c in candidates:
        print(c)