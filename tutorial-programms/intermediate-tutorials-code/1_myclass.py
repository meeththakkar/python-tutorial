class MyClass:
	number = 0
	name = "noname"

def main():
	me = MyClass()
	me.number = 999
	me.name = "Meet Thakkar"
	friend = MyClass()
	friend.number = 555
	friend.name = "Dhaval"

	empty = MyClass()

	print("Name :" + me.name + " fav Number: " + str(me.number))
	print("Name :" + friend.name + " fav Number: " + str(friend.number))
	print("Name :" + empty.name + " fav Number: " + str(empty.number))


if __name__ == "__main__":
	main()
