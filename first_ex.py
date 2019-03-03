example_list = [1,"2",3000,"hello",-1,[9999]]

element_3 = example_list[3]
print ("Element 3",element_3) #hello

element_2 = example_list[2]
print ("Element 2:",element_2) #3000

element_0 = example_list[0]
print ("Element 0:",element_0) #1

sum_element_0_2 = element_0 + element_2
print ("Sum 0 and 2: ",sum_element_0_2) #3001

element_last = example_list[-1]
print ("Last element: ",element_last) #[9999]

print ("Value of last element: ",element_last[0]) #9999

element_1 = example_list[1]
string3_1 = element_3+element_1
print ("String hello2: ", string3_1) #hello2


example_list[0] = 2
if example_list[0] == 1:
	print ("First element equal to one")
else:
	print ("First element not equal to one")
	print (example_list[0])