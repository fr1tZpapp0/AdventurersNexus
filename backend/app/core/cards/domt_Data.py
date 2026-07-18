from app.core.cards.card import Card


Balance_Desc = """Your mind suffers a wrenching alteration, causing your alignment to change. Lawful becomes chaotic, 
good becomes evil, and vice versa. If you are true neutral or unaligned, this card has no effect on you."""

Comet_Desc = """If you single-handedly defeat the next hostile monster or group of monsters you encounter, you gain 
experience points enough to gain one level. Otherwise, this card has no effect."""

Donjon_Desc = """You disappear and become entombed in a state of suspended animation in an extradimensional sphere. 
Everything you're wearing and carrying disappears with you except for Artifacts, which stay behind in the space you 
occupied when you disappeared. You remain imprisoned until you are found and removed from the sphere. You can't 
be located by any Divination magic, but a Wish spell can reveal the location of your prison. You draw no more cards."""

Euryale_desc = """The card's medusa-like visage curses you. You take a -2 penalty to saving throws while cursed in this 
way. Only a god or the magic of the Fates card can end this curse."""

Fates_desc = """Reality's fabric unravels and spins anew, allowing you to avoid or erase one event as if it never happened. 
You can use the card's magic as soon as you draw the card or at any other time before you die."""

Flames_desc = """A powerful devil becomes your enemy. The devil seeks your ruin and torments you, savoring your suffering 
before attempting to slay you. this enmity lasts until either you or the devil dies."""

Fool_desc = """You lose 10,000 XP, discard this card, and draw from the deck again, counting both draws as one 
of your declared draws. If losing that much XP would cause you to lose a level, you instead lose an amount that 
leaves you with just enough XP to keep your level."""

Gem_desc = """Twenty-five pieces of jewelry worth 2,000 GP each or fifty gems worth 1,000 GP each appear at your feet."""

Idiot_desc = """Permanently reduce your Intelligence by 1d4 + 1 (to a minimum score of 1). You can draw one 
additional card beyond your declared draws."""

Jester_desc = """You gain 10,000 XP, or you can draw two additional cards beyond your declared draws."""

Key_desc = """A Rare or rarer magic weapon with which you are proficient appears on your person. The DM chooses the weapon."""

Knight_desc = """You gain the service of a 4th-level fighter who appears in a space you choose within 30 feet of you. 
The fighter is of the same race as you and serves you loyally until death, believing the fates have drawn him or 
her to you. You control this character."""

Moon_desc = """You gain the ability to cast Wish 1d3 times. (Roll 1d6. Divide the result by 2, rounding up.)"""

Rogue_desc = """An NPC of the DM's choice becomes Hostile toward you. You don't know the identity of this NPC until they 
or someone else reveals it. Nothing less than divine intervention can end the NPC's hostility toward you."""

Ruin_desc = """All forms of wealth that you carry or own, other than magic items, are lost to you. Portable property vanishes. 
Businesses, buildings, and land you own are lost in a way that alters reality the least. If you have a Bastion, it is 
destroyed by some calamity beyond your control. Any documentation that proves you should own something lost to this card 
also disappears."""

Skull_desc = """An Avatar of Death appears in an unoccupied space as close to you as possible. The avatar targets only 
you with its attacks, appearing as a ghostly skeleton clad in a tattered black robe and carrying a spectral scythe. 
The avatar disappears when it drops to 0 Hit Points or you die. If an ally of yours deals damage to the avatar, that 
ally summons another Avatar of Death. The new avatar appears in an unoccupied space as close to that ally as possible 
and targets only that ally with its attacks. You and your allies can each summon only one avatar as a consequence of 
this draw. A creature slain by an avatar can't be restored to life."""

Star_desc = """Increase one of your ability scores by 2, to a maximum of 24."""

Sun_desc = """You gain 50,000 XP, and a wondrous item (which the DM determines randomly) appears in your hands."""

Talons_desc = """Every magic item you wear or carry disintegrates. Artifacts in your possession vanish instead."""

Throne_desc = """You gain Proficiency and Expertise in your choice of History, Insight, Intimidation, or Persuasion. 
In addition, you gain rightful ownership of a small keep somewhere in the world. However, the keep is currently 
home to one or more monsters, which must be cleared out before you can claim the keep as yours."""

Vizier_desc = """At any time you choose within one year of drawing this card, you can ask a question in 
meditation and mentally receive a truthful answer to that question. Besides information, the answer helps 
you solve a puzzling problem or other dilemma. In other words, the knowledge comes with wisdom on how to apply it."""

Void_desc = """Your soul is drawn from your body and contained in an object in a place of the DM's choice. One or 
more powerful beings guard the place. While your soul is trapped in this way, your body is inert, ceases aging, 
and requires no food, air, or water. A Wish spell can't return your soul to your body, but the spell reveals the 
location of the object that holds your soul. You draw no more cards."""

Balance = Card(
    name="Balance",
    description=Balance_Desc,
    returnToDeck=True,
    in13Deck=False
)

Comet = Card(
    name="Comet",
    description=Comet_Desc,
    returnToDeck=True,
    in13Deck=False
)

Donjon = Card(
    name="Donjon",
    description=Donjon_Desc,
    returnToDeck=True,
    in13Deck=False
)

Fates = Card(
    name="The Fates",
    description=Fates_desc,
    returnToDeck=True,
    in13Deck=False
)

Fool = Card(
    name="Fool",
    description=Fool_desc,
    returnToDeck=False,
    in13Deck=False
)

Gem = Card(
    name="Gem",
    description=Gem_desc,
    returnToDeck=True,
    in13Deck=False
)

Idiot = Card(
    name="Idiot",
    description=Idiot_desc,
    returnToDeck=True,
    in13Deck=False
)

Talons = Card(
    name="Talons",
    description=Talons_desc,
    returnToDeck=True,
    in13Deck=False
)

Vizier = Card(
    name="Vizier",
    description=Vizier_desc,
    returnToDeck=True,
    in13Deck=False
)

Sun = Card(
    name="Sun",
    description=Sun_desc,
    returnToDeck=True,
    in13Deck=True
)

Moon = Card(
    name="Moon",
    description=Moon_desc,
    returnToDeck=True,
    in13Deck=True
)

Star = Card(
    name="Star",
    description=Star_desc,
    returnToDeck=True,
    in13Deck=True
)

Throne = Card(
    name="Throne",
    description=Throne_desc,
    returnToDeck=True,
    in13Deck=True
)

Key = Card(
    name="Key",
    description=Key_desc,
    returnToDeck=True,
    in13Deck=True
)

Knight = Card(
    name="Knight",
    description=Knight_desc,
    returnToDeck=True,
    in13Deck=True
)

Void = Card(
    name="Void",
    description=Void_desc,
    returnToDeck=True,
    in13Deck=True
)

Flames = Card(
    name="Flames",
    description=Flames_desc,
    returnToDeck=True,
    in13Deck=True
)

Skull = Card(
    name="Skull",
    description=Skull_desc,
    returnToDeck=True,
    in13Deck=True
)

Ruin = Card(
    name="Ruin",
    description=Ruin_desc,
    returnToDeck=True,
    in13Deck=True
)

Euryale = Card(
    name="Euryale",
    description=Euryale_desc,
    returnToDeck=True,
    in13Deck=True
)

Rogue = Card(
    name="Rogue",
    description=Rogue_desc,
    returnToDeck=True,
    in13Deck=True
)

Jester = Card(
    name="Jester",
    description=Jester_desc,
    returnToDeck=False,
    in13Deck=True
)


ALL_DOMT_CARDS = [
    Vizier,
	Sun,
	Moon,
	Star,
	Comet,
	Fates,
	Throne,
	Key,
	Knight,
	Gem,
	Talons,
	Void,
	Flames,
	Skull,
	Idiot,
	Donjon,
	Ruin,
	Euryale,
	Rogue,
	Balance,
	Fool,
	Jester
]

def get_cards_for_size_DOMT(size):
	if size == 13:
		return [
			card for card in ALL_DOMT_CARDS
			if card.in13Deck
		]

	elif size == 22:
		return ALL_DOMT_CARDS.copy()

	else:
		raise ValueError("Invalid Deck Size")

