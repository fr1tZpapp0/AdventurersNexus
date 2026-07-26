import random
from uuid import uuid4
from random import choice, randint
from ..world import World
from .continent_generator import generate_continent
from ..names.area_names import worldNames
from ..names.area_names import worldAges




### DO NOT CHANGE THIS LINE: RANDOM.SEED(INT) | IS HOW IT MUST BE DONE!
def generate_world():
	seed = randint(0, 999999999)
	random.seed(seed)
	

	world = World(
		id=uuid4(),
		name=choice(worldNames),
		seed=seed,
		age=choice(worldAges),
		continents=[],
		oceans=[],
		pantheon=[],
		calendar=[]
	)

	for i in range(randint(1, 5)):
		continent = generate_continent(world.continents)
		world.add_continent(continent)


	return world
