def bonAppetit(bill, k, b):
    notAnna=bill[k]
    sum=0
    bill.remove(notAnna)
    for i in bill:
        sum+=i
    sum=sum//2
    if sum==b:
        print("Bon Appetit")
    else:
        print(int(abs(b-sum)))




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())

bonAppetit(bill, k, b)

