from app.core.cards.card import Card
from random import randint, sample

Red_Dragon = Card(
	name="Red Dragon",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Knight_4_Guards = Card(
	name="Knight & 4 Guards",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Druid = Card(
	name="Druid",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Cloud_Giant = Card(
	name="Cloud Giant",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Ettin = Card(
	name="Ettin",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Bugbear = Card(
	name="Bugbear",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Goblin = Card(		# 2 COPIES
	name="Goblin",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Archmage_Apprentice = Card(
	name="Archmage & Apprentice",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Ogre_Mage = Card(
	name="Ogre Mage",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Gnoll = Card(
	name="Gnoll",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Kobold = Card(		# 2 COPIES
	name="Kobold",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Lich = Card(
	name="Lich",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Priest_Acolyte = Card(
	name="Priest & 2 Acolytes",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Medusa = Card(
	name="Medusa",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Veteran = Card(
	name="Veteran",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Frost_Giant = Card(
	name="Frost Giant",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Troll = Card(
	name="Troll",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Hobgoblin = Card(
	name="Hobgoblin",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Iron_Golem = Card(
	name="Iron Golem",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Bandit_Captain_Bandits = Card(
	name="Bandit Captain & 3 Bandits",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Berserker = Card(
	name="Berserker",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Hill_Giant = Card(
	name="Hill Giant",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Ogre = Card(
	name="Ogre",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Orc = Card(
	name="Orc",
	description="",
	returnToDeck=False,
	in13Deck=False
)

You_Owner = Card(
	name="You (Deck's Owner)",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Succubus_Incubus = Card(
	name="Succubus  / Incubus",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Beholder = Card(
	name="Beholder",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Assassin = Card(
	name="Assassin",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Erinyes = Card(
	name="Erinyes",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Night_Hag = Card(
	name="",
	description="",
	returnToDeck=False,
	in13Deck=False
)

Fire_Giant = Card(
	name="",
	description="",
	returnToDeck=False,
	in13Deck=False
)



ALL_DOI_CARDS = [
	Red_Dragon,
	Knight_4_Guards,
	Druid,
	Cloud_Giant,
	Ettin,
	Bugbear,
	Goblin,
	Goblin,
	Archmage_Apprentice,
	Ogre_Mage,
	Gnoll,
	Kobold,
	Kobold,
	Lich,
	Priest_Acolyte,
	Medusa,
	Veteran,
	Frost_Giant,
	Troll,
	Hobgoblin,
	Iron_Golem,
	Bandit_Captain_Bandits,
	Berserker,
	Hill_Giant,
	Ogre,
	Orc,
	You_Owner,
	You_Owner,
	Succubus_Incubus,
	Beholder,
	Assassin,
	Erinyes,
	Night_Hag,
	Fire_Giant
]

def get_DOI_Cards():
	sizeMinus = randint(1, 20)
	sizeMinus -= 1

	cardCount = len(ALL_DOI_CARDS) - sizeMinus

	cards = sample(ALL_DOI_CARDS, cardCount)
	return cards

