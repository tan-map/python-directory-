class Disk:
	def __init__(self,radius):
		self.radius=radius
	def diameter(self):
		return self.radius*3.14
	

class Stack:
	def __init__(self):
		self.items=[]

	def is_empty(self):
		return self.items==[]

	def push(self, data):
		self.items.append(data)

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

def move(n, source, helper, target):
	if n > 0:
		move(n - 1, source, target, helper) # move tower of size n - 1 to helper:
		if source:
			# print( "moving value in ", str(n), " from ", str(source) , " to " , target)
			print('Tru 1:',source.items)
			print('Tru 2:',helper.items)
			print('Tru 3:',target.items)
			print('====================')
			target.push(source.pop()) # move disk from source peg to target peg
		move(n - 1, helper, source, target)# move tower of size n-1 from helper to target


disk1=Disk(1).diameter()
disk2=Disk(2).diameter()
disk3=Disk(3).diameter()

stack1=Stack()
stack1.push(disk3)
stack1.push(disk2)
stack1.push(disk1)
if __name__ == '__main__':
	print('Tru 1 before:',stack1.items)
if __name__ == '__main__':
	print('==================')
stack2=Stack()
stack3=Stack()

move(stack1.size(),stack1,stack2,stack3)
if __name__ == '__main__':
	print('Result')
if __name__ == '__main__':
	print('Tru 1:',stack1.items)
if __name__ == '__main__':
	print('Tru 2:',stack2.items)
if __name__ == '__main__':
	print('Tru 3:',stack3.items)