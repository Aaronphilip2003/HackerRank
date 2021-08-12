def Digits(n):
    digitList=[]
    while(n>0):
        r=n%10
        digitList.append(r)
        n=n//10
    return digitList
        

def findDigits(n):
    digits=Digits(n)
    divisors=[]
    for i in digits:
        if i!=0:
            if n%i==0:
                divisors.append(i)
    return (len(divisors))
            


t = int(input().strip())
while(t!=0):
    n = int(input().strip())

    result = findDigits(n)

    print(result)
        
    t-=1
