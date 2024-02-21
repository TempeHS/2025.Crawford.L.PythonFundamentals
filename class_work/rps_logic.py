'''
Psudocode:

BEGIN rps_logic
	INPUT playerChoice = "Rock, Paper or Scissors"
	FUNCTION generate_random
	SWITCH CASE player_choice
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