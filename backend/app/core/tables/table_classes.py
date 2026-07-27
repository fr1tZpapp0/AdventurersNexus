from dataclasses import dataclass

@dataclass
class Precious_Material:
	name: str
	rarity_percentage: float
	cost_per_pound: str
	strength: int
	purity: int


@dataclass
class Gemstone:
	name: str
	rarity_percentage: float
	cost_per_carat: str
	weight_per_carat: float





