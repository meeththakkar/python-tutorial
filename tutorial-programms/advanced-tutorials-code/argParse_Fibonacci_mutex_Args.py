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
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-v","--verbose",help ="vrbose mode" , action = "store_true")
	group.add_argument("-q","--quite",help ="quite mode" , action = "store_true")
	parser.add_argument("num", help = "fibbonachi number you wish to calculate",type = int)
	args = parser.parse_args()	
	
	print(args.num)
	result = fib(args.num,args.verbose)

	if args.verbose:
		print("fibbnoachi  calculated is  " + str(result))
	elif args.quite:
		print(result)
	else:
		print("ans=",result)


if __name__ =="__main__":
	main()
