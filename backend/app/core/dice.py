from random import randint, choice

rolledDice = []
acceptable_dice = [4, 6, 8, 10, 12, 20, 100]

def diceRoll(die_number, amount, modifier):
	if die_number not in acceptable_dice:
		return "The dice isn't right. Please roll a d4, d6, d8, d10, d12, d20, or d100"
	
	else:
		rolledDice.clear()
		for i in range(amount):
			rolledNumber = randint(1, die_number)
			rolledNumber += modifier
			rolledDice.append(rolledNumber)

		return rolledDice

def advantage(modifier):
	rolledDice.clear()

	for i in range(2):
		rolledNumber = randint(1, 20)
		rolledNumber += modifier
		rolledDice.append(rolledNumber)

	return rolledDice
