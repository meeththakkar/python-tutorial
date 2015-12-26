def Main():
	try:
		f = open("dosentExist.txt","r")
		for line in f:
			print ( line.strip("\n\r"))
		f.close()
	except:
		print("file was either not found or unable to be read")

	finally:
		print("exiting")

if __name__ == "__main__":
	Main()
