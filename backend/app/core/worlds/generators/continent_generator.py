import random
from uuid import uuid4
from random import choice, randint
from ..continent import Continent
from .region_generator import generate_region
from ..names.area_names import continentalNames


def generate_continent(continent_list):
	seed = randint(0, 999999999)
	random.seed(seed)

	while True:
		if len(continent_list) == 0 or len(continent_list) is None:
			c_name = choice(continentalNames)
			break
		else:
			c_name = choice(continentalNames)
			if c_name in continent_list:
				c_name = ""
				c_name = choice(continentalNames)
			else:
				break


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
		region = generate_region()
		continent.add_region(region)


	return continent

