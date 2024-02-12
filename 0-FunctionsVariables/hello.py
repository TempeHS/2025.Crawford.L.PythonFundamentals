def hello(to="World"):
	to = to.strip().title()
	print(f"Hello, {to}!")

def main():
	hello(
		input("What is your name? ")
	)

main()