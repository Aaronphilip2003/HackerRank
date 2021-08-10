def viralAdvertising(n):
    liked=2
    shared=5
    cumulative=0
    while(n!=0):
        cumulative=cumulative+((shared//liked))
        shared=((shared//2)*3)
        n-=1
    return cumulative




 
n = int(input().strip())
result = viralAdvertising(n)
print(result)
