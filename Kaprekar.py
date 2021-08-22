# INCOMPLETE


def noOfDigits(p):
	count=0
	while(p>0):
		p=p//10
		count+=1
	return count

def splitNo(p):
	sum=0
	while(p>0):
		r = p%10
		sum+=r
		p = p//10
	return sum

def kaprekarNumbers(p,q):
	list_kap=[]
	for i in range (p,q+1):
		sq=i*i
		sum=0
		dig=noOfDigits(i)
		if dig == 1:
			if splitNo(sq) == i:
				list_kap.append(i)
			else:
				pass
		else:
			pass
		print(list_kap)

		
        

p = int(input().strip())
q = int(input().strip())
kaprekarNumbers(p, q)



