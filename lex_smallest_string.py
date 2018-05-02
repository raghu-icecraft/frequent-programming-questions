#find lexicographically smallest string by performing below operation.
#can perform the below operation in one minute
#Operation: Choose some limit X,Y between 1 and length of string and remove substring [X,Y]  from S.
#The first line of input will contain an integer T, denoting the number of test cases. 
#Each test case starts with 2 numbers N and K - length of S and the number of minutes Kevin has. Next line contains string S.

for i in range(input()):
	l=[int(x) for x in raw_input().split()]
	a=raw_input()
	res="z"*l[0]
	if(l[1]>1):
		res=min(a)
	else:
		for j in range(0,l[0]):
			res=min(res,a[j:l[0]])
		for k in range(1,l[0]+1):
			res=min(res,a[:k])
	print(res)
