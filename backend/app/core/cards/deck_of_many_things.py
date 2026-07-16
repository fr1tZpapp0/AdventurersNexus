from random import choice, shuffle
from deck import Deck
from card import Card
from domt_Data import get_cards_for_size, ALL_DOMT_CARDS

class DeckOfManyThings(Deck):
	def __init__(self, size):
		cards = get_cards_for_size(size)
		super().__init__(cards)

