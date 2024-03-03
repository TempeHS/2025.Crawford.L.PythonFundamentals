allowed_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
no_letters = 0
no_numbers = 0

# while True:
# 	request = input("Request plate: ")
# 	# print(len(request))
# 	# print(request[len(request)-1])
# 	if 2 <= len(request) <= 6:
# 		print(f"'{request}' is within the allowed length.")
# 		c = 0
# 		while c < len(request):
# 			if request[c] not in allowed_char:
# 				if request[c] in lower_case:
# 					print(f"invalid. '{request[c]}' is a lower case letter. please enter with capital letters.")
# 					break
# 				else:
# 					print(f"invalid. '{request[c]}' is not a valid character.")
# 					break
# 			else:
# 				c += 1
# 				continue
# 		else:
# 			print(f"'{request}' is a valid plate.")
# 			break
# 	else:
# 		print("Invalid. Please enter a valid plate request.")
# 		continue

def len_query(request):
	if 2 <= len(request) <= 6:
		print(f"'{request}' is within the allowed length.")
		return True
	else:
		print(f"'{request}' is not within the allowed length.")
		return False

def char_check(request):
	c = 0
	while c < len(request):
		if request[c] not in allowed_char:
			if request[c] in lower_case:
				print(f"Invalid. '{request[c]}' is a lower case letter. Please enter with capital letters.")
				return False
			else:
				print(f"Invalid. '{request[c]}' is not a valid character.")
				return False
		else:
			c += 1
			continue
	else:
		print(f"'{request}' is a valid plate.")
		return True

def last_char(request):
	if request[len(request)-1] in numbers:
		print(f"'{request[len(request)-1]}' is a number.")
		return True
	else:
		print(f"Invalid. '{request[len(request)-1]}' is a letter. Please enter a number in the last character.")
		return False

def first_char(request):
	if request[0] in letters:
		print(f"'{request[0]}' is a letter.")
		return True
	else:
		print(f"Invalid. '{request[0]}' is a number. Please enter a letter in the first character.")
		return False