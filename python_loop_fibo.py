# ------------- vong lap for ---------------------#
import time
start = time.time()

def functSum (a: int,b: int,c: int)->int:
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
	print (functSum(10,20,70))

#--------------- tinh--finbonacci-------------------#


# def funcFib(num: int):
#   if (num <= 1):
#     return num
#   else:
#     return funcFib(num-1) + funcFib(num-2)
# print(funcFib(25))
#----------------------------------------------#
def fib(a: int) ->int:
    print("Calculating: Fib ",a)
    if a<=2:
        return 1
    return fib(a-1)+fib(a-2)
if __name__ == '__main__':
	print(fib(25))

fib_dict={0:0,1:1}
def fibo(n: int)->int:
     if(n==0):
       return 0
     if(n==1):
       return 1
     else:
          for i in range(2, n+1):
                fib_dict[i]=fib_dict[i-1]+fib_dict[i-2]
          return(fib_dict[i])

if __name__ == '__main__':
	print(fibo(200))


end = time.time()
print("Time executed:",end - start)