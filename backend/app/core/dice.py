from random import randint, choice
from dataclasses import dataclass

@dataclass
class RolledDice:
	amount: int
	results: list[int]
	modifier: int
	advantage: bool
	disadvantage: bool
	kept_result: int
	total: int
	


acceptable_dice = [4, 6, 8, 10, 12, 20, 100]

def roll_dice(die_number, amount, modifier):
	results = []
	modded_result = []

	if die_number not in acceptable_dice:
		return "The dice isn't right. Please roll a d4, d6, d8, d10, d12, d20, or d100"

	else:
		if modifier is None:
			modifier = 0

		for i in range(amount):
			rolled_number = randint(1, die_number)
			rolled_modded = rolled_number + modifier
			results.append(rolled_number)
			modded_result.append(rolled_modded)

		total = sum(modded_result)


	return RolledDice(
		amount=amount,
		results=results,
		modifier=modifier,
		total=total,
		advantage=False,
		disadvantage=False,
		kept_result=0
	)



def adv_or_dis(modifier, isDisadvantage):
	results = []
	modded_results = []

	if modifier is None:
		modifier = 0

	
	rolled1 = randint(1, 20)
	rolled2 = randint(1, 20)

	results.append(rolled1)
	results.append(rolled2)


	mod1 = rolled1 + modifier
	mod2 = rolled2 + modifier

	modded_results.append(mod1)
	modded_results.append(mod2)

	if isDisadvantage:
		kept = min(modded_results)
		adv = False
		dis = True

	else:
		kept = max(modded_results)
		adv = True
		dis = False

	return RolledDice(
		amount=1,
		results=results,
		modifier=modifier,
		advantage=adv,
		disadvantage=dis,
		kept_result=kept,
		total=kept
	)
