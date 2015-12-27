import threading
import time


tLock = threading.Lock()


def timer(name,delay,repeat):
	print("timer: " + name + "Started")
	tLock.acquire()	
	print("Name:" + name + "has acquired Lock")
	while repeat>0:
		time.sleep(delay)
		print(name + ": " + time.ctime(time.time()))
		repeat-=1 
	print(name + " is releaseing lock")
	tLock.release()
	print("TImer "+ name + " is completed")
	


def main():
	t1 = threading.Thread(target = timer, args = ("Timer1", 1, 5))
	t2 = threading.Thread(target = timer, args = ("Timer2", 2, 5))
	t3 = threading.Thread(target = timer, args = ("Timer3", 5, 5))
	
	t1.start()
	t2.start()
	t3.start()
	
	print("main completed")


if __name__ == "__main__":
	main()
