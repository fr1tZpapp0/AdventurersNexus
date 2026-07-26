from dataclasses import dataclass

@dataclass
class Continent():
	id: int
	name: str
	regions: list
	mountain_ranges: list
	rivers: list
	climate: list
	size: int
