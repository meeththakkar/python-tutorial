class Pet:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def talk(self):
		raise NotImplementedError("Example Error : sub class must implement this abstract method")

class Cat(Pet):
	def __init__(self,name,age):
		super().__init__(name,age) # can not run super class mthods like this

	def talk(self):
		return "Meeoww"

class Dog(Pet):
	def __init__(self,name,age):
		super().__init__(name,age) 

	def talk(self):
		return "woof"



def main():
	pet = Pet("p1",1)
	jess = Cat("jess",4)
	print("is jess a pet" + str(isinstance(jess,Cat)))
	print("is jess a pet" + str(isinstance(jess,Pet)))
	print("is pet a cat"  + str(isinstance(pet,Cat)))
	print("is pet a pet"  + str(isinstance(pet,Pet)))



	pets = [jess,Dog("jack",2), Cat("Fred",1),pet]

	for pet in pets:
		print("Name:" + pet.name + "age "+ str(pet.age) + "says " + pet.talk())


if __name__ == "__main__":
	main()		
