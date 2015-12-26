def Main():
	words = ["cat","rat","bat","map"]
	
	with open("tut7_1_data.txt","w") as f:
		for word in words:
			f.write(word + "\n")


if __name__ == "__main__":
	Main()
