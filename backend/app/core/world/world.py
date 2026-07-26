from dataclasses import dataclass

@dataclass
class World():
	id: int
	name: str
	continents: list
	oceans: list
	pantheon: list
	calendar: list
	age: int
	seed: int


def add_continent():
	return "Continent"