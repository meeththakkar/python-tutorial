class SkippingIterator:
	def __init__(self,data,stepSize):
		if stepSize <=0:
			raise Exception("stepSize must be greateer than 1")
		self.data = data
		self.stepSize = stepSize
		self.index = len(data)
		self.curIndex = 0
	def __iter__(self):
		return self
	def __next__(self):
		if self.index - self.curIndex  <self.stepSize:
			raise StopIteration
		else:
			ret = self.data[self.curIndex]
			self.curIndex  = self.curIndex + self.stepSize
			return ret



def main():
	rev = SkippingIterator('1234567890',2)
	for char in rev:
		print(char)

if __name__ == '__main__':
	main()

