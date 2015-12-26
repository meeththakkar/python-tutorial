import math

class Vector2D:

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __add__(self,other):
		return Vector2D(self.x+other.x , self.y+other.y)

	def __iadd__(self,other):
		self.x += other.x
		self.y += other.y
		return self

	def __sub__(self,other):
		return Vector2D(self.x-other.x , self.y-other.y)

	def __isub__(self,other):
		self.x -= other.x
		self.y -= other.y
		return self

	def __mul__(self,other):
		return Vector2D(self.x*other.x, self.y*other.y)

	def __imul__(self,other):
		self.x *= other.x
		self.y *= other.y
		return self


	def getLength(self):
		return math.sqrt(self.x**2 + self.y**2)

	def normalized(self):
		length = self.getLength()
		if length != 0:
			return Vector2D(self.x / length , self.y/length)
		return Vector2D(self)

	def getAngle(self):
		return math.degrees(math.atan2(self.y,self.x))

	def __str__(self):
		return "X: "+str(self.x) + " Y: "+str(self.y)



def main():
	vect = Vector2D(5,6)
	print(vect)
	vect2 = Vector2D(2,3)
	print(vect2)

	tempMethod = vect.getAngle
	
	print("adding")
	vect = vect + vect2
	print(vect)
	
	print("iadd")
	vect += vect2
	print(vect)

	print("imul")
	vect *= Vector2D(2,2)
	print(vect)

	print("normakized")
	print(vect.normalized())

	print("angle: " + str(vect.getAngle()))
	print("angle via method via method var" + str(tempMethod()))

if __name__ == "__main__":
	main()
