s = input()
s = s[::-1]
x = ""
dem = 0
for i in s:
    if(dem == 3):
        x = "," + x
        dem = 0
    x = i + x
    dem += 1
    
    
print(x)