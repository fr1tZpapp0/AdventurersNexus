import random
from uuid import uuid4
from random import choice, randint, randrange

from ..classes.world import World
from ..classes.generator import GenerationContext


from .continent_generator import generate_continent


from ..names.world_names import worldNames
from ..names.world_names import worldAges
from ..names.continent_names import continentalNames
from ..names.settlement_names import settlementNames
from ..names.region_names import regionNames




### DO NOT CHANGE THE LINE: RANDOM.SEED(INT) | IS HOW IT MUST BE DONE!
def generate_world():
	available_settlement_names = settlementNames.copy()
	available_continent_names = continentalNames.copy()
	available_world_names = worldNames.copy()
	available_region_names = regionNames.copy()

	seed = randint(0, 999999999)
	random.seed(seed)
	world_seed_rng = random.Random(seed)

	context = GenerationContext(
		world_seed=seed,
		rng=world_seed_rng,

		available_settlement_names=available_settlement_names,
		available_continent_names=available_continent_names,
		available_region_names=available_region_names,
		available_world_names=available_world_names
	)
	
	

	world = World(
		id=uuid4(),
		name=context.rng.choice(worldNames),
		seed=seed,
		age=context.rng.choice(worldAges),
		continents=[],
		oceans=[],
		pantheon=[],
		calendar=[]
	)

	number_of_continents = context.rng.randint(3, 6)

	for _ in range(number_of_continents):
		continent = generate_continent(context)
		world.add_continent(continent)

	return world
