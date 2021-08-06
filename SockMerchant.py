def sockMerchant(n, ar):
    diff_colors=[]
    count=[]
    sum=0
    pair=0
    for i in ar:
        if i not in diff_colors:
            diff_colors.append(i)
    for i in diff_colors:
        count.append(ar.count(i))
    
    for i in count:
        pair=i//2
        sum+=pair
    print(sum)



n = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)
