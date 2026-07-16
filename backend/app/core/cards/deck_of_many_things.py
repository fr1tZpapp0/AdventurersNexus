from app.core.cards.deck import Deck
from app.core.cards.domt_Data import get_cards_for_size_DOMT

class DeckOfManyThings(Deck):
	def __init__(self, size):
		cards = get_cards_for_size_DOMT(size)
		super().__init__(cards)

