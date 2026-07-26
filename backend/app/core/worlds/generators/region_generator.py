import random
from uuid import uuid4
from random import choice, randint
from ..region import Region
from ..biome import Biome
from ..names.biome_names import biomeSpecializer, biomeTypes
from .settlement_generator import generate_settlement


def generate_region():
	seed = randint(0, 999999999)
	random.seed(seed)


	bSpecial = choice(biomeSpecializer)
	bType = choice(biomeTypes)
	biomeName = f"{bSpecial} {bType}"


	biome = Biome(
		id=uuid4(),
		name=biomeName,
		climate=bSpecial,
		terrain=[],
		temperature=randint(-10, 110),
		humidity=randint(1, 100),
		elevation=randint(500, 5272),
		danger_level=randint(0, 15),
		resources=[],
		flora=[],
		fauna=[],
		settlement_type=[],
		monsters=[]
	)



	region = Region(
		id=uuid4(),
		seed=seed,
		biome=biome,
		settlements=[],
		dungeons=[],
		caves=[],
		roads=[],
		landmarks=[],
		weather=[]
	)


	

	for i in range(2):
		settlement = generate_settlement(region.settlements)
		region.add_settlement(settlement)

	return region


