name = input("Insert a string: ")

# print(name[1:]) # prints all from the second character to the end of the string
# print(len(name)) # print the length of the string
# name = name[0].lower() + name[1:] # make the first character of the string lower case

# print(name[:2]) # prints all to the third character of the string excluding the third character

# for c in range(len(name)):
c = 0
while True:
	if name[c].isupper():
		name = name[:c] + '_' + name[c].lower() + name[c+1:]
		c += 1
	elif name[c].islower():
		c += 1
		'''
		NtS: If the elif statement is not included, the loop will run indefinitely. 
		(I thought it would stop when the condition is not met, but it doesn't.)
		'''
	else:
		c += 1
		continue
	if c < len(name):
		continue
	else: 
		break

# Just a complicated do while loop.


print(name)

'''
Below is another way to solve the problem.
It takes each character of the string, ckecks it and then appends no matter what it to a new string. It may not be the most efficient way to solve the problem.
The above solution checks each character of the string and then replaces it with the camel case version. It is more efficient than the below solution. 
'''
# 
# result = []
# def camel_to_snake(name):
# 	result = [name[0].lower()]
# 	for c in name[1:]:
# 		if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'): # or c.isupper()
# 			result.append('_')
# 			result.append(c.lower())
# 		else:
# 			result.append(c)
# 	return ''.join(result)
