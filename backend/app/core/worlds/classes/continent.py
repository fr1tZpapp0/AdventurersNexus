from dataclasses import dataclass
from uuid import UUID

@dataclass
class Continent():
	id: UUID
	name: str
	seed: int
	regions: list
	mountain_ranges: list
	rivers: list
	climate: list
	size: int


	def __str__(self) -> str:
			return (
				f"ID: {self.id}\n"
				f"World: {self.name}\n"
				f"Seed: {self.seed}\n"
				f"Regions: {self.regions}\n"
				f"Mountain Ranges: {len(self.mountain_ranges)}\n"
				f"Rivers: {len(self.rivers)}\n"
				f"Climate: {len(self.climate)}\n"
				f"Size: {self.size}"
				)


	def add_region(self, region):
		return self.regions.append(region)

	