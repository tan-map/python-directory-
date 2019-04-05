class Disk:
	def __init__(self,bk):
		self.bk=bk
	def diameter(self):
		return self.bk

class Stack:
	def __init__(self):
		self.items=[]

	def push(self, data):
		self.items.append(data)

	def pop(self):
		return self.items.pop()

def hanoi(n, col_1, col_3, col_2):
	if n > 0:
		hanoi(n - 1, col_1, col_2, col_3)
		if col_1:
			print('Tru 1:',col_1.items)
			print('Tru 2:',col_3.items)
			print('Tru 3:',col_2.items)
			print('******next-step******')
			col_2.push(col_1.pop()) 
		hanoi(n - 1, col_3, col_1, col_2)

disk1=Disk(1).diameter()
disk2=Disk(2).diameter()
disk3=Disk(3).diameter()
disk4=Disk(4).diameter()

stack1=Stack()
stack1.push(disk3)
stack1.push(disk2)
stack1.push(disk1)
if __name__ == '__main__':
	print('Tru 1 before:',stack1.items)
if __name__ == '__main__':
	print('*****next-step******')
stack2=Stack()
stack3=Stack()


hanoi(len(stack1.items),stack1,stack2,stack3)
if __name__ == '__main__':
	print('Result')
if __name__ == '__main__':
	print('Tru 1:',stack1.items)
if __name__ == '__main__':
	print('Tru 2:',stack2.items)
if __name__ == '__main__':
	print('Tru 3:',stack3.items)