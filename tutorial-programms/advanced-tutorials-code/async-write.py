import threading
import time


class AsyncfileWriter(threading.Thread):
	def __init__(self,text,outfile):
		threading.Thread.__init__(self)
		self.text = text
		self.outfile = outfile
	def run(self):
		f = open(self.outfile, "w")
		f.write(self.text)
		f.close()
		time.sleep(2)
		print("finished background file write"+ self.outfile)


def main():
	message = input("enter a string to store")
	out = input("enter file name ")
	
	background = AsyncfileWriter(message,out)
	background.start()

	print("programm can continue while it writes in another thread")
	
	background.join()

	print("everyting is done now .. all thread completed")


if __name__ == "__main__":
	main()
	 
