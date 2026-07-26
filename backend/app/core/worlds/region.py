from dataclasses import dataclass

@dataclass
class Region():
	id: int
	biome: list
	settlements: list
	dungeons: list
	caves: list
	roads: list
	landmarks: list
	weather: list


