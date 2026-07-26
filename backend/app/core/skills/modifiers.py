MINIMUM_ABILITY_STAT_NUMBER = 0
MINIMUM_ROLLED_ABILITY_STAT_NUMBER = 3

MAXIMUM_ROLLED_ABILITY_STAT_NUMBER = 20
MAXIMUM_ABILITY_STAT_NUMBER = 30


def get_AbilityModifier(stat_Number):
	ability_Modifier = 0
	if stat_Number == 0 or stat_Number == 1:
		ability_Modifier = -5
        
	elif stat_Number == 2 or stat_Number == 3:
		ability_Modifier = -4

	elif stat_Number == 4 or stat_Number == 5:
		ability_Modifier = -3

	elif stat_Number == 6 or stat_Number == 7:
		ability_Modifier = -2

	elif stat_Number == 8 or stat_Number == 9:
		ability_Modifier = -1

	elif stat_Number == 10 or stat_Number == 11:
		ability_Modifier = 0

	elif stat_Number == 12 or stat_Number == 13:
		ability_Modifier = 1

	elif stat_Number == 14 or stat_Number == 15:
		ability_Modifier = 2

	elif stat_Number == 16 or stat_Number == 17:
		ability_Modifier = 3
	
	elif stat_Number == 18 or stat_Number == 19:
		ability_Modifier = 4

	elif stat_Number == 20 or stat_Number == 21:
		ability_Modifier = 5

	elif stat_Number == 22 or stat_Number == 23:
		ability_Modifier = 6

	elif stat_Number == 24 or stat_Number == 25:
		ability_Modifier = 7

	elif stat_Number == 26 or stat_Number == 27:
		ability_Modifier = 8

	elif stat_Number == 28 or stat_Number == 29:
		ability_Modifier = 9

	elif stat_Number == 30:
			ability_Modifier = 10


	return ability_Modifier


