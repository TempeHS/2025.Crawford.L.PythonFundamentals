w_vowel = input("Enter string: ")
vowels = "aeiouAEIOU"
c = 0

while c < len(w_vowel):
	if w_vowel[c].casefold() in vowels: # ensure that the vowel is lower case so that it can be compared to the vowels string
		w_vowel = w_vowel[:c] + w_vowel[c+1:] # remove the vowel from the string
	else:
		c += 1
		'''
  		NtS: If the vowel is removed from the string, the index should not be incremented.
		This is only necessary if the vowel is not removed from the string.
		'''
		continue
	# elif w_vowel[c] not in vowels:
	# 	c += 1
	# else:
	# 	c += 1
	# 	continue

print(w_vowel)