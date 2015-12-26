import math


def Main():
	try:
		number = float(input("please enter float: "))
		number = math.fabs(number)
		print(number)
	except:
		print("you did not enter a number")


if __name__ == "__main__":
	Main()


	
