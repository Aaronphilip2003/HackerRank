def birthdayCakeCandles(candles):
	candles.sort()
	max=0
	count=0
	for i in candles:
		if i > max:
			max=i
	for i in candles:
		if i==max:
			count+=1
	return count
		


candles = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(candles)
print(result)
