import time
start = time.time()

def functSum (a: int,b: int,c: int) -> int:
	sum=0
	x=0
	while x <= c:
		if a<b:
			sum=sum + a + b
		elif a>b:
			sum = sum + (a - b)
		if sum > 100:
			break
		x = x +1
	return sum

if __name__ == '__main__':
	print("Sum:",functSum(1,2,3))


# fib(3) = fib(2) + fib(1) = ( fib(1) + fib(0) ) + fib(1) = 1 + 0 + 1

def fib(a: int) ->int:
	# print ("Calculating: Fib",a)
	if a<=2:
		return 1
	return fib(a-1)+fib(a-2)

if __name__ == '__main__':
	print (fib(25))
	

def fib2(a: int) ->int:
	dict_fib={0:0,1:1}
	print ("Calculating: Fib2",a)
	if a<=2: 
		return 1
	else:
		for x in range(2, a+1):
			dict_fib[x]=dict_fib[x-1]+dict_fib[x-2]
		return dict_fib[x]
        
if __name__ == '__main__':
	print(fib2(500))

end = time.time()
print ("Time executed:", end -start)