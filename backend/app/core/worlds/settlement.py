from dataclasses import dataclass

@dataclass
class Settlement():
	id: int
	name: str
	population: int
	government: list
	shops: list
	npcs: list
	taverns: list
	quests: list

