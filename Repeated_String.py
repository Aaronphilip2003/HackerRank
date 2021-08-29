def repeatedString(s, n):
	length=len(s)
	buffer=n%length
	string=s[:buffer]
	d=string.count("a")
	x=n-buffer
	y=x/length
	n1=s.count("a")
	count_a=y*n1
	answer=count_a+d
	return int(answer)



s = input()
n = int(input())
result = repeatedString(s, n)
print(result)
