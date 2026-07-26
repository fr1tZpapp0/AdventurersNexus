from dataclasses import dataclass
from uuid import UUID

@dataclass
class World():
	id: UUID
	name: str
	seed: int
	age: str
	continents: list
	oceans: list
	pantheon: list
	calendar: list
	

	def __str__(self) -> str:
		return (
			f"ID: {self.id}\n"
			f"World: {self.name}\n"
			f"Seed: {self.seed}\n"
			f"Age: {self.age}\n"
			f"Continents: {len(self.continents)}\n"
			f"Oceans: {len(self.oceans)}\n"
			f"Pantheon: {len(self.pantheon)}\n"
			f"Calendar: {len(self.calendar)}"
			)

	def add_continent(self, continent):
		return self.continents.append(continent)

	def add_oceans(self, ocean):
		return self.oceans.append(ocean)


