while True:
	print(
		"Hello, this is my menu\n"
		"1: Option One\n"
		"2: Option Two\n"
		"3: Option Three\n"
		"4: Exit"
	)
	init = input("Enter option: ")
	if init == "": # init == ""
		print("No input detected.")
	elif init not in ["1", "2", "3", "4"]: # not in ["1", "2", "3", "4"]
		print("Invalid Option! Please try again.") # print("Invalid Option! Please try again.")
	else:
		match init:
			case "1":
				print("Option 1 picked.")
			case "2":
				print("Option 2 picked.")
			case "3":
				print("Option 3 picked.")
			case "4":
				print("Exit")
				break
  		# if init == "1":
		# 	print("Option 1 picked.")
		# 	continue
		# elif init == "2":
		# 	print("Option 2 picked.")
		# 	continue
		# elif init == "3":
		# 	print("Option 3 picked.")
		# 	continue
		# elif init == "4":
		# 	print("Exit")
		# 	break
'''
I don't know if we have to handle exceptions or not.
'''
