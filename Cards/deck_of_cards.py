from random import shuffle


class DeckOfCards:
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = [(suit, value) for suit in self.SUITS for value in self.VALUES]
        self.is_created = False

    @property
    def is_created(self):
        return self._is_created

    @is_created.setter
    def is_created(self, value):
        self._is_created = value

    def shuffle_deck(self):
        shuffle(self.cards)
        self.is_created = True

    def sort_deck_by_suit(self):
        self.cards.sort(key=lambda card: (self.SUITS.index(card[0]), self.VALUES.index(card[1])))

    def sort_deck_by_value(self):
        self.cards.sort(key=lambda card: (self.VALUES.index(card[1]), self.SUITS.index(card[0])))

    def search_card(self, suit, value):
        try:
            return self.cards.index((suit, value))
        except ValueError:
            return -1


if __name__ == '__main__':
    deck = DeckOfCards()
    deck.shuffle_deck()
    deck.sort_deck_by_suit()  # Sort by suit
    deck.sort_deck_by_value()  # Sort by value

    # Searching for a card
    index = deck.search_card('Hearts', 'A')
    if index != -1:
        print(f"Card found at index {index}")
    else:
        print("Card not found")
