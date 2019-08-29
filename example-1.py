class Queue:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items ==[]
	def enqueue(self, item):
		self.items.insert(0,item)
	def dequeue (self):
		return self.items.pop()
	def size(self):
		return len(self.items)



s=Queue()
s.enqueue(3)
s.enqueue(2)
s.enqueue(4)
s.enqueue(6)
s.enqueue(5)
print(s.items)


s.dequeue(3)
print(s.items)