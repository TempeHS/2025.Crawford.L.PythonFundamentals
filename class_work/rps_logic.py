import random

def generate_random():
	rps_seed = random.randint(1, 3)
	if rps_seed == 1:
		return "rock"
	elif rps_seed == 2:
		return "paper"
	else:
		return "scissors"
	
draw = "The result is a draw."
win = "The result is a win."
lose = "The result is a loss."

no_games = 0

while True:
	try:
		request_games = int(input("No. of games?").strip())
	except ValueError:
		print("Invalid number of games. Please enter a number ")
	else:
		break

while no_games < request_games:
	player_choice = input("Rock, Paper or Scissors? ").strip().casefold()
	computer_choice = generate_random()
	match computer_choice:
		case "rock":
			if player_choice == "paper":
				print(win)
				no_games += 1
			elif player_choice == "scissors":
				print(lose)
				no_games += 1
			else:
				print(draw)
				no_games += 1
		case "paper":
			if player_choice == "scissors":
				print(win)
				no_games += 1
			elif player_choice == "rock":
				print(lose)
				no_games += 1
			else:
				print(draw)
				no_games += 1
		case "scissors":
			if player_choice == "rock":
				print(win)
				no_games += 1
			elif player_choice == "paper":
				print(lose)
				no_games += 1
			else:
				print(draw)
				no_games += 1
		case _:
			print("Invalid choice. Please type a valid choice.")

'''
Psudocode:

BEGIN rps_logic
	INPUT playerChoice = "Rock, Paper or Scissors"
	FUNCTION generate_random
	MATCH player_choice
		CASE rock
			IF player_choice == paper
				PRINT "Win"
			ELSEIF player_choice == scissors
				PRINT "Lose"
			ELSE
				PRINT "Draw"
		CASE paper
			IF player_choice == scissors
				PRINT "Win"
			ELSEIF player_choice == rock
				PRINT "Lose"
			ELSE
				PRINT "Draw"
		CASE scissors
			IF player_choice == rock
				PRINT "Win"
			ELSEIF player_choice == paper
				PRINT "Lose"
			ELSE
				PRINT "Draw"
END rps_logic
'''