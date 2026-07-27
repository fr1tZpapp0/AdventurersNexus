from dataclasses import dataclass
from uuid import UUID

@dataclass
class Dungeon:
	id: UUID
	name: str
	seed: int
	total_size: tuple[int, int]
	room_amount: int
	dungeon_dressings: list
	monsters: list
	loot: list

	def __str__(self) -> str:
		return (
			f"ID: {self.id}\n"
			f"Name: {self.name}\n"
			f"Seed: {self.seed}\n"
			f"Total Size: {self.total_size}\n"
			f"Amount of Rooms: {self.room_amount}\n"
			f"Dungeon Dressings: {self.dungeon_dressings}\n"
			f"Monsters: {self.monsters}\n"
			f"Loot: {self.loot}"
		)


		