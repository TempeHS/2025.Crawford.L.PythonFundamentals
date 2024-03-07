# Sample dictionary
nutrition_info = {
	"apple": {"calories": 150},
	"avacado": {"calories": 50},
	"banana": {"calories": 110},
	"cantaloupe": {"calories": 50},
	"grapefruit": {"calories": 60},
	"grapes": {"calories": 90},
	"honeydew melon": {"calories": 50},
	"kiwifruit": {"calories": 90},
	"lemon": {"calories": 15},
	"lime": {"calories": 20},
	"nectarine": {"calories": 60},
	"orange": {"calories": 80},
	"peach": {"calories": 60},
	"pear": {"calories": 100},
	"pineapple": {"calories": 50},
	"plum": {"calories": 70},
	"strawberry": {"calories": 50},
	"sweet cherries": {"calories": 100},
	"tangerine": {"calories": 50},
	"watermelon": {"calories": 80},
}

while True:
	food = input("Enter the food: ").casefold().strip()
	if food not in nutrition_info:
		# print("Food not found.")
		continue
	else:
		print(f"Calories: {nutrition_info[food]['calories']}")
		break

# food = input("Enter the food: ").casefold().strip()

# # Check if the food is in the dictionary
# if food not in nutrition_info:
# 	exit()

# # Accessing values from the dictionary
# print(f"Calories: {nutrition_info[food]["calories"]}")