def main():
	x = get_int()
	print(f"x is {x}.")

def get_int():
	while True:
		x = input("What is x? ")
		try:
			x = int(x)
		except ValueError:
			pass
			# print(f"'{x}' is not a number or valid number.")
		else:
			break
	return x

main()

