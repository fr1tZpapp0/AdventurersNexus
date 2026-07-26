from dataclasses import dataclass
from uuid import UUID

@dataclass
class Biome():
	id: UUID
	seed: int

	biome_type: str
	specializer: str

	temperature: tuple[int, int]
	humidity: int

	danger_level: int

	flora: list[str]
	fauna: list[str]
	monsters: list[str]
	resources: list[str]


	def __str__(self) -> str:
		return (
			f"ID: {self.id}\n"
			f"Seed: {self.seed}\n"
			f"Biome Type: {self.biome_type}\n"
			f"Biome Specializer: {self.specializer}\n"
			f"Temperature: {self.temperature}\n"
			f"Humidity: {self.humidity}"
		)



	@property
	def name(self) -> str:
		return f"{self.specializer} {self.biome_type}"

	