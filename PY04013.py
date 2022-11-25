from datetime import datetime
from collections import defaultdict
if __name__ == "__main__":
    myMap = defaultdict(list)
    index = 1
    for i in range(int(input())):
        city, start, stop, rainAmount = input(), input(), input(), int(input())
        rainTime = (datetime.strptime(stop, "%H:%M") -
                    datetime.strptime(start, "%H:%M")).seconds//60
        if city in myMap.keys():
            myMap[city][0] += rainAmount
            myMap[city][1] += rainTime
        else:
            myMap[city] = [rainAmount, rainTime, "T%02d" % (index)]
            index += 1
    for city in list(myMap.keys()):
        print("%s %s %.2f" %
              (myMap[city][2], city, myMap[city][0]/myMap[city][1]*60))