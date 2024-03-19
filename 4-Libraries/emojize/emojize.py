import emoji

ji = input("Enter the emoji: ")
print(emoji.emojize("Output: " + ji))

# print(emoji.emojize('Python is :thumbs_up:'))
# print(emoji.emojize('Python is :thumbsup:', language='alias'))
# print(emoji.demojize('Python is 👍'))
# print(emoji.emojize("Python is fun :red_heart:"))
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type")) # red heart, not black heart
# print(emoji.is_emoji("👍")) # Print True if character is an emoji