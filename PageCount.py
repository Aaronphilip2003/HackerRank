
def pageCount(n, p):
    first=0
    last=n
    count=0
    if (abs(p-first)>=abs(p-last)):
        while(last!=p):
            last-=1
            count+=1
        if(count==1):
            print(count)
        elif(count>1):
            print(count//2)
        else:
            print("0")
    elif(abs(p-first)<abs(p-last)):
        while(first!=p):
            first+=1
            count+=1
        if (count==1):
            print(count)
