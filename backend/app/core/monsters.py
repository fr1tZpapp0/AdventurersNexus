from dataclasses import dataclass


cr0_monsters = [
	"Awakened Shrub",
	"Baboon",
	"Badger",
	"Bat",
	"Cat",
	"Commoner",
	"Crab",
	"Deer",
	"Eagle",
	"Frog",
	"Giant Fire Beetle",
	"Goat",
	"Hawk",
	"Homunculus",
	"Hyena",
	"Jackal",
	"Lemure",
	"Lizard",
	"Octopus",
	"Owl",
	"Quipper",
	"Rat",
	"Raven",
	"Scorpion",
	"Sea Horse",
	"Shrieker",
	"Spider",
	"Vulture",
	"Weasel"
]

cr0125_monsters = [
	"Bandit",
	"Blood Hawk",
	"Camel",
	"Cultist",
	"Flying Snake",
	"Giant Crab",
	"Giant Rat",
	"Giant Weasel",
	"Guard",
	"Kobold",
	"Mastiff",
	"Merfolk",
	"Mule",
	"Noble",
	"Poisonous Snake",
	"Pony",
	"Stirge",
	"Tribal Warrior"
]

cr025_monsters = [
	"Acolyte",
	"Axe Beak",
	"Blink Dog",
	"Boar",
	"Constrictor Snake",
	"Draft Horse",
	"Dretch",
	"Elf, Drow",
	"Elk",
	"Flying Sword",
	"Giant Badger",
	"Giant Bat",
	"Giant Centipede",
	"Giant Frog",
	"Giant Lizard",
	"Giant Owl",
	"Giant Poisonous Snake",
	"Giant Wolf Spider",
	"Goblin",
	"Grimlock",
	"Panther",
	"Pseudodragon",
	"Riding Horse",
	"Skeleton",
	"Sprite",
	"Steam Mephit",
	"Swarm of Bats",
	"Swarm of Rats",
	"Swarm of Ravens",
	"Violet Fungus",
	"Wolf",
	"Zombie"
]

cr05_monsters = [
	"Ape"
	"Black bear"
	"Cockatrice"
	"Crocodile"
	"Darkmantle"
	"Dust Mephit"
	"Giant Goat"
	"Giant Sea Horse"
	"Giant Wasp"
	"Gnoll"
	"Gnome, Deep (Svirfneblin)"
	"Gray Ooze"
	"Hobgoblin"
	"Ice Mephit"
	"Lizardfolk"
	"Magma Mephit"
	"Magmin"
	"Orc"
	"Reef Shark"
	"Rust Monster"
	"Sahuagin"
	"Satyr"
	"Scout"
	"Shadow"
	"Swarm of Insects"
	"Thug"
	"Warhorse"
	"Warhorse Skeleton"
	"Worg"
]

cr1_monsters = [
	"Animated Armor"
	"Brass Dragon Wyrmling"
	"Brown Bear"
	"Bugbear"
	"Copper Dragon Wyrmling"
	"Death Dog"
	"Dire Wolf"
	"Dryad"
	"Duergar"
	"Ghoul"
	"Giant Eagle"
	"Giant Hyena"
	"Giant Octopus"
	"Giant Spider"
	"Giant Toad"
	"Giant Vulture"
	"Harpy"
	"Hippogriff"
	"Imp"
	"Lion"
	"Quasit"
	"Specter"
	"Spy"
	"Swarm of Quippers"
	"Tiger"
]





@dataclass
class Monster():
	name: str
	mon_type: str
	mon_alignment: str
	mon_special_tag: str

	mon_size: str
	mon_ac: int
	mon_hp: int
	mon_speeds: dict

	mon_stats: dict
	mon_immunities: list[str]
	mon_resistances: list[str]
	mon_vulnerabilities: list[str]
	mon_senses: dict
	mon_languages: dict
	mon_cr: int
	
	mon_actions: dict
	mon_reactions: dict








