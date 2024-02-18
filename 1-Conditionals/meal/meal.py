def convert(time):
	hours, minutes = time.split(":")
	if int(hours) > 24 or int(minutes) > 60: # Filter invalid time
		print("Invalid time")
		exit() # Exit the program
	time = int(hours) + (int(minutes) / 60)
	return time

# def main():
# 	...

time = input("Insert time: ")
conTime = convert(time)

print(conTime)

# if __name__ == "__main__":
# 	main()
