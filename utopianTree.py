def utopianTree(n):
    h=1
    i=1
    
    while(i<=n and n!=0):
        if i%2!=0:
            h=h*2
        else:
            h=h+1
        i+=1
    
    if(n==0):
        return 1
    
    return h

t = int(input().strip())

while(t!=0):
    n = int(input().strip())

    result = utopianTree(n)

    print(result)
        
    t-=1
