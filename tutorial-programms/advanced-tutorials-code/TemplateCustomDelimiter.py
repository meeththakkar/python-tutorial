from string import Template


class MyTemplate(Template):
	delimiter = "#"

def main():
	cart = []
	cart.append(dict(item="coke",price=8, quantity=2))
	cart.append(dict(item="cake",price=12,quantity = 1))
	cart.append(dict(item="fish",price=32,quantity =  4))

	# double delimeter skips it
	# {} is used to clearly specify token  
	t = MyTemplate("###quantity x #{item}pcs.  = #price ")

	total  =0
	print("cart")

	for data in cart:
		print ( t.substitute(data))
		total+= data["price"]

	print("total", total)


if __name__ == "__main__":
	main()
