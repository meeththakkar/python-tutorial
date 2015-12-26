def Main():
	f = open("tut7_1_data.txt","w")

	print("please enter few words to append")
	for i in range(4):
		f.write(input("please enter a word") + "\n")



	f.close()

if __name__ == "__main__":
	Main()
