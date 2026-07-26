from dataclasses import dataclass
from uuid import UUID

@dataclass
class Biome():
	id: UUID
	name: str
	climate: str
	terrain: list
	temperature: int
	humidity: int
	elevation: int
	danger_level: int
	resources: list
	flora: list
	fauna: list
	settlement_type: list
	monsters: list

	def __str__(self) -> str:
		return (
			f"ID: {self.id}\n"
			f"Name: {self.name}\n"
			f"Climate: {self.climate}\n"
			f"Terrain: {self.terrain}\n"
			f"Temperature: {self.temperature}\n"
			f"Humidity: {self.humidity}\n"
			f"Elevation: {self.elevation}\n"
			f"Danger Level: {self.danger_level}\n"
			f"Resources: {self.resources}\n"
			f"Flora: {self.flora}\n"
			f"Fauna: {self.fauna}\n"
			f"Settlement Type: {self.settlement_type}\n"
			f"Monsters: {self.monsters}"
		)

	