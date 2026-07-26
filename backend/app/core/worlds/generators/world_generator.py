import random, uuid
from world import World
from names.world_names import world_names
from names.world_ages import world_ages




def generate_world():
	seed = random.randint(0, 999999999)
	random.seed(seed)

	world = World(
		id=uuid.uuid4(),
		name=random.choice(world_names),
		seed=seed,
		age=random.choice(world_ages),
		continents=[],
		oceans=[],
		pantheon=[],
		calendar=[]
	)


	return world
