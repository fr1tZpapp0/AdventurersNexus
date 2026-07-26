import random
from uuid import uuid4
from random import choice, randint



from ..classes.continent import Continent
from ..classes.generator import GenerationContext

from .region_generator import generate_region


def generate_continent(context: GenerationContext):
	seed = randint(0, 999999999)
	random.seed(seed)

	c_name = context.available_continent_names.pop(context.rng.randrange(len(context.available_continent_names)))


	continent = Continent(
		id=uuid4(),
		name=c_name,
		seed=seed,
		regions=[],
		mountain_ranges=[],
		rivers=[],
		climate=[],
		size=randint(1, 10)
	)

	for i in range(randint(1, 4)):
		region = generate_region(context)
		continent.add_region(region)


	return continent

