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

player_choice = input("Rock, Paper or Scissors? ").strip().casefold()
computer_choice = generate_random()
match computer_choice:
	case "rock":
		if player_choice == "paper":
			print(win)
		elif player_choice == "scissors":
			print(lose)
		else:
			print(draw)
	case "paper":
		if player_choice == "scissors":
			print(win)
		elif player_choice == "rock":
			print(lose)
		else:
			print(draw)
	case "scissors":
		if player_choice == "rock":
			print(win)
		elif player_choice == "paper":
			print(lose)
		else:
			print(draw)
	case _:
		print("Invalid choice. Please type a valid choice.")
		exit()

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