from threading import Thread
import time


def timer(name,delay,repeat):
	print("timer: " + name + "Started")
	while repeat>0:
		time.sleep(delay)
		print(name + ": " + time.ctime(time.time()))
		repeat-=1 
	print("TImer "+ name + " is completed")


def main():
	t1 = Thread(target = timer, args = ("Timer1", 1, 5))
	t2 = Thread(target = timer, args = ("Timer2", 2, 5))
	t3 = Thread(target = timer, args = ("Timer3", 5, 5))
	
	t1.start()
	t2.start()
	t3.start()
	
	print("main completed")


if __name__ == "__main__":
	main()
