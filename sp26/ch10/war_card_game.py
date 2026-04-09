# Write a program that creates a deck of cards.
# Start by creating a list of suit strings and
# a list of rank strings, and then use these to create a deck.
import random

suits = ["♦️", "♣️", "❤️","♠️"]
ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

deck = []
for suit in suits:
    for rank in ranks:
        deck.append(suit+rank)

random.shuffle(deck)
random.shuffle(deck)
random.shuffle(deck)

print(deck)

# Implement a two-player game of War (for simplicity, assume
# on a tie, both players keep their own card).
player1_deck = deck[:len(deck)//2]
player2_deck = deck[len(deck)//2:]
# random.shuffle(player1_deck)
# random.shuffle(player2_deck)

while len(player1_deck) > 0 and len(player2_deck) > 0:
    print("P1 has", len(player1_deck), "cards and P2 has", len(player2_deck), "cards")
    player1_card = player1_deck.pop()
    player2_card = player2_deck.pop()
    print("P1 plays", player1_card, "cards and P2 plays", player2_card, "cards")

    player1_card_rank = player1_card[2:]
    player1_card_power = ranks.index(player1_card_rank)

    player2_card_rank = player2_card[2:]
    player2_card_power = ranks.index(player2_card_rank)

    if player1_card_power > player2_card_power:
        print("P1 wins!")
        player1_deck.insert(0,player1_card)
        player1_deck.insert(0, player2_card)
    elif player1_card_power < player2_card_power:
        print("P2 wins!")
        player2_deck.insert(0, player1_card)
        player2_deck.insert(0, player2_card)
    else:
        print("Tie!")
        player1_deck.insert(0, player1_card)
        player2_deck.insert(0, player2_card)
