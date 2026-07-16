from app.core.cards.deck import Deck
from app.core.cards.doi_Data import get_DOI_Cards


class DeckOfIllusions(Deck):
	def __init__(self):
		cards = get_DOI_Cards()
		super().__init__(cards)