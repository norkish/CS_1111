import random

SUITS = ["♦️", "♣️", "❤️","♠️"]
RANKS = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

# card class
class Card:
    def __init__(self, _suit, _rank):
        self.suit = _suit
        self.rank = _rank

    def __str__(self):
        return self.suit + self.rank

# deck class
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __str__(self):
        return str([str(card) for card in self.cards])

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, _card):
        self.cards.append(_card)

    def value(self):
        value = 0
        for card in self.cards:
            card_idx = RANKS.index(card.rank)
            if card_idx == 12: # ace
                value += 11
            elif 9 <= card_idx <= 11: # face card
                value += 10
            else:
                value += (card_idx + 2)
        return value

    def __str__(self):
        return str([str(card) for card in self.cards])

# Program should:
# create and shuffle a deck of 52 cards
deck = Deck()
deck.shuffle()

# solicit number of players
num_players = int(input("How many players are there? "))
hands = [Hand() for i in range(num_players)]

# simulate a game of blackjack, allowing players to decide whether they want to hit or stay
# How to play 21:
# Each player is dealt two cards and tries to get as close to 21 as possible without going over.
for i in range(2):
    for hand in hands:
        hand.add_card(deck.deal_card())

# Number cards count as their value; face cards count as 10; Aces count as 1 or 11 (whichever is better for the hand).
# Players may hit (take another card) or stand (take no more cards).

for hand in hands:
    if hand.value() < 18:
        hand.add_card(deck.deal_card())

# If a player exceeds 21, they bust and automatically lose.

winner_value = 0
winner_idx = -1

for i in range(len(hands)):
    hand = hands[i]
    print("Player", i, ":", hand, hand.value())
    if 21 >= hand.value() > winner_value:
        winner_value = hand.value()
        winner_idx = i

print("Winner is Player", winner_idx, "!!!")
