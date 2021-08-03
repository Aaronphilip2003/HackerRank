def miniMaxSum(arr):
	sum_min=0
	sum_max=0
	arr.sort()
	for i in range(0,len(arr)-1):
	 sum_min+=arr[i]
	for i in range(1,len(arr)):
		sum_max+=arr[i]
	print(sum_min,sum_max)


arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)
