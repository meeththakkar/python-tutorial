import socket


def main():
	host = "127.0.0.1"
	port = 5000
	
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))

	print("server started")

	while True:
		data,address = s.recvfrom(1024)
		data = data.decode("utf-8")
		print("message from "+str(address)+" is :" + data )
		data = data.upper()
		print("sending data " + data)
		s.sendto(data.encode("utf-8"),address)
	
	c.close()


if __name__ == "__main__":
	main()


