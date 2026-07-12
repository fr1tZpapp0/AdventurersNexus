

def define_armor(cost, ac, mod, str_req, stealth, weight):
	_Armor = {
		"cost": f"{cost}gp",
		"ac": ac,
		"modifier": mod,
		"strength_requirement": str_req,
		"stealth_affected": stealth,
		"weight": weight
	}

	return _Armor

def define_weapon(cost, damage, weight, properties):
	_Weapon = {
		"cost": cost,
		"damage": damage,
		"weight": weight,
		"properties": properties
	}
	
	return _Weapon


# Light Armors
padded_Armor = define_armor(5, 11, "Dexterity", 0, "Disadvantage", 8)
leather_Armor = define_armor(10, 11, "Dexterity", 0, "No", 10)
studded_Leather_Armor = define_armor(45, 12, "Dexterity", 0, "No", 13)

# Medium Armors
hide_Armor = define_armor(10, 12, "Dexterity (Max of +2)", 0, "No", 12)
chain_Shirt_Armor = define_armor(50, 13, "Dexterity (Max of +2)", 0, "No", 20)
scale_Mail_Armor = define_armor(50, 14, "Dexterity (Max of +2)", 0, "Disadvantage", 45)
breastplate_Armor = define_armor(400, 14, "Dexterity (Max of +2)", 0, "No", 20)
half_Plate_Armor = define_armor(750, 15, "Dexterity (Max of +2)", 0, "Disadvantage", 40)

# Heavy Armors
ring_Mail_Armor = define_armor(30, 14, "No", 0, "Disadvantage", 40)
chain_Mail_Armor = define_armor(75, 16, "No", 13, "Disadvantage", 55)
splint_Armor = define_armor(200, 17, "No", 15, "Disadvantage", 60)
plate_Armor = define_armor(1500, 18, "No", 15, "Disadvantage", 65)

# Shields
shield_Armor = define_armor(10, "+2", "No", 0, "No", 6)



# Simple Melee Weapons
club = define_weapon("1sp", "1d4 Bludgeoning", 2, ["Light"])
dagger = define_weapon("2gp", "1d4 Piercing", 1, ["Finesse, Light", "Thrown (Range: 20/60)"])
greatclub = define_weapon("2sp", "1d8 Bludgeoning", 10, ["Two-Handed"])
handaxe = define_weapon("5gp", "1d6 Slashing", 2, ["Light", "Thrown (Range: 20/60)"])
javelin = define_weapon("5sp", "1d6 Piercing", 2, ["Thrown (Range: 20/60)"])
light_Hammer = define_weapon("2gp", "1d4 Bludgeoning", 2, ["Light, Thrown (Range: 20/60)"])
mace = define_weapon("5gp", "1d6 Bludgeoning", 4, [])
quarterstaff = define_weapon("2sp", "1d6 Bludgeoning", 4, ["Versatile (1d8)"])
sickle = define_weapon("1gp", "1d4 Slashing", 2, ["Light"])
spear = define_weapon("1gp", "1d6 Piercing", 3, ["Thrown (Range: 20/60)", "Versatile (1d8)"])

# Simple Ranged Weapons
light_Crossbow = define_weapon("25gp", "1d8 Piercing", 5, ["Ammunition (Range: 80/320", "Loading", "Two-Handed"])
dart = define_weapon("5cp", "1d4 Piercing", 0.25, ["Finesse, Thrown (Range: 20/60)"])
shortbow = define_weapon("25gp", "1d6 Piercing", 2, ["Ammunition (Range: 80/320)", "Two-Handed"])
sling = define_weapon("1sp", "1d4 Bludgeoning", 0, ["Ammunition (Range: 30/120)"])

# Martial Melee Weapons
battleaxe = define_weapon("10gp", "1d8 Slashing", 4, ["Versatile (1d10)"])
flail = define_weapon("10gp", "1d8 Bludgeoning", 2, [])
glaive = define_weapon("20gp", "1d10 Slashing", 6, ["Heavy", "Reach", "Two-Handed"])
greataxe = define_weapon("30gp", "1d12 Slashing", 7, ["Heavy", "Two-Handed"])
greatsword = define_weapon("50gp", "2d6 Slashing", 6, ["Heavy", "Two-Handed"])
halberd = define_weapon("20gp", "1d10 Slashing", 6, ["Heavy", "Reach", "Two-Handed"])
lance = define_weapon("10gp", "1d12 Piercing", 6, ["Reach", "Special"])
longsword = define_weapon("15gp", "1d8 Slashing", 3, ["Versatile (1d10)"])
maul = define_weapon("10gp", "2d6 Bludgeoning", 10, ["Heavy", "Two-Handed"])
morningstar = define_weapon("15gp", "1d8 Piercing", 4, [])
pike = define_weapon("5gp", "1d10 Piercing", 18, ["Heavy", "Reach", "Two-Handed"])
rapier = define_weapon("25gp", "1d8 Piercing", 2, ["Finesse"])
scimitar = define_weapon("25gp", "1d6 Slashing", 3, ["Finesse", "Light"])
shortsword = define_weapon("10gp", "1d6 Piercing", 2, ["Finesse", "Light"])
trident = define_weapon("5gp", "1d6 Piercing", 4, ["Thrown (20/60)", "Versatile (1d8)"])
war_Pick = define_weapon("5gp", "1d8 Piercing", 2, [])
warhammer = define_weapon("15gp", "1d8 Bludgeoning", 2, ["Versatile (1d8)"])
whip = define_weapon("2gp", "1d4 Slashing", 3, ["Finesse, Reach"])

# Martial Ranged Weapons
blowgun = define_weapon("10gp", "1 Piercing", 1, ["Ammunition (Range: 25/100)", "Loading"])
hand_Crossbow = define_weapon("75gp", "1d6Piercing", 3, ["Ammunition (Range: 30/120)", "Light", "Loading"])
heavy_Crossbow = define_weapon("50gp", "1d10 Piercing", 18, ["Ammunition (Range:100/400)", "Heavy", 
	"Loading", "Two-Handed"])
longbow = define_weapon("50gp", "1d8 Piercing", 2, ["Ammunition (Range: 150/600)", "Heavy", "Two-Handed"])
net = define_weapon("1gp", 0, 3, ["Special", "Thrown (Range: 5/15)"])



armors_list = {
	"Light Armor": [padded_Armor, leather_Armor, studded_Leather_Armor],
	"Medium Armor": [hide_Armor, chain_Shirt_Armor, scale_Mail_Armor, breastplate_Armor, half_Plate_Armor],
	"Heavy Armor": [ring_Mail_Armor, chain_Mail_Armor, splint_Armor, plate_Armor],
	"Shields": shield_Armor
}

weapons_list = {
	"Simple Melee": [
		club, 
		dagger, 
		greatclub, 
		handaxe, 
		javelin, 
		light_Hammer, 
		mace, 
		quarterstaff, 
		sickle, 
		spear, 
		"Unarmed Strike: 1 Bludgeoning"
	],

	"Simple Ranged": [
		light_Crossbow, 
		dart, 
		shortbow, 
		sling
	],
	
	"Martial Melee": [
		battleaxe,
		flail,
		glaive,
		greataxe,
		greatsword,
		halberd,
		lance,
		longsword,
		maul,
		morningstar,
		pike,
		rapier,
		scimitar,
		shortsword,
		trident,
		war_Pick,
		warhammer,
		whip
	],

	"Martial Ranged": [
		blowgun, 
		hand_Crossbow, 
		heavy_Crossbow, 
		longbow, 
		net
	]
}

