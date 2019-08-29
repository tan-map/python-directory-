# def search(arr, x):

#     for i in range(len(arr)):

#         if arr[i] == x:
#             return i

#     return -1
# arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
# x= 110
# print(search(arr, x))


# -----------binary search ------------
# def binary_search(arr, target):
# 	lower = 0
# 	upper = len(arr)
# 	while lower < upper:
# 		x = (lower + upper) // 2
# 		val = arr[x]
# 		if target == val:
# 			return x
# 		elif target > val:
# 			if lower == x:
# 				break
# 			lower = x
# 		elif target < val:
# 			upper = x
# arr= [1,2,3,4,33,22,44,55,33,22,44,55,33,44]
# target= 44
# print(binary_search(arr, target))


# --------quick sort----------
# def partition(arr, gt_dau, gt_cuoi):
# 	pt_chon = arr[gt_cuoi]
# 	small_i = gt_dau - 1
# 	for i in range(gt_dau, gt_cuoi):
# 		if arr[i] <= pt_chon:
# 			small_i += 1
# 			arr[small_i], arr[i] = arr[i], arr[small_i]
# 	small_i += 1
# 	arr[small_i], arr[gt_cuoi] = arr[gt_cuoi], arr[small_i]
# 	return small_i

# def quicksort(arr, gt_dau, gt_cuoi):
# 	if gt_dau < gt_cuoi:
# 		pt_chon = partition(arr, gt_dau, gt_cuoi)
# 		quicksort(arr, gt_dau, pt_chon - 1)
# 		quicksort(arr, pt_chon + 1, gt_cuoi)
# input_arr=[1,5,6,7,12,34,14,66,33,10,11,99,19]
# print(format(input_arr))
# print(quicksort(input_arr,0,len(input_arr)-1))
# print(input_arr)


# -------insertion sort ---------
# def insertion_soft(list):
# 	for i in range(1,len(list)):
# 		j = i
# 		while(j!= 0 and list[j] < list[j-1]):
# 			list[j-1],list[j] = list[j],list[j-1]
# 			j-= 1
# arr=[1,5,43,67,99,545,33,4,3,8,45,34,66,323,666]
# print(insertion_soft(arr))
# print(arr)
# selection sort ( lay phan tu dau roi so sanh cac pt cong lai, nho nhat thi dua ve vi tri 0 cua mang)
def selection_sort(list):
	for i i n range(0, len(list) - 1):
		minIndex = i
		for j in range(i+1, len(list)):
			if list[j] < list[minIndex]:
				minIndex = j
		if minIndex != i:
			list[i] , list[minIndex] = list[minIndex] , list[i]
 arr=[1,5,43,67,99,545,33,4,3,8,45,34,66,323,666]
 print(selection_sort(arr))
 print(arr)