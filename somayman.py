x = input()
dem = 0
for i in x:
    if(i == '4' or i == '7'):
        dem += 1
if (dem == 4 or dem == 7):
    print("YES")
else:
    print("NO")
    