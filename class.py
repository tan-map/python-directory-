class Stack:
   def __init__(self):
       self.items = []

   def is_empty(self):
       return self.items == []

   def push(self, data):
       self.items.append(data)

   def pop(self):
       return self.items.pop()
   def __init__(self):
   		self.items=[]
    	self.maxsize= 4
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


 # hàm thêm phần tử
# s = Stack()
# s.push(3)
# s.push(2)
# s.push(4)
# print(s.items)
# #---------------------




# #hàm xóa phần tử

# s.pop()
# print(s.items)
#--------------------------
