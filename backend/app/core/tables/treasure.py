from .table_classes import Precious_Material
from .table_classes import Gemstone

# Gems are found in the link below:
# https://www.dndbeyond.com/equipment?filter-search=gem&filter-cost-min=&filter-cost-max=&filter-weight-min=&filter-weight-max=&sort=cost

# Precious Materials are found at:
# NOTE: Precious Metals are harder to have accurate pricing
# https://olddungeonmaster.com/2016/12/02/dd-5e-metals/

Azurite = Gemstone(
	name="Azurite",
	rarity_percentage=90,
	cost_per_carat="10 gp",
	weight_per_carat=0.1
)

Banded_Agate = Gemstone(
	name="Banded Agate",
	rarity_percentage=90,
	cost_per_carat="10 gp",
	weight_per_carat=0.1
)

Blue_Quartz = Gemstone(
	name="Blue Quartz",
	rarity_percentage=90,
	cost_per_carat="10 gp",
	weight_per_carat=0.1
)

Eye_Agate = Gemstone(
	name="Eye Agate",
	rarity_percentage=90,
	cost_per_carat="10 gp",
	weight_per_carat=0.1
)


PRECIOUS_GEMS = [
	Azurite,
	Banded_Agate,
	Blue_Quartz,
	Eye_Agate
]


