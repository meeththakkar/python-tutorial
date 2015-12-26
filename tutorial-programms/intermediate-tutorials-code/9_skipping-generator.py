def SkippingGenerator(data,stepSize):
	if(stepSize <= 0):
		raise Exception("pleae provide positive step size")

	for i in range(0,len(data),stepSize):
		yield data[i]


def main():
	rev = SkippingGenerator('malyalam',1)
	for char in rev:
		print(char)
	rev  = SkippingGenerator("TEEM",3)
	for char in rev:
		print(char)
	data = "abcdefijklmnopqrstuvwxyz"
	print(list(data[i] for i  in range (0,len(data),3)))

if __name__ == "__main__":
	main()
