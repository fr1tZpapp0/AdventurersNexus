from dataclasses import dataclass
from random import randint, choice

races = [
	"Aarakocra",
	"Aasimar",
	"Astral Elf",
	"Autognome",
	"Bugbear",
	"Centaur",
	"Changeling",
	"Deep Gnome",
	"Dragonborn",
	"Drow Elf",
	"Duergar",
	"Eladrin",
	"Fairy",
	"Forest Gnome",
	"Firbolg",
	"Genasi - Air",
	"Genasi - Earth",
	"Genasi - Fire",
	"Genasi - Water",
	"Giff",
	"Githyanki",
	"Githzerai",
	"Goblin",
	"Goliath",
	"Hadozee",
	"Half-Elf",
	"Half-Orc",
	"Harengon",
	"High Elf"
	"Hill Dwarf",
	"Hobgoblin",
	"Human",
	"Kenku",
	"Kobold",
	"Lightfoot Halfling"
	"Lizardfolk",
	"Loxodon",
	"Minotaur",
	"Mountain Dwarf"
	"Orc",
	"Plasmoid"
	"Rock Gnome"
	"Satyr",
	"Sea Elf",
	"Shadar-Kai",
	"Shifter",
	"Simic Hybrid",
	"Stout Halfling",
	"Tabaxi",
	"Thri-kreen",
	"Tiefling"
	"Tortle",
	"Triton",
	"Vedalken",
	"Wood Elf",
	"Yuan-Ti"
]

Dragonborn_Colors = {
	"Black": "Acid",
	"Blue": "Lightning",
	"Brass": "Fire",
	"Bronze": "Lightning",
	"Copper": "Acid",
	"Gold": "Fire",
	"Green": "Poison",
	"Red": "Fire",
	"Silver": "Cold",
	"White": "Cold",
	"Amethyst": "Force",
	"Crystal": "Radiant",
	"Emerald": "Psychic",
	"Sapphire": "Thunder",
	"Topaz": "Necrotic"
}

classes = [
	"Artificer",
	"Barbarian",
	"Bard",
	"Cleric",
	"Druid",
	"Fighter",
	"Monk",
	"Paladin",
	"Ranger",
	"Rogue"
	"Sorcerer",
	"Warlock",
	"Wizard"
]




@dataclass
class Character:
	name: str
	race: str
	class_type: str
	subclass: str
	level: int
	background: str
	size: int
	speed: int
	ac: int
	hp_max:	int
	hp_current:	int
	hp_temp: int
	proficiency_bonus: int
	initiative: int
	hit_dice_max: str
	hit_dice_spent: str

	languages: list
	alignment: str

	copper_pieces: int
	silver_pieces: int
	gold_pieces: int
	electrum_pieces: int
	platinum_pieces: int

	passive_perception: int
	weapons_and_damages: list
	equipment: list
	profiencies: list
	class_features: list
	racial_features: list
	feats: list

	spell_mod: int
	spell_save_dc: int
	spell_attack_bonus: int

	known_spells: dict
	spell_slots: dict

	stat_STR: int
	stat_DEX: int
	stat_CON: int
	stat_INT: int
	stat_WIS: int
	stat_CHA: int

	mod_STR: int
	mod_DEX: int
	mod_CON: int
	mod_INT: int
	mod_WIS: int
	mod_CHA: int

	saving_throw_STR: int
	saving_throw_DEX: int
	saving_throw_CON: int
	saving_throw_INT: int
	saving_throw_WIS: int
	saving_throw_CHA: int

	skills: dict


