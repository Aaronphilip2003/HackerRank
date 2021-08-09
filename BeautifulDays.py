def Rev(a):
    rev=0
    while(a!=0):
        r=a%10
        rev=rev*10+r
        a=a//10
    return rev
        

def beautifulDays(i, j, k):
    count=0
    for p in range(i,j+1):
        diff=0
        diff=abs(p-Rev(p))
        if diff%k==0:
            count+=1
    return count
            
        

first_multiple_input = input().rstrip().split()

i = int(first_multiple_input[0])

j = int(first_multiple_input[1])

k = int(first_multiple_input[2])

result = beautifulDays(i, j, k)

print(result)
