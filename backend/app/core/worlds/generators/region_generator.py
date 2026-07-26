import random
from uuid import uuid4
from random import choice, randint


from ..classes.region import Region
from ..classes.biome import Biome
from ..classes.generator import GenerationContext


from ..data.Biome.biome_data import BIOME_TYPE



from .settlement_generator import generate_settlement


def generate_region(context: GenerationContext):
	biome_seed = randint(0, 999999999)
	random.seed(biome_seed)


	b_rng = random.Random(biome_seed)

	biomeType = b_rng.choice(list(BIOME_TYPE.keys()))
	biomeData = BIOME_TYPE[biomeType]

	biome = Biome(
		id=uuid4(),
		seed=biome_seed,
		biome_type=biomeType,
		specializer=b_rng.choice(biomeData["Specializers"]),
		temperature=(0, 0),
		humidity=0,
		danger_level=0,
		flora=[],
		fauna=[],
		monsters=[],
		resources=[]
	)

	region_seed = randint(0, 999999999)
	random.seed(region_seed)


	r_name = context.available_region_names.pop(context.rng.randrange(len(context.available_region_names)))


	region = Region(
		id=uuid4(),
		seed=region_seed,
		name=r_name,
		biome=biome,
		settlements=[],
		dungeons=[],
		caves=[],
		roads=[],
		landmarks=[],
		weather=[]
	)

	number_of_settlements = context.rng.randint(1, 5)
	for _ in range(number_of_settlements):
		settlement = generate_settlement(context)
		region.add_settlement(settlement)



	return region


