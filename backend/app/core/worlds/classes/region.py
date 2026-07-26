from dataclasses import dataclass
from uuid import UUID
from .biome import Biome


@dataclass
class Region():
	id: UUID
	seed: int
	name: str
	biome: Biome
	settlements: list
	dungeons: list
	caves: list
	roads: list
	landmarks: list
	weather: list


	def __str__(self) -> str:
		return (
			f"ID: {self.id}\n"
			f"Seed: {self.seed}\n"
			f"Name: {self.name}\n"
			f"Biome: {self.biome}\n"
			f"Settlements: {self.settlements}\n"
			f"Dungeons: {self.dungeons}\n"
			f"Caves: {self.caves}\n"
			f"Roads: {self.roads}\n"
			f"Landmarks: {self.landmarks}\n"
			f"Weather: {self.weather}"
		)

	def add_settlement(self, settlement):
		return self.settlements.append(settlement)



	