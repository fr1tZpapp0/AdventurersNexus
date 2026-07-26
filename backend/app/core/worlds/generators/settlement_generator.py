import random
from uuid import uuid4
from random import choice, randint
from ..settlement import Settlement
from ..names.area_names import settlementNames

def generate_settlement(settlement_list):
	seed = randint(0, 999999999)
	random.seed(seed)

	while True:
		if len(settlement_list) == 0 or len(settlement_list) is None:
			s_name = choice(settlementNames)
			break
		else:
			s_name = choice(settlementNames)
			if s_name in settlement_list:
				s_name = ""
				s_name = choice(settlementNames)
			else:
				break



	settlement = Settlement(
		id=uuid4(),
		seed=seed,
		name=s_name,
		style=[],
		population=randint(82, 5781),
		government=[],
		shops=[],
		npcs=[],
		taverns=[],
		quests=[]
	)




	return settlement