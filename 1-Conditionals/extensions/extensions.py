typ = input("Type file: ")
typ = typ.strip().casefold()

file_extension = '.' + typ.split('.')[-1]

if file_extension in [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]:
	if file_extension == ".gif":
		print("image/gif")
	elif file_extension == ".jpg" or ".jpeg":
		print("image/jpeg")
	elif file_extension == ".png":
		print("image/png")
	elif file_extension == ".pdf":
		print("application/pdf")
	elif file_extension == ".txt":
		print("text/plain")
	elif file_extension == ".zip":
		print("application/zip")
else:
	print("application/octet-stream")
