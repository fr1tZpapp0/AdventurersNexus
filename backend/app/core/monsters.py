from dataclasses import dataclass

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
	mon_mods: dict
	mon_immunities: list[str]
	mon_resistances: list[str]
	mon_vulnerabilities: list[str]
	mon_senses: dict
	mon_languages: dict
	mon_cr: int
	
	mon_actions: dict
	mon_reactions: dict




Awakened_Shrub = Monster(
	name="Awakened Shrub",
	mon_type="Plant",
	mon_alignment="Unaligned",
	mon_special_tag="",
	mon_size="Small",
	mon_ac=9,
	mon_hp=10,
	mon_speeds={
		"Walking Speed": 20
	},
	mon_stats={
		"STR": 3,
		"DEX": 8,
		"CON": 11,
		"INT": 10,
		"WIS": 10,
		"CHA": 6
	},
	mon_mods={
		"STR": -4,
		"DEX": -1,
		"CON": 0,
		"INT": 0,
		"WIS": 0,
		"CHA": -2
	},
	mon_immunities=[],
	mon_resistances=["Piercing"],
	mon_vulnerabilities=["fire"],
	mon_senses={
		"Passive Perception": 10
	},
	mon_languages={
		"One language know by its creator": "Understands"
	},
	mon_cr=0,
	mon_actions={
		"Rake": {
			"To Hit": 1,
			"Reach (in ft)": 5,
			"Target": 1,
			"Hit": "1d4-1 slashing damage"
		},
		"False Appearance": {
			"Ability": "While the shrub, given sentience and mobility by the awaken spell or similar magic"
		}
	},
	mon_reactions={}
)

Baboon = Monster(
	name="Baboon",
	mon_type="Beast",
	mon_alignment="Unaligned",
	mon_special_tag="",
	mon_size="Small",
	mon_ac=12,
	mon_hp=3,
	mon_speeds={
		"Walking": 30,
		"Climbing": 30
	},
	mon_stats={
		"STR": 8,
		"DEX": 14,
		"CON": 11,
		"INT": 4,
		"WIS": 12,
		"CHA": 6
	},
	mon_mods={
		"STR": -1,
		"DEX": 2,
		"CON": 0,
		"INT": -3,
		"WIS": 1,
		"CHA": -2
	},
	mon_immunities=[],
	mon_resistances=[],
	mon_vulnerabilities=[],
	mon_senses={},
	mon_languages={"Passive Perception": 11},
	mon_cr=0,
	mon_actions={
		"Bite": {
			"Melee Weapon Attack": 1,
			"Reach": 5,
			"Target": 1,
			"Hit": "1d4-1 Piercing Damage"
		},
		"Pack Tactics": """The baboon has advantage on an attack roll against a creature if at least one of the baboon's allies 
		is within 5 feet of the creature and the ally isn't incapacitated."""
	},
	mon_reactions={}
)

Badger = Monster(
	name="Badger",
	mon_type="Beast"
)



cr0_monsters = [
	Awakened_Shrub,
	Baboon,
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

cr2_monsters = [
	"Ankheg",
	"Awakened Tree",
	"Azer",
	"Bandit Captain",
	"Berserker",
	"Black Dragon Wyrmling",
	"Bronze Dragon Wyrmling",
	"Centaur",
	"Cult Fanatic",
	"Druid",
	"Ettercap",
	"Gargoyle",
	"Gelatinous Cube",
	"Ghast",
	"Giant Boar",
	"Giant Constrictor Snake",
	"Giant Elk",
	"Gibbering Mouther",
	"Green Dragon Wyrmling",
	"Grick",
	"Griffon",
	"Hunter Shark",
	"Merrow",
	"Mimic",
	"Minotaur Skeleton",
	"Ochre Jelly",
	"Ogre",
	"Ogre Zombie",
	"Pegasus",
	"Plesiosaurus",
	"Polar Bear",
	"Priest",
	"Rhinoceros",
	"Rug of Smothering",
	"Saber-Toothed Tiger",
	"Sea Hag",
	"Silver Dragon Wyrmling",
	"Swarm of Poisonous Snakes",
	"Wererat",
	"White Dragon Wyrmling",
	"Will-o'-Wisp"
]

cr3_monsters = [
	"Basilisk",
	"Bearded Devil",
	"Blue Dragon Wyrmling",
	"Doppelganger",
	"Giant Scorpion",
	"Gold Dragon Wyrmling",
	"Green Hag",
	"Hell Hound",
	"Killer Whale",
	"Knight",
	"Manticore",
	"Minotaur",
	"Mummy",
	"Nightmare",
	"Owlbear",
	"Phase Spider",
	"Veteran",
	"Werewolf",
	"Wight",
	"Winter Wolf"	
]

cr4_monsters = [
	"Black Pudding",
	"Chuul",
	"Couatl",
	"Elephant",
	"Ettin",
	"Ghost",
	"Lamia",
	"Red Dragon Wyrmling",
	"Succubus/Incubus",
	"Wereboar",
	"Weretiger"
]

cr5_monsters = [
	"Air Elemental",
	"Barbed Devil",
	"Bulette",
	"Earth Elemental",
	"Fire Elemental",
	"Flesh Golem",
	"Giant Crocodile",
	"Giant Shark",
	"Gladiator",
	"Gorgon",
	"Half-Red Dragon Veteran",
	"Hill Giant",
	"Night Hag",
	"Otyugh",
	"Roper",
	"Salamander",
	"Shambling Mound",
	"Triceratops",
	"Troll",
	"Unicorn",
	"Vampire Spawn",
	"Water Elemental",
	"Werebear",
	"Wraith",
	"Xorn"
]

cr6_monsters = [
	"Chimera",
	"Drider",
	"Invisible Stalker",
	"Mage",
	"Mammoth",
	"Medusa",
	"Vrock",
	"Wyvern",
	"Young Brass Dragon",
	"Young White Dragon"
]

cr7_monsters = [
	"Giant Ape",
	"Oni",
	"Shield Guardian",
	"Stone Giant",
	"Young Black Dragon",
	"Young Copper Dragon"
]

cr8_monsters = [
	"Assassin",
	"Chain Devil",
	"Cloaker",
	"Frost Giant",
	"Hezrou",
	"Hydra",
	"Spirit Naga",
	"Tyrannosaurus Rex",
	"Young Bronze Dragon",
	"Young Green Dragon"
]

cr9_monsters = [
	"Bone Devil",
	"Clay Golem",
	"Cloud Giant",
	"Fire Giant",
	"Glabrezu",
	"Treant",
	"Young Blue Dragon",
	"Young Silver Dragon"
]

cr10_monsters = [
	"Aboleth",
	"Deva",
	"Guardian Naga",
	"Stone Golem",
	"Young Gold Dragon",
	"Young Red Dragon"
]

cr11_monsters = [
	"Behir",
	"Djinni",
	"Efreeti",
	"Gynosphinx",
	"Horned Devil",
	"Remorhaz",
	"Roc"
]

cr12_monsters = [
	"Archmage",
	"Erinyes"
]

cr13_monsters = [
	"Adult Brass Dragon",
	"Adult White Dragon",
	"Nalfeshnee",
	"Rakshasa",
	"Storm Giant",
	"Vampire"
]

cr14_monsters = [
	"Adult Black Dragon",
	"Adult Copper Dragon",
	"Ice Devil"
]

cr15_monsters = [
	"Adult Bronze Dragon",
	"Adult Green Dragon",
	"Mummy Lord",
	"Purple Worm"
]

cr16_monsters = [
	"Adult Blue Dragon",
	"Adult Silver Dragon",
	"Iron Golem",
	"Marilith",
	"Planear"
]

cr17_monsters = [
	"Adult Gold Dragon",
	"Aduult Red Dragon",
	"Androsphinx",
	"Dragon Turtle"
]

cr19_monsters = [
	"Balor"
]

cr20_monsters = [
	"Ancient Brass Dragon",
	"Ancient White Dragon",
	"Pit Fiend"
]

cr21_monsters = [
	"Ancient Black Dragon",
	"Ancient Copper Dragon",
	"Lich",
	"Solar"
]

cr22_monsters = [
	"Ancient Bronze Dragon",
	"Ancient Green Dragon"
]

cr23_monsters = [
	"Ancient Blue Dragon",
	"Ancient Silver Dragon",
	"Kraken"
]

cr24_monsters = [
	"Ancient Gold Dragon",
	"Ancient Red Dragon"
]

cr30_monsters = [
	"Tarrasque"
]


