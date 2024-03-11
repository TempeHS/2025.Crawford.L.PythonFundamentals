import random

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
random.shuffle(cards)
random.shuffle(suits)

def draw_card():
    return cards.pop() + ' of ' + suits.pop()

print (draw_card())

