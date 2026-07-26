from dataclasses import dataclass
from random import Random

@dataclass
class GenerationContext:
	rng: Random
	available_settlement_names: list[str]
	available_region_names: list[str]
	available_continent_names: list[str]
	available_world_names: list[str]
	world_seed: int

