def hurdleRace(k, height):
    maximum=0
    for i in height:
        if i>maximum:
            maximum=i
    if k>maximum:
        return 0
    elif maximum>k:
        return (maximum-k)




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

height = list(map(int, input().rstrip().split()))

result = hurdleRace(k, height)

print(result)
