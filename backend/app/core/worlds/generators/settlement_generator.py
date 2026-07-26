import random
from uuid import uuid4
from random import choice, randint

from ..classes.generator import GenerationContext
from ..classes.settlement import Settlement

def generate_settlement(context: GenerationContext):
	seed = randint(0, 999999999)
	random.seed(seed)

	s_name = context.available_settlement_names.pop(context.rng.randrange(len(context.available_settlement_names)))


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