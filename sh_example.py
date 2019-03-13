"""sh module. Contains Classes Shape, Square and Circle"""
class Shape:
	"""Has method move"""
	def __init__(self,x,y): #Contruction function / The first argument of any method is by convention called self
		self.x=x
		self.y=y

	def move(self, deltaX,deltaY): # a fucntion in class
		seft.x= self.x + deltaX
		seft.y= self.y + deltaY

class Square(Shape):
	"""Square Class:inherits from Shape""" 
	def __init__(self, side=1, x=0, y=0):
		Shape.__init__(self, x, y)
		self.side = side

class Circle(Shape): 
	"""Circle Class: inherits from Shape and has method area"""
	pi = 3.14159 
	def __init__(self, r=1, x=0, y=0):
		Shape.__init__(self, x, y) 
		self.radius = r 
	def area(self):
		"""Circle area method: returns the area of the circle."""
		return self.radius * self.radius * self.pi
	def __str__(self):  #The __str__ method is used by the print function
		return "Circle of radius %s at coordinates (%d, %d)"\
		% (self.radius, self.x, self.y)