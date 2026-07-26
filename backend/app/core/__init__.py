#
#   core/__init__.py
#

from backend.app.core.dice.dice import roll_dice, adv_or_dis
from backend.app.core.skills.skills import skills_list
from backend.app.core.combat.combat import armors_list, weapons_list
from backend.app.core.skills.modifiers import get_AbilityModifier


from backend.app.core.monsters.monsters import Monster
from backend.app.core.monsters.monsters import cr0_monsters
from backend.app.core.monsters.monsters import cr0125_monsters
from backend.app.core.monsters.monsters import cr025_monsters
from backend.app.core.monsters.monsters import cr05_monsters
from backend.app.core.monsters.monsters import cr1_monsters



from app.core.cards.card import Card
from app.core.cards.deck import Deck


from app.core.cards.deck_of_many_things import DeckOfManyThings
from app.core.cards.domt_Data import ALL_DOMT_CARDS

from app.core.cards.deck_of_illusions import DeckOfIllusions
from app.core.cards.doi_Data import ALL_DOI_CARDS