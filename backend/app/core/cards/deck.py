from random import choice, shuffle

class Deck:
	def __init__(self, cards):
		self.cards = cards

	def __str__(self):
		return f"Deck contains {len(self.cards)} cards"

	def draw(self):
		card = choice(self.cards)
		self.cards.remove(card)
		return card
	
	def shuffle_deck(self):
		shuffle(self.cards)

	def add_card(self, card):
		self.cards.append(card)

	def remove_card(self, card):
		self.cards.remove(card)

	def get_remaining(self):
		return len(self.cards)
	
