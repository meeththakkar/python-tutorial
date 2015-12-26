import math


def Main():
	try:
		rad = float(input("please enter float radious"))
		area = math.pi * rad**2 	
		print("aread =", area)
	except:
		print("you did not enter a number")


if __name__ == "__main__":
	Main()


	
