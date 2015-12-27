import argparse


def fib(n,verbose):
	a,b = 0,1
	for i in range(n):
		
		a,b = b,a+b
		if(verbose):
			print(a)
	return a

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("num", help = "fibbonachi number you wish to calculate",type = int)
	parser.add_argument("-v","--verbose",help ="verbose logging" , action="store_true")
	args = parser.parse_args()	
	
	print(args.num)
	result = fib(args.num,args.verbose)
	
	print("fibbnoachi = " + str(result))
	


if __name__ =="__main__":
	main()
