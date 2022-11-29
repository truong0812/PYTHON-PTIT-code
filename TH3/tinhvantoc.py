from datetime import datetime


class Racer:
    def __init__(self, name, city, timeFinish):
        self.name = name
        self.city = city
        self.timeFinish = timeFinish

    def getCode(self):
        code = ""
        for i in range(len(self.city)):
            if i == 0 or self.city[i-1] == " ":
                code += self.city[i]
        for i in range(len(self.name)):
            if i == 0 or self.name[i-1] == " ":
                code += self.name[i]
        return code

    def getVelocity(self):
        rangeTime = (datetime.strptime(self.timeFinish, "%H:%M") -
                     datetime.strptime("6:00", "%H:%M")).seconds/3600
        return round(120/rangeTime)

    def __str__(self):
        return "%s %s %s %s Km/h" % (self.getCode(), self.name, self.city, self.getVelocity())


if __name__ == "__main__":
    n = int(input())
    racers = []
    for i in range(n):
        racers.append(Racer(input(), input(), input()))
    racers.sort(key=lambda x: x.timeFinish)
    for x in racers:
        print(x)
        



