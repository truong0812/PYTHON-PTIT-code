
def doit():
    x = int(input())
    print ("1", end ='')
    for i in range(2,int(x ** 0.5)):
        dem = 0
        while( x % i == 0):
            dem += 1
            x /=i
        if(dem != 0): print(" * " + str(i) + "^" + str(dem) ,end = '' )

    if(x != 1): print( " * " +str(int(x)) + "^1")
    else: print()
    
for i in range(int(input())):
    doit()
    
    