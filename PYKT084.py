check = False
count = 0
for _ in range(int(input())):
    if(not check):
        print(input() + ": ",end = ' ')
        check = True
        continue
    if(input() == ''):
        print(count)
        check = False
        count = 0
        continue
    count += 1
print(count)

