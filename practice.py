# binary search
def linear_search(list,n):
	for i in range(len(list)):
		if list[i] == n:
			print("true")
		else:
			print("flase")
list = [ 1,2,3,5,6,8,9,7,55,22,33,44]
n = 5
if linear_search(list,n):
	print("Tim thay")
else:
	print("Khong tim thay")