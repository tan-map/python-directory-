class Stack:
	def __init__(self):
		self.items=[]

	def is_empty(self):
		return self.items==[]

	def push(self, data):
		self.items.append(data)

	def pop(self):
		return self.items.pop()

s = Stack()
s.push(3)
s.push(2)
s.push(4)
print(s.items)

s.pop()
s.pop()
s.pop()
print(s.items)

if s.is_empty():
	if __name__ == '__main__':
		print('Stack is empty')