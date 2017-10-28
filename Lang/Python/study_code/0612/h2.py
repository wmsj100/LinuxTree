import random
values = range(1, 11) + 'Jack Queen King'.split()
suits = 'spades hearts clubs diamonds'.split()
deck = ['%s of %s' % (value, suit) for value in values for suit in suits]
random.shuffle(deck)
while deck:
    raw_input(deck.pop())
