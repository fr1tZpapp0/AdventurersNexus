from app.core.cards.deck import Deck
from app.core.cards.domt_Data import get_cards_for_size

class DeckOfManyThings(Deck):
	def __init__(self, size):
		cards = get_cards_for_size(size)
		super().__init__(cards)

