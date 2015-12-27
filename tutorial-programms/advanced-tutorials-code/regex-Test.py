import re

def main():
	line = "I think I understand regular expressions"

	matchResult = re.match("think",line,re.M | re.I )

	if matchResult:
		print("match found" + matchResult.group())

	else:
		print("no match was found")



	searchResult = re.search('think',line, re.M| re.I )
	
	if searchResult:
		print("search found" + searchResult.group())
	else:
		print("nothing found in search")



if __name__ == "__main__":
	main()


