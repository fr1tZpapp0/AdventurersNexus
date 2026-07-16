from dataclasses import dataclass

@dataclass
class Card:
    name: str
    description: str
    returnToDeck: bool
    in13Deck: bool

    def __str__(self):
        return f"{self.name} :: {self.description}"