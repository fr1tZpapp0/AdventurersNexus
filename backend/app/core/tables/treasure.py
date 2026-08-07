from .table_classes import Precious_Material
from .table_classes import Gemstone

# Gems are found in the link below:
# https://www.dndbeyond.com/equipment?filter-search=gem&filter-cost-min=&filter-cost-max=&filter-weight-min=&filter-weight-max=&sort=cost

# Precious Materials are found at:
# NOTE: Precious Metals are harder to have accurate pricing
# https://olddungeonmaster.com/2016/12/02/dd-5e-metals/
# The STRENGTH attribute of the precious materials is also the materials
#		natural AC

Adamantine = Precious_Material(
	name="Adamantine",
	rarity_percentage=0.06,
	cost_per_pound="5,000 gp",
	strength=23,
	purity=100
)

Brass = Precious_Material(
	name="Brass",
	rarity_percentage=52,
	cost_per_pound="3 sp",
	strength=16,
	purity=100
)

Bronze = Precious_Material(
	name="Bronze",
	rarity_percentage=73,
	cost_per_pound="4 sp",
	strength=18,
	purity=100
)

Cold_Iron = Precious_Material(
	name="Cold Iron",
	rarity_percentage=73,
	cost_per_pound="4 sp",
	strength=20,
	purity=100
)

Copper = Precious_Material

Electrum = Precious_Material

Gold = Precious_Material

Iron = Precious_Material

Lead = Precious_Material

Mithral = Precious_Material

Platinum = Precious_Material

Silver = Precious_Material

Steel = Precious_Material

Tin = Precious_Material





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

Hematite = Gemstone(
	name="Hematite",
	rarity_percentage=90,
	cost_per_carat="10 gp",
	weight_per_carat=0.1
)

Lapis_Lazuli = Gemstone(
	name="Lapis Lazuli",
	rarity_percentage=72,
	cost_per_carat="10 gp",
	weight_per_carat=0.1
)

Malachite = Gemstone(
	name="Malachite",
	rarity_percentage=72,
	cost_per_carat="10 gp",
	weight_per_carat=0.1
)

Moss_Agate = Gemstone(
	name="Moss Agate",
	rarity_percentage=72,
	cost_per_carat="10 gp",
	weight_per_carat=0.1
)

Obsidian = Gemstone(
	name="Obsidian",
	rarity_percentage=72,
	cost_per_carat="10 gp",
	weight_per_carat=0.1
)

Rhodochrosite = Gemstone(
	name="Rhodochrosite",
	rarity_percentage=72,
	cost_per_carat="10 gp",
	weight_per_carat=0.1
)

Tiger_Eye = Gemstone(
	name="Tiger Eye",
	rarity_percentage=72,
	cost_per_carat="10 gp",
	weight_per_carat=0.1
)

Turquoise = Gemstone(
	name="Turquoise",
	rarity_percentage=72,
	cost_per_carat="10 gp",
	weight_per_carat=0.1
)

Bloodstone = Gemstone(
	name="Bloodstone",
	rarity_percentage=84,
	cost_per_carat="50 gp",
	weight_per_carat=0.1
)


PRECIOUS_GEMS = [
	Azurite,
	Banded_Agate,
	Blue_Quartz,
	Eye_Agate,
	Hematite,
	Lapis_Lazuli,
	Malachite,
	Moss_Agate,
	Obsidian,
	Rhodochrosite,
	Tiger_Eye,
	Turquoise,
	Bloodstone
]


PRECIOUS_MATERIALS = [

]