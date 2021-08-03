def pattern(n):
	spaces=n-2
	i=1
	while(spaces!=-1):
		print(spaces*" ",i*"#")
		i+=1
		spaces-=1
	print(n*"#")

n=int(input())
pattern(n)
