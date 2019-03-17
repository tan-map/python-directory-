class Queue:
	def __init__(self):
		self.items=[]
		self.maxsize=4

	def size(self):
		return len(self.items)

	def enqueue(self,data):
		if self.size()>=self.maxsize:
			return "Queue is full"
		else:
			self.items.insert(0,data)
			return data

	def dequeue(self):
		if self.size()<=0:
			return "Queue is empty"
		else:
			return self.items.pop()
			
	def is_empty(self):
		return self.items==[]


queue=Queue()
print('Insert: ',queue.enqueue(4))
print('Insert: ',queue.enqueue(1))
print('Insert: ',queue.enqueue(3))
print('Insert: ',queue.enqueue(20))
print('Insert: ',queue.enqueue(8))
print('Insert: ',queue.enqueue(12))

if __name__ == '__main__':
	print(queue.items)

queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
if __name__ == '__main__':
	print(queue.items)

if __name__ == '__main__':
	print(queue.size())

if 	queue.is_empty():
	if __name__ == '__main__':
		print('Queue is empty')


	