example_list = [1,"2",30000,"hello",-1,[9999]]

example_list[0] = 2
if example_list[0]==1:
    print("First element equal 1")
else:
    print("First element not equal 1")
    print(example_list[0])



sua cho vui 



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