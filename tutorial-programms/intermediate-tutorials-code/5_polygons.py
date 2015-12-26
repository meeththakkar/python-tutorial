import math

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y 

	def getDistanceFrom(self,other):
		return math.hypot(other.x-self.x , other.y-self.y)


class Polygon:
	def __init__(self,points):
		self.points = points

	def getArea(self):
		raise NotImplementedError(" this is abstract method")
	
	def getPoints(self):
		return self.points

	
class Triangle(Polygon):
	def __init__(self,points):
		super().__init__(points)
		

	def getArea(self):
		a = self.points[0].getDistanceFrom(self.points[1])
		b = self.points[1].getDistanceFrom(self.points[2])
		c = self.points[2].getDistanceFrom(self.points[0])
		s = (a + b + c ) /2
		return math.sqrt(s* (s-a) * (s-b) * ( s-c))

	def getPoints(self):
		return self.points

class Square(Polygon):
	def __init__(self,points):
                super().__init__(points)

	def getArea(self):
		a = self.points[0].getDistanceFrom(self.points[1])
		b = self.points[1].getDistanceFrom(self.points[2])
		return a*b

	def getPoints(self):
		return super().getPoints()

def main():
	points = [Point(0,0),Point(0,1),Point(1,1)]
	t = Triangle(points)
	print("Area: " + str(t.getArea()))

	points.append(Point(1,0))
	
	s = Square(points)
	
	print("Area: " + str(s.getArea()))

if __name__ == "__main__":
	main()


