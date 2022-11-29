from datetime import datetime


class Customer:
    def __init__(self, orderNumber, name, roomCode, arrive, left, service):
        self.code = "KH%02d" % (orderNumber)
        self.name = name
        self.roomCode = roomCode
        self.arrive = arrive
        self.left = left
        self.service = service

    def getRangeTime(self):
        return (datetime.strptime(self.left, "%d/%m/%Y") - datetime.strptime(self.arrive, "%d/%m/%Y")).days+1

    def getCost(self):
        unitPrice = [25, 34, 50, 80]
        return (self.getRangeTime() * unitPrice[int(self.roomCode[0])-1] + self.service)

    def __str__(self):
        return "%s %s %s %s %s" % (self.code, self.name, self.roomCode, self.getRangeTime(), self.getCost())


if __name__ == "__main__":
    n = int(input())
    customers = []
    for i in range(n):
        customers.append(Customer(i+1, input().strip(), input().strip(),
                         input().strip(), input().strip(), int(input().strip())))
    customers.sort(key=lambda x: x.getCost(), reverse=True)
    for x in customers:
        print(x)