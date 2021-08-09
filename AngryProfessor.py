def angryProfessor(k, a):
    count=0
    for i in a:
        if i<=0:
            count+=1
    
    if count<k:
        return "YES"
    else:
        return "NO"



t = int(input().strip())

while(t!=0):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = angryProfessor(k, a)

    print(result)
        
    t-=1
