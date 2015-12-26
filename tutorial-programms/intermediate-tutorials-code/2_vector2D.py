class Vector2D:
	x = 0
	y = 0

	def set(self,x,y):
		self.x = x
		self.y = y

def main():
	vect = Vector2D()
	vect.set(5,6)
	print("X is " + str(vect.x) + " y is " + str(vect.y))


if __name__ == "__main__":
	main()
