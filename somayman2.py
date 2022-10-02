def somayman():
    
    x = input()
    check = "YES"
    for j in x:
        if(j != '4' and j != '7'):
            check = "NO"
            
    print(check)
    
for i in range (int(input())):
    somayman()
    