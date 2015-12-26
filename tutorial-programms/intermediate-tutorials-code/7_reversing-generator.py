def  Reverse(data):
	for index in range(len(data)-1,-1,-1):
		yield data[index]


def main():
	rev = Reverse('malyalam')
	for char in rev:
		print(char)


	rev  = Reverse("TEEM")
	for char in rev:
		print(char) 
	
	data = "abcdef"
	print(list(data[i] for i  in range (len(data)-1,-1,-1)))

if __name__ == "__main__":
	main()
