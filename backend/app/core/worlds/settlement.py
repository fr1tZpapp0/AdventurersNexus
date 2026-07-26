from dataclasses import dataclass
from uuid import UUID


@dataclass
class Settlement():
	id: UUID
	seed: int
	name: str
	style: list
	population: int
	government: list
	shops: list
	npcs: list
	taverns: list
	quests: list

	def __str__(self) -> str:
		return (
			f"ID: {self.id}\n"
			f"Seed: {self.seed}\n"
			f"Name: {self.name}\n"
			f"Settlement Style: {self.style}\n"
			f"Population: {self.population}\n"
			f"Government: {self.government}\n"
			f"Shops: {self.shops}\n"
			f"NPCS: {self.npcs}\n"
			f"Taverns: {self.taverns}\n"
			f"Quests: {self.quests}"
		)